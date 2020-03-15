from django.urls import path
from . import views
from . import course_views
app_name='cms'
urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('index/',views.index_view,name="index"),
    path('news_list/',views.NewsListView.as_view(),name='news_list'),
    path('edit_news/',views.EditNewsView.as_view(),name='edit_news'),
    path('write_news/', views.WriteNewsView.as_view(), name='write_news'),
    path('delete_news/',views.delete_news,name='delete_news'),
    path('news_category/',views.news_category,name="news_category"),
    path('add_news_category/',views.add_news_category,name="add_news_category"),
    path('edit_news_category/',views.edit_news_category,name="edit_news_category"),
    path('delete_news_category/',views.delete_news_category,name="delete_news_category"),
    path('news_list/',views.news_list,name="news_list"),
    path('upload_file/',views.upload_file,name="upload_file"),
    path('qntoken/',views.qntoken,name="qntoken"),
    path('banners/',views.banners,name='banners'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('banner_list/',views.banner_list,name='banner_list'),
    path('delete_banner/',views.delete_banner,name='delete_banner'),
    path('edit_banner/',views.edit_banner,name='edit_banner'),
    path('course_list/',views.CourseListView.as_view(),name='course_list'),
    path('edit_course/',views.EditCourse.as_view(),name='edit_course'),
    path('delete_course/', views.delete_course, name='delete_course'),

]
# 这是课程相关的url映射
urlpatterns += [
    path('pub_course/',course_views.PubCourse.as_view(),name='pub_course'),

]