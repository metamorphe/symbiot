function main() {
  var obj = new LED();
  var gui = new dat.GUI();

  gui.add(obj, 'height').min(20).max(300)
    .onChange(function(newValue) {
      render();
    });
  gui.add(obj, 'width').min(20).max(300)
    .onChange(function(newValue) {
      render();
    });
  gui.add(obj, 'amplitude').min(0.1).max(5);
  gui.add(obj, 'frequency').min(0.1).max(5).step(1);
  gui.addColor(obj, 'color').onChange(function(newValue) {
    render();
  });
  gui.add(obj, 'blink').name('blink');
  gui.add(obj, 'cosine').name('cosine');
  gui.add(obj, 'play').name('play');

  gui.remember(obj);

  var c = document.getElementById('frame');
  var ctx = c.getContext('2d');

  ctx.fillStyle = obj.color;
  ctx.fillRect(0, 0, obj.width, obj.height);

  function render() {
    ctx.clearRect(0, 0, 500, 500);
    ctx.fillStyle = obj.color;
    ctx.fillRect(0, 0, obj.width, obj.height);
  };

  var fps = 15;
  function render2() {
    setTimeout(function() {
    if (obj.states.length == 0) {
      clearInterval();
    }
    requestAnimationFrame(drawLen);
    ctx.clearRect(0, 0, 500, 500);
    ctx.fillStyle = obj.color;
    ctx.fillRect(0, 0, obj.width, obj.height);
    }, 1000 / fps);
  };
};