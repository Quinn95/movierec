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
  		$(title).on('shown.bs.modal', function(){
  			var frame = $(title).find("#vid").width()/100;
  			frame = frame * 62.5;
			$(".video-container iframe").height(frame);
  		});
  		$(window).resize(function(){
  			var frame = $(title).find("#vid").width()/100;
  			frame = frame * 62.5;
			$(".video-container iframe").height(frame);
  		});

		$(title).on('hidden.bs.modal', function(e) {
	    	$(this).find('iframe').attr('src', $(this).find('iframe').attr('src'));
		});
 	})

  	var from = $("#from");
	var to = $("#to");
	for (i = new Date().getFullYear(); i > 1877; i--) {
		if(i == new Date().getFullYear()){
	    	from.append($('<option />').val("-----").html("-----"));
	    	to.append($('<option />').val("-----").html("-----"));
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
		image("netflix");
	}); 

	$('body #amazon').on('click', function() {
		image("amazon");
	}); 

	$('body #hulu').on('click', function() {
		image("hulu");
	}); 

	$(".people").on("click", function(){
		$("#people").focus();
	});
	$(".keywords").on("click", function(){
		$("#keywords").focus();
	});

	$('#people').on('keydown', function(e) {
   		if(e.which == 13) {
   			var flag = false;
   			e.preventDefault();
        	$(".people").children(".tag").each(function(){
				if($("#people").val() === $(this).text()){
					flag = true;
				}
			});
			if(!flag){
				$('#people').before('<span class="tag">' + $(this).val() + '<div class="bar"></div><i class="fa fa-close"></i></span>');
				$(".people").append('<input type="hidden" name="people" value="' + $(this).val() + '">');
				$(".people").scrollLeft($(".people").scrollLeft() + $(".people").children(".tag").last().width() + 4);
				$(this).val("");
			}
			flag = false;

			if($(".people").find(".tag").length !== 0){
				input.removeAttr('placeholder');
			}
    	}
    	var key = event.keyCode || event.charCode;

			if( key == 8 || key == 46 ){
				if(!$("#people").val()){
					$(".people").children(".tag").last().remove();
					if($(".people").find(".tag").length === 0){
						renew("people");
					}
					return false;
				}
			}
	});
	$(function() {
		var items = $("#hidden_keywords").val().split(",");
		if(items[items.length - 1] === "" || items[items.length - 1] === " "){
			items.pop();
		}
		var input = $('#keywords');
		var size = input.width();
		var flag = false;

		input.autocomplete({
			minLength: 0,
			autoFocus: true,
			source: function( request, response ) {
				response( $.ui.autocomplete.filter(
					items, extractLast( request.term ) 
				));
			},
			focus: function(event, ui) {
				event.preventDefault();
				return false;
			},
			select: function( event, ui ) {
				$(".keywords").children(".tag").each(function(index){
					if($(this).text() === ui.item.value){
						flag = true;
					}
				});
				if(!flag){
					$(this).val("");
					$('#keywords').before('<span class="tag">' + ui.item.value + '<div class="bar"></div><i class="fa fa-close"></i></span>');
					$(".keywords").append('<input type="hidden" name="keywords" value="' + ui.item.value + '">');
					$(".keywords").scrollLeft($(".keywords").scrollLeft() + $(".keywords").children(".tag").last().width() + 4);
				}
				flag = false;

				if($(".keywords").find(".tag").length !== 0){
					input.removeAttr('placeholder');
				}
				return false;
			}
		});
		backspace("keywords");
		// input.on('keydown', function(e){
		// 	if(e.which == 13) {
		// 		e.preventDefault();
		// 	} else{
		// 		$("#ui-id-2").addClass("ui-state-focus");
		// 		// console.log($())
		// 	}
		// });
	});

	function split( val ) {
		return val.split( /,\s*/ );
	}
	function extractLast( term ) {
		return split( term ).pop();
	}

	function backspace(input) {
		$("#" + input).on("keydown", function(e){
			var key = event.keyCode || event.charCode;

			if( key == 8 || key == 46 ){
				if(!$("#" + input).val()){
					console.log($(".people").children(".tag").length);
					$("." + input).children(".tag").last().remove();
					if($("." + input).find(".tag").length === 0){
						renew(input);
					}
					return false;
				}
			}
			if(e.which == 13){
				event.preventDefault();
			}
		});
	};
	$(document).on('click', '.tag', function(){
		var parent = $(this).parent();
		var text = parent.attr("class");
		$(this).remove();
		if(parent.find(".tag").length === 0){
			renew(text);
		}
    });
    function renew(input){
		if(input === "keywords"){
			$("#" + input).attr("placeholder", "Alice, Man, Spider");
		}
		else{
			$("#" + input).attr("placeholder", "Will Smith");
		}
    }

	$(window).load(function(){
		$(".nav").find("a").each(function(){

			if($(this).attr("href").trim() === $(".hide_name").text().trim()){
				$(this).addClass("active");
				if($(".search_page") !== null){
					$(".navbar-brand").addClass("hide_name");
				}
			}
			else if($(this).hasClass("active")){
				$(this).removeClass("active");
			}
		});

    	return false;

	});

	$("#up").on('click', function(){
		$(this).css({"background-color": "orange"});
		if( $("#down").css("background-color") == 'rgb(255, 165, 0)'){
			$("#down").css({"background-color": "white"});
		}
	});
	$("#down").on('click', function(){
		$(this).css({"background-color": "orange"});
		if( $("#up").css("background-color") == 'rgb(255, 165, 0)'){
			$("#up").css({"background-color": "white"});
		}
	});

});

function image(input){
    if($('#'+input).css('border') == '0px none rgb(255, 255, 255)'){
    	$('#'+input).css({"border": "2px solid orange"});
    	$( "input[name='"+input+"']" ).prop("checked", true);
    }
    else if($('#'+input).css('border') == '2px solid rgb(255, 165, 0)'){
    	$('#'+input).css({"border": "0px none rgb(255, 255, 255)"});
    	$( "input[name='"+input+"']" ).prop("checked", false);
    }		
}
