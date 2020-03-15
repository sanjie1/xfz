
function PubCourse() {

}

PubCourse.prototype.initUEditor = function () {
    window.ue = UE.getEditor("editor",{
        'serverUrl': '/ueditor/upload/'
    });
};

PubCourse.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function () {
        var btn = $(this);
        var title = $("#title-input").val();
        var category_id = $("#category-input").val();
        var teacher_id = $("#teacher-input").val();
        var video_url = $("#video-input").val();
        var cover_url = $("#cover-input").val();
        var price = $("#price-input").val();
        var duration = $("#duration-input").val();
        var pk = btn.attr('data-news-id');
        var profile = window.ue.getContent();
        var url = '';
        if(pk){
            url = '/cms/edit_course/';
        }else{
            url = '/cms/pub_course/';
        }

        xfzajax.post({
            'url': url,
            'data': {
                'title': title,
                'video_url': video_url,
                'cover_url': cover_url,
                'price': price,
                'duration': duration,
                'profile': profile,
                'category_id': category_id,
                'teacher_id': teacher_id,
                'pk':pk
            },
            'success': function (result) {
                if(result['code'] === 200){
                    window.location = window.location.href;

                }
            }
        });
    });
};

PubCourse.prototype.run = function () {
    this.initUEditor();
    this.listenSubmitEvent();
};


$(function () {
    var course = new PubCourse();
    course.run();
});