$(document).ready( function() { 

console.log( "Chrome extension go" );

chrome.runtime.onMessage.addListener( function gotMessage( message, sender, sendResponse ) {
	//Send HTTP request with this stuff to the server
		var raw_HTML = document.documentElement.outerHTML;
		console.log(raw_HTML);





		// Re-format the website
		// BAD SOLUTION
		//document.body.style.marginTop = "75px";

		// GOOD SOLUTION

		var div1 = $("div:first");
		console.log( div1 );
		// Our image
		var ImgURL = chrome.extension.getURL( 'SlantLogo.png' );
		// Creates a new div before their first div
		$('<div class="slantDiv"></div>').insertBefore( div1 );
		var slantDiv = $(".slantDiv")[ 0 ];
		$( slantDiv ).css( { "position":"relative" } );
		console.log( slantDiv );
		// Animates our new div to slide down (looks nice)
		$( slantDiv ).prepend($('<div>', {id:'bar'} ) );
		$( slantDiv ).prepend($('<img>', {id:'SlantLogo', src:ImgURL} ) );
		

		//Style logo
		$( "#SlantLogo" ).attr( 'width', '200' );
		$( "#SlantLogo" ).attr( 'align', 'left' ); 
		$( "#SlantLogo" ).attr( 'hspace', '50' );
		$( "#SlantLogo" ).attr( 'border', '50' );
		$( "#SlantLogo" ).css( { 
			"position":"absolute",
			"top":"5%",
			"left":"3%"
		})

		//Style bias scale
		$( "#bar" ).css({
		 "width":"75%",
		 "height":"35px", 
		 "background-image":"linear-gradient(to right, rgb(11, 36, 251), rgb(252, 13, 27)", 
		 "border-radius":"7px",
		 "position":"absolute",
		 "top":"62%",
		 "left":"22%"
		})

		//$('<img src="SlantLogo.png">').appendTo( slantDiv );


		$( slantDiv ).animate( {height: '150px' } );











		// Code for the animation
		// function animateScale( bias ) {
		// 	// Area designated to the animation
		// 	var elem = document.getElementById( "myAnimation" )
		// 	var pos = 0;
		// 	var id = setInterval( frame, 10 );
		// 	function frame() {
		// 		// check if we reached the bias and end
		// 		if ( pos == bias ) {
		// 			clearInterval( id );
		// 		}
		// 		// We haven't reached the end, increment animation
		// 		else {
		// 			pos++
		// 			elem.style.top = pos + 'px';
		// 			elem.style.left = pos + 'px';
		// 		}
		// 	}
		// }



})

});
