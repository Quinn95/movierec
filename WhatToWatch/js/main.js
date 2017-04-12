$( document ).ready(function() {
	var arrow = $('.arrow');
	var tile = 211;
	var animationSpeed = 450;
	var carousel = new Array();
	var numberOfTiles = new Array();

	arrow.on('click', function(){
		var side = $(this).attr('data-arrow');
		var window_size = $(window).width() - 30;
		var numTiles = window_size/tile | 0;
		var id = side.split(" ")[1];

		if(carousel[id] == undefined){
			carousel[id] = 0;
		}

		if(numberOfTiles[id] == undefined){
			numberOfTiles[id] = $(".c" + id).children(".tile").length;
		}

		if(side.split(" ")[0] == "left"){
			carousel[id] = carousel[id] - numTiles * tile;
			$(".c" + id).animate({scrollLeft: carousel[id]}, animationSpeed);
			if(carousel[id] == 0){
				$('.left' + id).hide();
			}
			if(carousel[id] < ((tile - 26) * numberOfTiles[id])){
				$('.right' + id).fadeTo(10, 1);
				$('.right' + id).removeAttr("disabled");
			}
		} 
		else{
			carousel[id] = carousel[id] + numTiles * tile;
			if(carousel[id] != 0){
				$('.left' + id).show();
			}
			// if(carousel[id] = )
			$(".c" + id).animate({scrollLeft: carousel[id]}, animationSpeed);
			if(carousel[id] >= ((tile - 26) * numberOfTiles[id])){
				$('.right' + id).fadeTo(10, 0);
				$('.right' + id).attr("disabled", "disabled");
			}
		}

	});


  // $("body").on('hidden.bs.modal', function (e) {
  //   var $iframes = $(e.target).find("iframe");
  //   $iframes.each(function(index, iframe){
  //     $(iframe).attr("src", $(iframe).attr("src"));
  //   });
  // });


  $(".tile").on("click", function(){
  	var title = $(this).find(".tile__title").text().trim().replace(":", "").replace(";", "").split(" ");
  	console.log(title);
  	var realTitle;
  	if(title.length != 1){
  		for (var i = 0; i < title.length; i++) {
  			if(realTitle == undefined){
  				realTitle = title[i];
  			}
  			else{
  				realTitle = realTitle + title[i];
  			}
  		}
  	}
  	else{
  		realTitle = title;
  	}
  	console.log(realTitle);
	$('#myModal' + realTitle).on('hidden.bs.modal', function(e) {
	    $(this).find('iframe').attr('src', $(this).find('iframe').attr('src'));
	    // $(this).find('iframe').attr('src', rawVideoURL);
	});
  })




});