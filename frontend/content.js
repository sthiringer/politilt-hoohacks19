/*
Content script for slant browser extension
*/

var API_ENDPOINT = 'https://theslantapp.com/score';
$(document).ready( function() { 

chrome.runtime.onMessage.addListener( function gotMessage( message, sender, sendResponse ) {
		//Send HTTP request with this stuff to the server
		var raw_HTML = document.documentElement.outerHTML;
		var url = window.location.href;

		let data_obj = {"text":raw_HTML, "source":url};

		$.ajax({
		    url: API_ENDPOINT,
		    dataType: 'json',
		    type: 'post',
		    contentType: 'application/json',
		    data: JSON.stringify(data_obj),
		    processData: true,
		    success: onGetScore,
		    error: function( jqXhr, textStatus, errorThrown ){
		        console.log( 'error getting score:', errorThrown );
		    }
		});
		
	})
});


var onGetScore = function(data){
	var div1 = $("div:first");
	console.log( div1 );

	// Our logo
	var ImgURL = chrome.extension.getURL( 'logo.svg' );
	
	//Create HTML structure for modal
	$('<style>body {font-family: Arial, Helvetica, sans-serif;}/* The Modal (background) */.modal { /* Hidden by default */position: fixed; /* Stay in place */z-index: 999999; /* Sit on top */padding-top: 100px; /* Location of the box */left: 0;top: 0;width: 100%; /* Full width */height: 100%; /* Full height */overflow: auto; /* Enable scroll if needed */background-color: rgb(0,0,0); /* Fallback color */background-color: rgba(0,0,0,0.4); /* Black w/ opacity */}/* Modal Content */.modal-content {background-color: #fefefe;margin: auto;padding: 20px;border: 1px solid #888;width: 80%;height: 200px;position:relative}/* The Close Button */.close {color: #aaaaaa;float: right;font-size: 28px;font-weight: bold;}.close:hover,.close:focus {color: #000;text-decoration: none;cursor: pointer;}</style><div id="myModal" class="modal"><div class="modal-content"><span id="close">&times;</span></div></div>').insertBefore( div1 );
	$('#close').css({
		"font-size":"30px",
		"float":"right"
	})
	$('#close').hover(function() {
		$(this).css({'cursor':'pointer'});
	})


	var slantDiv = $("#myModal > .modal-content");
	$( slantDiv ).css( { "position":"relative", "width":"1100px" } );
	console.log( slantDiv );

	// Animates our new div to slide down (looks nice)
	$( slantDiv ).prepend($('<div>', {id:'triangledown'} ) );
	$( slantDiv ).prepend($('<div>', {id:'bar'} ) );
	$( slantDiv ).prepend($('<img>', {id:'SlantLogo', src:ImgURL} ) );
	$( slantDiv ).prepend($('<p>', {id:'response'} ) );
	$( slantDiv ).prepend($('<button>', {id:'saysWhoButton'} ) );
	$('#saysWhoButton').html("Says who?")

	//Bias calculations
	var bias = 59 + ( data.score * 36 );
	var biasString = bias + "%";

	var presentedBias = data.score * 100;
	var pBiasTrunc = presentedBias.toFixed(2);
	var pBias = pBiasTrunc + "%";
	var lor;
	if ( presentedBias < 0 ) {
		lor = "left";
		pBias = ( presentedBias * -1 ) + "%"; 
	}
	else if ( presentedBias > 0 ) {
		lor = "right";
	}
	else {
		lor = "most part";
		pBias = "extremeley low"
	}

	//Style response
	$( "#response" ).append( "This site has a " + pBias + " bias for the " + lor + "." );
	$( "#response" ).css( { 
		"font-size":"18px",
		"color":"Black",
		"position":"absolute",
		"left": "400px"
	})



	//Style triangledown
	$( "#triangledown" ).css( { 
		"border-left":"10px solid transparent",
		"border-right":"10px solid transparent",
		"border-top":"25px solid",
		"left":"59%",
		"bottom":"50px",
		"width":"10px",
		"position":"absolute"
	})
	

	//Style logo
	$( "#SlantLogo" ).attr( 'width', '200' );
	$( "#SlantLogo" ).attr( 'align', 'left' ); 
	$( "#SlantLogo" ).attr( 'hspace', '50' );
	$( "#SlantLogo" ).attr( 'border', '50' );
	$("#SlantLogo ").css({
		"width":"200px", 
		"height":"auto",
		"margin":"0",
		"border":"0"
	})

	//Style bias scale
	$( "#bar" ).css({
	 "width":"75%",
	 "height":"35px", 
	 "background-image":"linear-gradient(to right, rgb(11, 36, 251), rgb(252, 13, 27)", 
	 "border-radius":"7px",
	 "left":"22%",
	 "position":"absolute",
	 "bottom":"30px"
	})

	//Style button
	$('#saysWhoButton').css({
		"position":"absolute",
		"left":"50px",
		"bottom":"30px",
		"height":"35px",
		"width":"100px",
		"background-color":"black",	
		"border-radius":"7px",
		"color":"white"
	})

	$('#saysWhoButton').click(function(){
		window.location.href = 'https://github.com/sthiringer/slant'
	}).hover(function() {
		$(this).css({'cursor':'pointer'});
	})

	$('#close').click(function(){
		$('#myModal').css({"display":"none"})
	})

	$( "#triangledown" ).animate( { left: biasString }, 1500 );

};