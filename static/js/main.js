	$(document).on("scroll", function(){
		if
      ($(document).scrollTop() > 86){
		  $("#banner").addClass("shrink");
		}
		else
		{
			$("#banner").removeClass("shrink");
		}
    });
    

function toggle(){
    var blur = document.getElementById("home");
    blur.classList.toggle('active');
    var log = document.getElementById("log");
    log.classList.toggle('active');
    document.getElementById("log").style.display = 'block';
}

