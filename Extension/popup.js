'use strict';

//me
//let checkEthics = document.getElementById('checkEthics');//button

var url;
var text, color;
var ethicScore;

chrome.tabs.query({active: true, lastFocusedWindow: true}, function (tabs) {


	url = tabs[0].url;

		
	$.post("receiver", url, function(){	});


	console.log(url);

	var ethicScore = 11;//=kyles code;

	if(ethicScore<0){
		color = 'white';
		text = 'no company found';
	} else{
		text = "This comapany scores " + ethicScore + "/15 for Ethics";
		if(ethicScore>10){
			color = 'lightgreen';
		}else if(ethicScore>5){
			color = 'lightyellow';
		} else if(ethicScore>=0){
			color = 'lightred';
		}
	}
	   		
	document.getElementById('ethicstext').innerHTML = text;
	document.body.style.backgroundColor = color;

});

	/*
checkEthics.onclick = function(element) {

}


*/

/////// not me 
/*
let changeColor = document.getElementById('changeColor');

chrome.storage.sync.get('color', function(data) {
  changeColor.style.backgroundColor = data.color;
  changeColor.setAttribute('value', data.color);
});

changeColor.onclick = function(element) {
  let color = element.target.value;
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.executeScript(
        tabs[0].id,
        {code: 'document.body.style.backgroundColor = "' + color + '";'});
  });
};
*/