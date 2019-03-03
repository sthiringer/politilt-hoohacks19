console.log( "Chrome extension go" );

chrome.runtime.onMessage.addListener( function gotMessage( message, sender, sendResponse ) {
	//Send HTTP request with this stuff to the server
		var raw_HTML = document.documentElement.outerHTML;
		console.log(raw_HTML);
})