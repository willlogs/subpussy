import * as p5 from 'p5';

new p5((p: p5) => {
  p.setup = () => {
    p.createCanvas(400, 400);
  };

  p.draw = () => {
    p.background(220);
    p.ellipse(p.width / 2, p.height / 2, 50, 50);
  };
});