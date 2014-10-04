var mainPath;
Path.loadWave = function(pts){
	mainPath = new Path({
		segments: pts,
		strokeColor: 'black',
		fullySelected: true
	});
	mainPath.smooth();
}


var hitOptions = {
	segments: true,
	stroke: true,
	fill: true,
	tolerance: 5
};


var segment, path;
var movePath = false;
function showIntersections(path1, path2) {
	var intersections = path1.getIntersections(path2);
	for (var i = 0; i < intersections.length; i++) {
		// new Path.Circle({
		// 	center: intersections[i].point,
		// 	radius: paper.view.size.height/50,
		// 	fillColor: '#009dec'
		// })//.removeOnMove();
		var val = (intersections[i].point.y/(paper.view.size.height/1.35));
		$(".led-value")
			.css('opacity', val);
			// .html((val * 255).toFixed(0));
	}
}
function intersect(){
	tracker.selected = false;
	tracker.position.x += paper.view.size.width/100;

	showIntersections(mainPath, tracker);
	if(tracker.position.x > paper.view.size.width) {
		tracker.position.x = 0;
		// console.log('cleared interval');
		clearInterval(interval);
		interval = null;
	}
	paper.view.update();
}
var interval = null;
function onMouseDown(event) {
	if(!interval){
		// console.log('set interval');
		interval = setInterval(intersect, 30);
	}
	segment = path = null;
	var hitResult = project.hitTest(event.point, hitOptions);
	if (!hitResult) return;

	if (event.modifiers.shift) {
		if (hitResult.type == 'segment') {
			hitResult.segment.remove();
		};
		return;
	}

	if (hitResult) {
		path = hitResult.item;
		if (hitResult.type == 'segment') {
			segment = hitResult.segment;
		} else if (hitResult.type == 'stroke') {
			var location = hitResult.location;
			segment = path.insert(location.index + 1, event.point);
			path.smooth();
		}
	}
	movePath = hitResult.type == 'fill';
	if (movePath)
		project.activeLayer.addChild(hitResult.item);
}

function onMouseMove(event) {
	project.activeLayer.selected = false;
	// if (event.item)
	// 	event.item.selected = true;
}

function onMouseDrag(event) {
	if (segment) {
		segment.point += event.delta;
		path.smooth();
	} else if (path) {
		path.position += event.delta;
	}
}


var tracker;
$(function(){
	var pts = new Wave("test", Wave.trig(Wave.cos, 40, 2 * Math.PI, 10,  Math.PI/2)).dataPts(paper.view.size);
	
	Path.loadWave(pts);

	project.activeLayer.selected = false;
	tracker = new Path();
	tracker.strokeColor = 'blue';
	tracker.add(new Point(0, 0));
	tracker.add(new Point(0, paper.view.size.height));
	tracker.selected = true;

	project.activeLayer.selected = false;
	axis = new Path();
	axis.strokeColor = '#CCC';
	axis.add(new Point(0, paper.view.size.height/2.0));
	axis.add(new Point(paper.view.size.width, paper.view.size.height/2.0));
	axis.selected = false;


});





