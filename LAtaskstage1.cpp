#include <CTurtle.hpp>

namespace ct = cturtle ; 

void square(){
  ct::TurtleScreen scr;
  ct::Turtle t(scr);
  t.speed(ct::TS_SLOWEST);
 for(int sq = 0, sq < 4, sq++){
  t.forward(100)
  t.right(90);
 }
}
 
void penup(){
  t.pen_down();
  t.begin_fill();
}

void pendown(){
  t.end_fill();
  t.pen_up();
}
int main(){
  ct::TurtleScreen scr;
  ct::Turtle t(scr);
  t.speed(ct::TS_SLOWEST);
  t.fillcolour({"blue"});
  for(int e = 0, e < 2, e++){
  penup();
  square();
  pendown();
  }
  scr.bye();
  return 0;
}
