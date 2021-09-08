



function MovePage(arg) {
	var webloc='http://192.168.0.236:80/'
	var webArr= ['', 'projects', 'contact']
	console.log(arg)
	
		
	if (arg >= -1){
		var path = webloc + webArr[webIndex + arg];
		console.log(path)
	}
	else{
		arg = (arg == 'index') ? '' : arg
	var path = webloc + arg;
	}
	document.location = path;
}
function hideArrows(){
		var navLeft = document.getElementById("LeftArrow")
		var navRight = document.getElementById("RightArrow")
	if (webIndex <1){
		if (!navLeft.classList.contains('hide'))
			toggle("LeftArrow", 'hide')
		if (navRight.classList.contains('hide'))
			toggle("RightArrow", 'hide')
	} else if (webIndex > 1){
	if (navLeft.classList.contains('hide'))
			toggle("LeftArrow", 'hide')
		if (!navRight.classList.contains('hide'))
			toggle("RightArrow", 'hide')
	} else{
		navLeft.classList.remove('hide')
		navRight.classList.remove('hide')
	}
	
	
}
function btnClick(id){
	var target = document.getElementById(id)
	target.click()
}
function btnMouseOver(id){
	document.getElementById(id).style.backgroundImage="url(/../../static/sources/img/button-pressed.png)"
}
function btnMouseOff(id){
	document.getElementById(id).style.backgroundImage="url(/../../static/sources/img/button.png)"
}
function toggle(id, arg){
	var target = document.getElementById(id)
	if (target.classList.contains(arg)){
		target.classList.remove(arg);
		} else {
			target.classList.add(arg);
		}
}


function httpGetAsync(URL, callback){
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function(){
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
			callback(xmlHttp.responseText);
			
		}
	}
	xmlHttp.open('GET', URL, true);
	xmlHttp.send(null);
}
function InsertImages(el, image_list) {
	
}

function callback(data){
	var hi = "ol"
}
function stopanimationR(){
	var arrows = ["LeftArrow","RightArrow" ]
	toggle(arrows[0], 'leftA')
	toggle(arrows[1], 'rightA')
	
}
function startanimationR(){
	var arrows = ["LeftArrow","RightArrow" ]
	toggle(arrows[0], 'leftA')
	toggle(arrows[1], 'rightA')
}