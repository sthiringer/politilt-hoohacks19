/*
Background script for slant browser extension
*/

chrome.browserAction.onClicked.addListener( buttonClicked );

function buttonClicked( tab ) {
	//console.log( tab );
	let msg = {
		txt: "hello"
	}
	chrome.tabs.sendMessage( tab.id, msg );

}