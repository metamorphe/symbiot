function Environment() {

  var that = this;

  this.ledList = new Array();
  this.ledCount = 0;
  this.currLed;
  this.currLedNum = 0;

  this.addLed = function() {
    console.log("Gonna make new LED YEEEE");
    this.ledList.push(new LED(this.ledCount));
    this.currLed = this.ledList[this.ledCount];
    this.ledCount++;
    return this.currLed;
  }
  
  this.prevLed = function() {
    switchLed(-1)
  }

  this.nextLed = function() {
    switchLed(1);
  }

  function switchLed(shift) {
    env.currLedNum = (env.currLedNum + shift) % env.ledCount;
    currLed = env.ledList[env.currLedNum];
    console.log("switchLED is setting LED to: " + env.currLedNum);
    gui.setLed(currLed);
    render();
    renderWaveform();
  }

}