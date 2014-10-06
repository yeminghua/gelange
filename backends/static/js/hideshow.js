//  Andy Langton's show/hide/mini-accordion @ http://andylangton.co.uk/jquery-show-hide

// this tells jquery to run the function below once the DOM is ready
$(document).ready(function() {

// choose text for the show/hide link - can contain HTML (e.g. an image)
var showText='显示';
var hideText='隐藏';

// initialise the visibility check
var is_visible = false;

// append show/hide links to the element directly preceding the element with a class of "toggle"
$('.toggle').prev().append(' <a href="#" class="toggleLink">'+hideText+'</a>');

// hide all of the elements with a class of 'toggle'
$('.toggle').show();

// capture clicks on the toggle links
$('a.toggleLink').click(function() {

// switch visibility
is_visible = !is_visible;

// change the link text depending on whether the element is shown or hidden
if ($(this).text()==showText) {
$(this).text(hideText);
$(this).parent().next('.toggle').slideDown('slow');
}
else {
$(this).text(showText);
$(this).parent().next('.toggle').slideUp('slow');
}

// return false so any link destination is not followed
return false;

});


//添加一级列表时候的正常显示为英文表中的内容。
$('#select_language').change(function(){
	val = $('#select_language').val();
	if(val == "chinese"){
		href = '/get_contents/chinese';
		$.ajax({
            url: href,
            // 从服务器上获取数据,为中文对应的contents
            type: 'get',
            async : false,
            success: function(data){
            	// alert(data);
            	$('#linhc_control_contents').html(data);             	
            }})
	}else{
		href = '/get_contents/english';
		$.ajax({
            url: href,
            // 从服务器上获取数据,为英文对应的contents
            type: 'get',
            async : false,
            success: function(data){
            	// alert(data);
            	$('#linhc_control_contents').html(data);             	
            }})
	}


	}
	)






});