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
	this.repeatDom = null;
	this.stretchDom = null;
	this.preview;
	this.init();
}

WaveView.prototype = {
	init: function() {
		//TODO: fix hardcoding?
		var scope = this;
		this.dom = $('#current-wave');
		this.fieldDom = $('.field');
		this.previewDom = $('.preview');
		this.repeatDom = $('.repeat');
		this.stretchDom = $('.stretch');
		this.repeatDom.change(function() {
			var num = parseInt(scope.repeatDom.val());
			scope.currentBehavior.wave.setRepeat(num);
			scope.refresh();
		});
		this.stretchDom.change(function() {
			var num = parseInt(scope.repeatDom.val());
			scope.currentBehavior.wave.setStretch(num);
			scope.refresh();
		});
		this.repeatDom.hide();
		this.stretchDom.hide();
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

		this.repeatDom.show();
		this.stretchDom.show();
	},
	changeRepresentation: function(repName) {
		this.currentBehavior.preview.switchRep(repName);
	},
	refresh: function() {
		console.log('Todo: refresh wave');
	}
}