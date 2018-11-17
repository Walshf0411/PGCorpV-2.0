const fill = document.querySelector('.fill');
const droppers = document.querySelectorAll('.dropper'); 
const nav_contains = document.querySelectorAll('.dropper2');

// fill listeners 
fill.addEventListener('dragstart',dragStart);
fill.addEventListener('dragend',dragEnd);
//loop  for dropper2 
for (const dropper of nav_contains){
	dropper.addEventListener('dragover',dragOver2);
	dropper.addEventListener('dragenter',dragEnter2);
	dropper.addEventListener('dragleave',dragLeave2);
	dropper.addEventListener('drop',dragDrop2);
}
// loop through the droppers 
for (const dropper of droppers){
	dropper.addEventListener('dragover',dragOver);
	dropper.addEventListener('dragenter',dragEnter);
	dropper.addEventListener('dragleave',dragLeave);
	dropper.addEventListener('drop',dragDrop);
}

// drag functions 

function dragStart(){
	//console.log ("start");
	this.className +=' hold';
	//for removing the whole object use 
	// this.className = 'invisible';
	//setTimeout(()=> this.className = 'invisible',0); 
}

function dragEnd(){
	//console.log("end");
	this.className ='fill';
}

function dragOver(e){
	e.preventDefault();
	//console.log('over');
}

function dragEnter(e){
	e.preventDefault();
	//console.log('enter');
	this.className +=' hovered';
}

function dragLeave(){
	//console.log('leave');
	this.className ='dropper';
}

function dragDrop(){
	//console.log('drop');
	this.className ='dropper';
	// you need to add the entire dom element fill into this function to drop the image in selected box
	this.append(fill.cloneNode(true));
}

function dragOver2(e){
	e.preventDefault();
	//document.getElementById('nav_dropper').style.display='block';
	console.log('over');
}

function dragEnter2(e){
	e.preventDefault();
	console.log('enter');
	this.className +=' hovered';
}

function dragLeave2(){
	console.log('leave');
	this.className ='dropper2';
}

function dragDrop2(){
	console.log('drop');
	// you need to add the entire dom element fill into this function to drop the image in selected box
	this.append(fill.cloneNode(true));
}