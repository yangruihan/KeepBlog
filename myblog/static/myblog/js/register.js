$(document).ready(function () {
	// 当用户名框失去焦点时，进行重复检测
    $(".username").blur(function () {
		$.get("/myblog/username_check/",{'username': $(this).val()}, function(result){
	        $(".alert").html(result);
	    });
	});
});