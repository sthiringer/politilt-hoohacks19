console.log( "Chrome extension go" );

chrome.runtime.onMessage.addListener( function gotMessage( message, sender, sendResponse ) {
	//Send HTTP request with this stuff to the server
		var raw_HTML = document.documentElement.outerHTML;
		console.log(raw_HTML);





		// Re-format the website
		// BAD SOLUTION
		//document.body.style.marginTop = "75px";

		//var div1 = document.querySelector( $div:first );








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