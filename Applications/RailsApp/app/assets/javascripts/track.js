function Track(name, parent) {
	this.name = name;
	this.container = parent;
	this.DOM = null;
	this.behaviors = []; //Note: this implementation doesn't allow reordering
	this.wrappers = [];
}

Track.prototype = {
	init: function() {
		this.DOM = $('<div class="track"></div>').appendTo(this.container);
	},
	addBehavior: function(behavior) {
		this.behaviors.push(behavior);
		var wrapper = $('<div class="wrapper"></div>').appendTo(this.DOM);
		this.wrappers.push(wrapper);
		wrapper.attr('index', this.behaviors.length);
		behavior.load(wrapper);
	},
	play: function() {
		if(this.behaviors.length == 0) { return; }
		recursiveSample(this.behaviors[0]);
	},
	getData:function() {
		var data = [];
		this.behaviors.forEach(function(e, i) {
			data.push(e.wave.data);
		});
	return data;
	}
}

/**
 * Given lpIndex, samples the LP whose index is referenced at
 * canvasIndices[lpIndex].
 */
function recursiveSample(behavior) {
	behavior.sample(function() {
		if (lpIndex + 1 < this.behaviors.length) {
			recursiveSample(lpIndex + 1);
		}
	});
}