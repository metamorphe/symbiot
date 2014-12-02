/*
 * Dependencies: 
 *  - requires page with instance 'api' of api.js,
 *  - requires _wave_view.html.erb
 *  - requires behavior.js
 */

function WaveView() {
	this.currentBehavior = null;
	this.dom = null;
	this.fieldDom = null;
	this.previewDom = null;
	this.init();
}

WaveView.prototype = {
	init: function() {
		this.dom = $('#current-wave');
		this.fieldDom = $('.field');
		this.previewDom = $('.preview');
	},
	loadBehavior: function(behaviorId) {
		var behavior = api.get_async('/api/behaviors/' + behaviorId);
		behavior.wave = new Wave(behavior.name, behavior.states, null);
		behavior.preview = new Preview(this.previewDom);
		behavior.__proto__ = Behavior.prototype;
		console.log(behavior);
		behavior.load(this.fieldDom);
		behavior.preview.switchRep("light"); // default to LED Rep, TODO: change later
		this.currentBehavior = behavior;
	},
	changeRepresentation: function(repName) {
		this.currentBehavior.preview.switchRep(repName);
	}
}