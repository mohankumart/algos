/**
 * Loop over the dom
 * read the class attributes
 * push the class names into array 
 */
function loopDom(node, classNames){
	getClassNames(node, classNames);
	node = node.firstChild;
	while(node){
		loopDom(node, classNames);
		node = node.nextSibling;
	}
}

function getClassNames(node, classNames){
	if(node.nodeName != "#text"){
		var classlist = node.getAttribute('class').split(" ");
		for(var i=0;i<classlist.length;i++){
			classNames.push(classlist[i]);
		}
	}
}

function collectNames(){
	var classNames = [];
	loopDom(document.body, classNames);
	console.log("classes---->"+classNames.join(', '));
}