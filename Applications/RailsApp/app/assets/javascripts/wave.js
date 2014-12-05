/* Class: Wave
 * Description: Internal representation of a waveform
 * Dependencies: numeric.js, GUI: paper.js
 */

function Wave(name, data, isSmooth){
	this.name = name;
	this.data = data;
	this.isSmooth = isSmooth;
	this.strech = 1;
	this.repeat = 1;
}

const DEFAULT_LEN = 300;
const DEFAULT_STRETCH = 1;
const DEFAULT_REPEAT = 1;

var newArr;
var xAxis;

Wave.prototype = {
	//return LED states
	getData: function(n){
		// TODO: Return a n-array representation of wave from this.data 
		if (n == undefined) { return this.data; }
		xAxis = numeric.linspace(0, this.data.length - 1);
		return numeric.spline(xAxis, this.data)
					.at(numeric.linspace(0, this.data.length - 1, n));
	},
	setData: function(newData) {
		this.data = newData;
	},
	getStretch: function() {
		return this.stretch;
	},
	setStretch: function(stretch) {
		this.stretch = stretch;
		// do stretch operations
	},
	clearStretch: function() {
		this.setStretch(DEFAULT_STRETCH);
	},
	getRepeat: function() {
		return this.repeat;
	},
	setRepeat: function(repeat) {
		this.repeat = repeat;
	},
	clearRepeat: function() {
		this.setRepeat(DEFAULT_REPEAT);
	},
	reset: function() {
		this.clearStretch();
		this.clearRepeat();
	},

	/* Begin math transforms */
	add: function(w, modify){
		// TODO: Add to waves together, return a new Wave if modify is false
		newArr = numeric.addVV(this.getData(DEFAULT_LEN),
									w.getData(DEFAULT_LEN));
		if (modify) {
			this.setData(newArr);
		} else {
			return newArr;
		}
	},
	sub: function(w, modify){
		// TODO: Sub waves, return a new Wave if modify is false
		newArr = numeric.subVV(this.getData(DEFAULT_LEN),
									w.getData(DEFAULT_LEN));
		if (modify) {
			this.setData(newArr);
		} else {
			return newArr;
		}
	},
	mul: function(s,modify){
		// TODO: Multiply scalar, return a new Wave if modify is false
		newArr = numeric.mulVV(this.getData(DEFAULT_LEN).
									w.getData(DEFAULT_LEN));
		if (modify) {
			this.setData(newArr);
		} else {
			return newArr;
		}
	},
	div: function(s, modify){
		return this.mul(1/s, modify);
	},
	wSum: function(arrW, weightW, modify){ //TODO: make static
		//TODO: Return weightedSum, return a new Wave if modify is false
	},
	clone: function(){
		// TODO: duplicate wave
		return new Wave(this.name, this.data, this.isSmooth);
	},
	guiSVG: function(editable){
		// TODO: return a DOM representation of this wave as an SVG
	},
	dataAdd: function(v){
		this.data.push(v);
		return this;
	}, 
	dataPts: function(scale){
		var t = numeric.linspace(0, 1, this.data.length);
		return $.map(this.data, function(el, i){
			return new paper.Point(t[i] * scale.width, el * (scale.height *0.45));
		});
	}
}


// For t = 1 ..  
// Return an array of F(t) = Af(Bt – C) + D
// F: a trig function (e.g., Math.cos)
// A: amplitude is A
// B: period is (2π)/|B|
// C: phase shift is C/B
// D: vertical shift is D

Wave.cos = numeric.cos;
Wave.sin = numeric.sin;

Wave.trig = function(func, samples, n, amp, period, phaseShift, vertShift){

	if(typeof n === "undefined") n = 2 * Math.PI;
	if(typeof amp === "undefined") amp = 1;
	if(typeof period === "undefined") period = 2 * Math.PI;
	if(typeof phaseShift === "undefined") phaseShift = 0;
	if(typeof vertShift === "undefined") vertShift = 0;
	vertShift *= -1;
	
	var A = amp;
	var B = Math.abs((2 * Math.PI) / period);
	var C = phaseShift * B;
	var D = vertShift;
	
	var t = numeric.linspace(1, n, samples);
	var Bt = numeric.mul(B, t);
	var Bt_C = numeric.sub(Bt, C);
	var fBt_C = numeric.cos(Bt_C);

	var AfBt_C = numeric.mul(A, fBt_C);
	var AfBt_CD = numeric.add(D, fBt_C);
	return AfBt_CD;
}


// Wave.square = function(-)
// 

