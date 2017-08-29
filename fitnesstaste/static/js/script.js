var show_reason = $('#show_reason').click(function(e){
	e.preventDefault()
	if($('.video_left').length + $('.video_right').length < 4){
		//alert($('div.video_left').length + $('div.video_right').length);
		var left_video = $('.video_left').clone().appendTo('#videos');
		var right_video = $('.video_right').clone().appendTo('#videos');
		$(this).text('Скрыть 2 причины');
	}
	else{
		$('.video_left:last').remove();
		$('.video_right:last').remove();
		$(this).text('Показать еще 2 причины');
	}

});
