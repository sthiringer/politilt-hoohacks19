console.log( "Chrome extension go" );



chrome.runtime.onMessage.addListener( gotMessage );

function gotMessage( message, sender, sendResponse ) {
	if ( message.txt == "hello" ) {
		let paragraphs = document.getElementsByTagName( 'p' );
		for ( elt of paragraphs ) {
			elt.innerHTML = message.txt;
		}
	}
}