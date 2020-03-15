from django.shortcuts import render
from .models import News,NewsCategory,Comment,Banner
from django.conf import settings
from .serializers import NewsSerializer,CommentSerizlizer
from django.http import Http404
from utils import restful
from .forms import PublicCommentForm
from apps.xfzauth.decorators import xfz_login_required
from django.db.models import Count

# Create your views here.
def index(request):
    count=settings.ONE_PAGE_NEWS_COUNT
    newses=News.objects.order_by('-pub_time')[0:count]
    categories=NewsCategory.objects.all()
    sidebars = News.objects.order_by('-pub_time').first()
    context={
        'newses':newses,
        'categories':categories,
        'banners':Banner.objects.all(),
        'sidebars': sidebars
    }
    print(sidebars.pub_time)

    return render(request,'news/index.html',context=context)
# def sidebar(request):
#     sidebars = News.objects.order_by('-pub_time').first()
#     context={
#         'sidebars': sidebars
#     }
#     print(sidebars.pub_time)
#     return render(request,"common/sidebar.html",context=context)

def news_list(request):
    # 通过p参数，来指定要获取第几页的数据
    # 并且这个p参数，是通过查询字符串的方式传过来的/news/list/?p=2
    page = int(request.GET.get('p',1))
    # 分类为0：代表不进行任何分类，直接按照时间倒序排序
    category_id = int(request.GET.get('category_id',0))
    # 0,1
    # 2,3
    # 4,5
    start = (page-1)*settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT

    if category_id == 0:
        # QuerySet
        # {'id':1,'title':'abc',category:{"id":1,'name':'热点'}}
        newses = News.objects.select_related('category','author').all()[start:end]
    else:
        newses = News.objects.select_related('category','author').filter(category__id=category_id)[start:end]
    serializer = NewsSerializer(newses,many=True)
    data = serializer.data
    return restful.result(data=data)


def news_detail(request,news_id):
    try:
        news = News.objects.select_related('category','author').get(pk=news_id)
        counts=News.objects.filter(pk=news_id).annotate(news_type=Count("comments"))
        context = {
            'news': news,
            'counts':counts
        }

        for count in counts:
            print(count.news_type)

        return render(request,'news/news_datail.html',context=context)
    except News.DoesNotExist:
        raise Http404
@xfz_login_required
def public_comment(request):
    form = PublicCommentForm(request.POST)
    if form.is_valid():
        news_id = form.cleaned_data.get('news_id')
        content = form.cleaned_data.get('content')
        news = News.objects.get(pk=news_id)
        comment = Comment.objects.create(content=content,news=news,author=request.user)

        serizlize = CommentSerizlizer(comment)
        return restful.result(data=serizlize.data)
    else:
        return restful.params_error(message=form.get_errors())



def search(request):
    return render(request,'search/search.html')