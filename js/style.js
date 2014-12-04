function changeInner()
{
	var obj=document.getElementById("hello");
	if (obj.innerHTML=="Hello World, This is PROJ_R ! ")
		obj.innerHTML="Hello World";
	else
		obj.innerHTML="Hello World, This is PROJ_R ! ";
}


function buttonAnimation()
{
	$(document).ready
	(
		function()
		{
			$("img").hover
			(
				function()
				{
					$(this).animate({left:'+=5px'});
				}
			);
		}
	);
}