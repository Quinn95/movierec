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
			if(carousel[id] != 0){
				$('.left' + id).show();
			}
			$(".c" + id).animate({scrollLeft: carousel[id]}, animationSpeed);
			if(carousel[id] >= ((tile - 26) * numberOfTiles[id])){
				$('.right' + id).fadeTo(10, 0);
				$('.right' + id).attr("disabled", "disabled");
			}
		}

	});

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
		if(to.find(":selected").text() === "-----" && op != "-----"){
			to.val($("#to option").eq(1).val());
		}
		if(op == "-----"){
			to.val("-----");
		}
	});
	to.change(function(){
		var op = to.val();
		$('#from option').filter(function() {
		    return $(this).val() > op;
		}).prop('disabled', true);
		$('#from option').filter(function() {
		    return $(this).val() <= op;
		}).prop('disabled', false);
		if(from.find(":selected").text() === "-----"){
			from.val(op);
		}
		if(op !== "-----"){
			$("#from option[value='-----'").prop('disabled', false);
		}
	});

	$('.streaming-services-search #netflix').on('click', function() {
		imageSearch("netflix");
	}); 

	$('.streaming-services-search #amazon').on('click', function() {
		imageSearch("amazon");
	}); 

	$('.streaming-services-search #hulu').on('click', function() {
		imageSearch("hulu");
	}); 

	$('.streaming_choice #netflix').on('click', function() {
		image("netflix");
	}); 

	$('.streaming_choice #amazon').on('click', function() {
		image("amazon");
	}); 

	$('.streaming_choice #hulu').on('click', function() {
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
	});

	$(document).on('click', '.tag', function(){
		var parent = $(this).parent();
		var text = parent.attr("class");
		$(this).remove();
		if(parent.find(".tag").length === 0){
			renew(text);
		}
    });

	$(window).load(function(){
		$(".nav").find("a").each(function(){

			if($(this).attr("href").trim() === $(".hide_name").text().trim()){
				$(this).addClass("active");
				if($(".search_page").length !== 0){
					$(".navbar-brand").hide();
				} else{
					$(".navbar-brand").show();
				}
			}
			else if($(this).hasClass("active")){
				$(this).removeClass("active");
			}
		});

    	return false;

	});
	$(window).scroll(function(){
	    if ($(window).scrollTop() > 300) {
	    	$(".navbar-brand").fadeIn();
	    } else {
	       	if($(".search_page").length !== 0){
	       		$(".navbar-brand").fadeOut();
	       	}
	    }
	});

	$(".stream").css({"margin-top": $("#search_img").height()/4});

  $("#recommendation").on('submit', function(e){
    e.preventDefault();
    var pep = new Array();
    var key = new Array();
    $(".people").children(".tag").each(function(){
      pep.push($(this).text());
    });
    $(".keywords").children(".tag").each(function(){
      key.push($(this).text());
    });

    $.ajax({
        url: $(this).attr("action"),
        type: "POST",
        data: {
          from: $("#from").val(),
          to: $("#to").val(),
          genre: $("#genre").val(),
          imdb: $("#imdb").val(),
          rating: $("#rating").val(),
          language: $("#language").val(),
          'people[]': pep,
          keywords: key.toString(),
          netflix: $("#n").is(":checked"),
          amazon: $("#a").is(":checked"),
          hulu: $("#h").is(":checked"),
          csrfmiddlewaretoken: $(this).find("input[name='csrfmiddlewaretoken']").val()},


        // handle a successful response
        success: function(data) {
        	$("#insert").empty();
	        $("#insert").append(data.split("<!-- END -->")[1]);
	        modal();
	        // console.log(data.split("<!-- END -->")[1])
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
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

function imageSearch(input){
    if($('#'+input).css('border') == '0px none rgb(255, 255, 255)'){
    	$('#'+input).css({"border": "2px solid red"});
    	$( "input[name='"+input+"']" ).prop("checked", true);
    }
    else if($('#'+input).css('border') == '2px solid rgb(255, 0, 0)'){
    	$('#'+input).css({"border": "0px none rgb(255, 255, 255)"});
    	$( "input[name='"+input+"']" ).prop("checked", false);
    }		
}
function renew(input){
	if(input === "keywords"){
		$("#" + input).attr("placeholder", "Alice, Man, Spider");
	}
	else{
		$("#" + input).attr("placeholder", "Will Smith");
	}
}
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
function modal(){
  	$(".tile").on("click", function(){
  		var title = $(this).attr("data-target");
  		$(title).on('shown.bs.modal', function(){
  			var youtube = $(this).find("#video").val();

  			var iframe_div = $(this).find(".col-lg-8");

  			if(iframe_div.find("iframe").length){
  				if(iframe_div.find("input").attr("name") === "bunny"){
  					iframe_div.find('iframe').attr('src', iframe_div.find('iframe').attr('src')+"&autoplay=1");
  				}
  			} else if(iframe_div.find("input").attr("name") === "trailer"){
  				iframe_div.prepend("<iframe id='vid' src='"+youtube+"' allowfullscreen></iframe>");
  			} else if(iframe_div.find("input").attr("name") === "bunny"){
  				$("<iframe class='ytplayer' id='vid' src='"+youtube+"&autoplay=1' volume='0'></iframe>").insertAfter($("#no-trailer"));
  				var mute = iframe_div.find('iframe');
  			}

  			var frame = $(title).find("#vid").width()/100;
  			frame = frame * 62.5;
			$(".video-container iframe").height(frame);

			var id = $(this).attr("id");
			$(".up" + id).on('click', function(){
				$(this).css({"background-color": "orange"});

				if( $(".down" + id).css("background-color") == 'rgb(255, 165, 0)'){
					$(".down" + id).css({"background-color": "white"});
				}
			});
			$(".down" + id).on('click', function(){
				$(this).css({"background-color": "orange"});

				if( $(".up" + id).css("background-color") == 'rgb(255, 165, 0)'){
					$(".up" + id).css({"background-color": "white"});
				}
			});
  		});

  		$(window).resize(function(){
  			var frame = $(title).find("#vid").width()/100;
  			frame = frame * 62.5;
			$(".video-container iframe").height(frame);

			$(".description .row").each(function(){
				if($(window).width() < 540){
					$(this).removeClass("row-eq-height");
				}
			});
  		});

		$(title).on('hidden.bs.modal', function(e) {
			if($(this).find('input').attr("name") === "bunny"){
				var link = $(this).find('iframe').attr("src");
				var new_link = link.substring(0, link.length-11);
				$(this).find('iframe').attr('src', new_link);
			} else{
	    		$(this).find('iframe').attr('src', $(this).find('iframe').attr('src'));
	    	}
		});
 	});
}
