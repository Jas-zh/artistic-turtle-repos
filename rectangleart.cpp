#include <CTurtle.hpp>

namespace ct = cturtle ; 

int main(){
  ct::TurtleScreen scr;
  ct::Turtle t(scr);
  t.speed(ct::TS_SLOWEST);
  t.fillcolour({"blue"});
  for(int e = 0, e < 2, e++){
  t.pen_down();
  t.begin_fill();
  for(int i = 0, i < 4, i++){
    t.forward(100);
    t.right(90);
  }
  t.end_fill();
  t.pen_up();
  }
  scr.bye();
  return 0;
}