let timeout = null;
let prevCommands = [];
let commandIndex = 0;

// Function that is used to make all of the ajax http requests to the server
function makeRequest(reqType, endpoint, data) {
	return new Promise((resolve, reject) => {
		const httpRequest = new XMLHttpRequest();
		if (!httpRequest) {
			alert('Cannot create http request');
			return false;
		}
		httpRequest.onreadystatechange = () => { 
			if (httpRequest.readyState === XMLHttpRequest.DONE) {
				if (httpRequest.status === 200) {
					resolve(httpRequest.response);
				} else {
					reject(httpRequest.response);
				}
				
			}
		}
		httpRequest.open(reqType, endpoint);
		httpRequest.setRequestHeader('Content-Type', 'application/json');
		if (data) {
			httpRequest.send(data);
		} else {
			httpRequest.send();
		}
	});
}

function startPoll() {
	// This kicks off our polling
	timeout = setTimeout(poll, 100);
}

// Event linstner for enter, which we will send a request for
window.addEventListener('keypress', (e) => {
	var key = e.which || e.keyCode;
	if (key === 13) { // 13 is enter
		let input = document.getElementById('main');
		makeRequest('POST', '/general', input.value)
		.then(() => {
			if (prevCommands.length === 100) {
				prevCommands = prevCommands.slice(1);
			}
			prevCommands.push(input.value);
			commandIndex = prevCommands.length;
			input.value = '';
		}).catch((err) => {
			let res = 'There was an error.';
			document.getElementById('mainText').textContent = '';
			for(var i = 0; i<res.length; i++) {
				(function(index) {
					setTimeout(function() {
						document.getElementById('mainText').textContent+=res.charAt(index); 
					}, 50*i);
				})(i);
			}
		});
	}
});

window.addEventListener('keydown', (e) => {
	var key = e.which || e.keyCode;
	let input = document.getElementById('main');
	if (key === 40) {
		if (commandIndex < prevCommands.length) {
			commandIndex++;
			input.value = prevCommands[commandIndex] || '';
		}
	} else if (key === 38) {
		if (commandIndex > 0) {
			commandIndex--;
			input.value = prevCommands[commandIndex] || '';
		}
	}
});

function poll() {
	makeRequest('PUT', '/general')
	.then((res) => {
		res = clean(res);
		if(res != '') {
			document.getElementById('mainText').textContent = '';
			for(var i = 0; i<res.length; i++) {
				(function(index) {
					setTimeout(function() {
						document.getElementById('mainText').textContent+=res.charAt(index); 
					}, 50*i);
				})(i);
			}
		}
		setTimeout(poll, 100);
	});
}

function clean(str) {
	str = str.substring(1,str.length-2);
	return str;
}

async function printString(string) {
	document.getElementById('mainText').innerText = '';
}

// Rending my basic information
ReactDOM.render(
	<span>
		{startPoll()}
		<br />
		<br />
		<h1 id="mainText">Hello, Mike</h1>
		<br />
		<input type="text" id="main"></input>
	</span>,
	document.getElementById('root')
);