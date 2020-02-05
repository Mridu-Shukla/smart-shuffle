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

// $(document).ready(function(){
	$('.owl-carousel').owlCarousel({
		loop:true,
		margin:10,
		responsiveClass:true,
		responsive:{
			0:{
				items:1,
				nav:true
			},
			600:{
				items:3,
				nav:false
			},
			1000:{
				items:5,
				nav:true,
				loop:false
			}
		}
	})
//   });

// window.onclick = function(event) {
//     if (event.target == document.getElementById("log")) {
//         document.getElementById("log").style.display = 'none';
//         var blur = document.getElementById("home");
//     blur.classList.toggle('active');
//     }
// }

