$( document ).ready(function() {
	var arrow = $('.arrow');
	var tile = 211;
	var animationSpeed = 450;
	var window_size = $(window).width() - 30;
	var numTiles = window_size/tile | 0;
	var carousel = new Array();
	var numberOfTiles = new Array();

	arrow.on('click', function(){
		var side = $(this).attr('data-arrow');
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
			// console.log("Carousel is: " + carousel[id] + " max should be: " + ((tile - 26) * numberOfTiles[id]));
			// console.log("Number of tiles " + numberOfTiles[id]);
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



  	$(".tile").on("click", function(){
  		var title = $(this).find(".tile__title").text().trim().replace(":", "").replace(";", "").split(" ");
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
		$('#myModal' + realTitle).on('hidden.bs.modal', function(e) {
	    	$(this).find('iframe').attr('src', $(this).find('iframe').attr('src'));
	    	// $(this).find('iframe').attr('src', rawVideoURL);
		});
 	})

  	var from = $("#from");
	var to = $("#to");
	for (i = new Date().getFullYear(); i > 1877; i--) {
		if(i == new Date().getFullYear()){
	    	from.append($('<option />').val(i).html("-----"));
	    	to.append($('<option />').val(i).html("-----"));
	    }
	    from.append($('<option />').val(i).html(i));
	    to.append($('<option />').val(i).html(i));
	}
	from.change(function(){
		var op = from.val();
		$('#to option').filter(function() {
		    return $(this).val() < op;
		}).prop('disabled', true);
		$('#to option').filter(function() {
		    return $(this).val() >= op;
		}).prop('disabled', false);
	});
	to.change(function(){
		var op = to.val();
		$('#from option').filter(function() {
		    return $(this).val() > op;
		}).prop('disabled', true);
		$('#from option').filter(function() {
		    return $(this).val() <= op;
		}).prop('disabled', false);
	});

    var data = ["Boston Celtics", "Chicago Bulls", "Miami Heat", "Orlando Magic", "Atlanta Hawks", "Philadelphia Sixers", "New York Knicks", "Indiana Pacers", "Charlotte Bobcats", "Milwaukee Bucks", "Detroit Pistons", "New Jersey Nets", "Toronto Raptors", "Washington Wizards", "Cleveland Cavaliers"];
    $("#people").autocomplete({source:data});

});
