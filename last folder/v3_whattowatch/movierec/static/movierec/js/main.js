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
  		var title = $(this).attr("data-target");
		$(title).on('hidden.bs.modal', function(e) {
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
		if($('#from').find(":selected").text() === "-----"){
			$('#from').val(op);
		}
		if(op !== "-----"){
			$("#from option[value='-----'").prop('disabled', false);
		}
	});

	$('body #netflix').on('click', function() {
	    if($('#netflix').css('border') == '0px none rgb(255, 255, 255)'){
	    	$('#netflix').css({"border": "2px solid orange"});
	    	$( "input[name='netflix']" ).prop("checked", true);
	    }
	    else if($('#netflix').css('border') == '2px solid rgb(255, 165, 0)'){
	    	$('#netflix').css({"border": "0px none rgb(255, 255, 255)"});
	    	$( "input[name='netflix']" ).prop("checked", false);
	    }
	}); 

	$('body #amazon').on('click', function() {
	    if($('#amazon').css('border') == '0px none rgb(255, 255, 255)'){
	    	$('#amazon').css({"border": "2px solid orange"});
	    	$( "input[name='amazon']" ).prop("checked", true);
	    }
	    else if($('#amazon').css('border') == '2px solid rgb(255, 165, 0)'){
	    	$('#amazon').css({"border": "0px none rgb(255, 255, 255)"});
	    	$( "input[name='amazon']" ).prop("checked", false);
	    }
	}); 

	$('body #hulu').on('click', function() {
	    if($('#hulu').css('border') == '0px none rgb(255, 255, 255)'){
	    	$('#hulu').css({"border": "2px solid orange"});
	    	$( "input[name='hulu']" ).prop("checked", true);
	    }
	    else if($('#hulu').css('border') == '2px solid rgb(255, 165, 0)'){
	    	$('#hulu').css({"border": "0px none rgb(255, 255, 255)"});
	    	$( "input[name='hulu']" ).prop("checked", false);
	    }
	}); 

	$(function() {
		var items = [ 'Germany', 'Brazil', 'Portugal', 'Morocco', 'New Zealand', 'France', 'Italy', 'Malta', 'England', 
		'Australia', 'Spain', 'Scotland', "eat, pray, love" ];
		var input = $('#people');
		var flag = false;

		function split( val ) {
			return val.split( /,\s*/ );
		}
		function extractLast( term ) {
			return split( term ).pop();
		}

		input.autocomplete({
			minLength: 0,
			source: function( request, response ) {
				response( $.ui.autocomplete.filter(
					items, extractLast( request.term ) 
				));
			},
			focus: function() {
				return false;
			},
			select: function( event, ui ) {
				$(".people").children(".tag").each(function(index){
					if($(this).text() === ui.item.value){
						flag = true;
					}
				});
				if(!flag){
					$(this).val("");
					$('#people').before('<span class="tag">' + ui.item.value + '</span>');
					$(".people").append('<input type="hidden" name="people" value="' + ui.item.value + '">');
				}
				flag = false;

				if($(".people").find(".tag").length !== 0){
					input.removeAttr('placeholder');
				}
				return false;
			}
		});
		$(document).on('click', '.tag', function(){
			$(this).remove();
	    });
		input.on('keydown', function() {
			var key = event.keyCode || event.charCode;

			if( key == 8 || key == 46 ){
				if(!input.val()){
					$(".people").children(".tag").last().remove();
					if($(".people").find(".tag").length === 0){
						input.attr("placeholder", "Will Smith");
					}
					return false;
				}
			}
		});
	});

	$(window).load(function(){
		$(".nav").find("a").each(function(){
			if($(this).attr("href") === $(".hide_name").text()){
				$(this).addClass("active");
			}
			else if($(this).hasClass("active")){
				$(this).removeClass("active");
			}
		});

    	return false;

	});

});
