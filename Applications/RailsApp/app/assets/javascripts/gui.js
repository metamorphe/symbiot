function gui() {

  var that = this;

  this.datGUI = new dat.GUI();
  
  this.env = env;
  this.obj = this.env.addLed(); //current LED pulled from env

  this.ledCanvas;
  this.measurerCanvas;
  this.waveform;

  var MEASURER_COLOR = 'rgba(46, 204, 113, 1.0)';
  var WAVEFORM_COLOR = 'rgba(230, 126, 34, 1.0)';
  var WAVEFORM_WIDTH = 300;
  var WAVEFORM_HEIGHT = 150;

  initializeDatGui(that.obj);

  ////////////////////////////////////////////////////////

  this.setLed = function(object) {
    setObj(object);
    setCanvases(object.ledNumber);
    document.getElementById("led_number_button").innerHTML
        = object.ledNumber;
  }

  function setObj(object) {
    if (! (object instanceof LED)) {
      throw new TypeError("Cannot set gui to control non-LED object.");
    }
    that.obj = object;
    that.datGUI.destroy();
    that.datGUI = new dat.GUI();
    initializeDatGui(object);
  }

  function setCanvases(ledNumber) {
    that.ledCanvas = document.getElementById('led').getContext('2d');
    that.measurerCanvas = document.getElementById('measurer').getContext('2d');
    that.waveform = d3.select('#waveform');
  }


  function initializeDatGui(object) {
    that.datGUI.add(that.env, 'addLed')
        .name('New LED');
    that.datGUI.add(object, 'time')
      .min(0)
      .max(100)
      .step(1)
      .onChange(function(newValue) {
        that.obj.time = newValue;
        that.obj.updateFrame();
        }
    );
    that.datGUI.add(object, 'amplitude')
        .min(0.1)
        .max(5)
        .listen();
    that.datGUI.add(object, 'frequency')
        .min(1)
        .max(10)
        .step(1)
        .listen();
    that.datGUI.addColor(object, 'color').onChange(function(newValue) {
      render(that.obj);
    });
    that.datGUI.add(object, 'blink')
        .name('blink');
    that.datGUI.add(object, 'cosine')
        .name('cosine');
    that.datGUI.add(object, 'play')
        .name('play');
    that.datGUI.add(object, 'printState')
        .name('print states');
    that.datGUI.add(object, 'paramsToCSV')
        .name('export');

    that.datGUI.remember(object);
  }

  this.initializeCanvases = function(object) {
    initializeLED(object);
    initializeMeasurer(object);
    initializeWaveform(object);
  }

  function initializeLED(object) {
    var c = d3.select('#main_frame')
      .append('canvas')
        .attr('id', 'led');
    var ctx = document
      .getElementById('led')
      .getContext('2d');
    ctx.fillStyle = object.color;
    ctx.beginPath();
    ctx.arc(95,50,40,0,2*Math.PI);
    ctx.fill();
  }

  function initializeMeasurer(object) {
    var d = d3.select('#main_frame')
      .append('canvas')
        .attr('id', 'measurer');
    var dtx = document
      .getElementById('measurer')
      .getContext('2d');
    dtx.fillStyle = MEASURER_COLOR;
    dtx.fillRect(0, 0, (object.width * DIM_SCALAR),
                  (object.height * DIM_SCALAR));
  }

  function initializeWaveform(object) {
    var width = WAVEFORM_WIDTH;
    var height = WAVEFORM_HEIGHT;

    var e = d3.select('#main_frame')
      .append('svg')
        .attr('id', 'waveform')
        .attr('width', width)
        .attr('height', height);

    that.waveform = e;
    
    that.updateWaveform();

    d3.select('#main_frame').append('br');
  }

  this.updateWaveform = function() {
    var width = WAVEFORM_WIDTH;
    var height = WAVEFORM_HEIGHT;

    that.waveform.select('g').remove();
    
    var y = d3.scale.linear()
    .domain([0, d3.max(that.obj.states)])
    .range([0, height]);

    var x = d3.scale.linear()
        .domain([0, that.obj.states.length])
        .range([0, width]);

    var chart = that.waveform
        .attr("width", width)
        .attr("height", height);

    var g = chart.append("svg:g")
        .attr("transform", "translate(0, " + height + ")");

    var line = d3.svg.line()
        .x(function(d, i) { return x(i); })
        .y(function(d) { return -1 * y(d); });

    g.append("svg:path")
        .attr("class", "line")
        .attr("d", line(that.obj.states));
  }

}