document.getElementById("analyze").onclick = function() {myFunction()};

function myFunction() {




	console.log( "poopy 3" );

	let params = {
		active: true,
		currentWindow: true
	}

	chrome.tabs.query( params, gotTabs );

	function gotTabs( tabs ) {

		
		let msg = {
			txt: "hello"
		}
		console.log(tabs[0]);
		chrome.tabs.sendMessage( tabs[0].id, msg );
	}



	
}


