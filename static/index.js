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


// Event linstner for enter, which we will send a request for
window.addEventListener('keypress', (e) => {
	var key = e.which || e.keyCode;
	if (key === 13) { // 13 is enter
		let input = document.getElementById('main');
		makeRequest('POST', '/general', input.value)
		.then((res) => {
			res = clean(res);
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

function clean(str) {
	str = str.substring(1,str.length-2);
	return str;
}

async function outputString(string) {
	document.getElementById('mainText').innerText = '';
	
}

// Rending my basic information
ReactDOM.render(
	<span>
		<br />
		<br />
		<h1 id="mainText">Hello, Mike</h1>
		<br />
		<input type="text" id="main"></input>
	</span>,
	document.getElementById('root')
);