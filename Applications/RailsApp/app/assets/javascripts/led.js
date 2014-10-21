var intervalID;
var STATES_LENGTH = 100;

function LED(ledNumber) {
  this.play = this._play;
  this.blink = this._blink;
  this.cosine = this._cosine;
  this.printState = this._print;
  this.updateFrame = this._update;
  this.paramsToCSV = this._csv;
  this._init(ledNumber);
}

LED.prototype = {
  _init: function(ledNumber){
    this.states = new Array(STATES_LENGTH);
    
    for (var i = 0; i < STATES_LENGTH; i++)
      this.states[i] = 1;

    /* Time represents a millisecond (or 10ms); index for states */
    this.time = 0;
    this.ledNumber = ledNumber;

    this.height = 1;
    this.width = 1;
    this.color = 'rgba(231, 76, 60, 1.0)';

    this.amplitude = 1;
    this.frequency = 1;
  }, 
  _cosine : function() {
    var frequency = this.frequency;
    for (var i = 0; i < STATES_LENGTH; i++) {
      this.states[i] = Math.cos(frequency 
        * 2 * Math.PI * (i / STATES_LENGTH));
      this.states[i] += 1 // bias waveform above 0 brightness
    }
  }, 
  _blink : function() {
    var frequency = this.frequency;
    var runLength = STATES_LENGTH / (frequency * 2) >> 0;
    var isDark = true;
    for (var i = 0; i < STATES_LENGTH; i++) {
      if (i % runLength == 0) {
        isDark = !isDark
      }
      this.states[i] = (isDark) ? 0 : 1;
    }
  },
  _play : function() {
    renderWaveform();
    var that = this;
    intervalID = setInterval(function() {
      LED.frameDraw(that, that.time)
      that.time++;
    }, 10);
    this.time = 0;
  },
  _print: function() {
    console.log("State values for: led" + this.ledNumber);
    console.log(this.states);
  }, 
  _update: function() {
    if (this.time < STATES_LENGTH) {
      var curr = this.states[this.time];
      this.width = curr;
      this.color = 'rgba(231, 76, 60, ' + curr + ')';
      render();
    }
  }, 
  _csv: function(){
    var csvContent = "data:text/csv;charset=utf-8,";
    var header = "Index, Value, Color";
    var currLine;
    for (var i = 0; i < STATES_LENGTH; i++) {
      currLine = i + "," + this.states[i] * this.amplitude + "," + "NYI\n";
      csvContent += currLine;
    }
    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "waveform_data.csv");
    link.click();
  }
}


LED.frameDraw = function(stateObj, arrayIndex) {
  if (arrayIndex >= STATES_LENGTH) {
    clearTimeout(intervalID);
  } else {
    var curr = stateObj.states[arrayIndex];
    stateObj.width = curr;
    stateObj.color = 'rgba(231, 76, 60, ' + curr + ')';
    render();
  }
}