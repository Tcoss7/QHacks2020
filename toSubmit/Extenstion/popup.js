'use strict';
//me
//var webdriver = require('selenium-webdriver'),
//	SeleniumServer = require('selenium-webdriver/remote').SeleniumServer;

//const {Builder, By, Key, Until} = require('selenium-webdriver');

var url;
var text, color;
var ethicScore;

chrome.tabs.query({active: true, lastFocusedWindow: true}, function (tabs) {

	url = tabs[0].url;

	
	//console.log(getEthicsScore());


	var ethicScore = Math.floor(Math.random() * Math.floor(15));//=kyles code;

	if(ethicScore<0){
		color = 'white';
		text = 'no company found';
	} else{
		text = "This comapany scores " + ethicScore + "/15 for Ethics";
		if(ethicScore>10){
			color = 'lightgreen';
		}else if(ethicScore>5){
			color = 'lightyellow';
		} else {
			color = 'red';
		}
	}
	document.getElementById('kyleair').innerHTML = url;

	document.getElementById('ethicstext').innerHTML = text;
	document.body.style.backgroundColor = color;

});
/*
(async function example() {
	let driver = await new Builder().forBrowser('chrome').build();
	try {
		await driver.get(url);
	} finally {
		await driver.quit();
	}
})();
/*
async function getEthicsScore(){
	try{ 
		var driver = new webdriver.Builder()
        .forBrowser('chrome')
        .withCapabilities(webdriver.Capabilities.chrome())
		.build();
		
		await driver.get(url);

		await driver.getTitle().then(function(title){
			console.log("the title is" + title)
		});

		driver.quit();

	}
	catch(err){
		console.error('fuck you ', err.stack, '\n');
		driver.quit();
	}
}
*/
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