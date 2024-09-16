#include <CTurtle.hpp>

namespace ct = cturtle ; 

void square(){
  ct::TurtleScreen scr;
  ct::Turtle t(scr);
  t.speed(ct::TS_SLOWEST);
  t.pen_down();
  t.begin_fill();
 for(int sq = 0, sq < 4, sq++){
  t.forward(100)
  t.right(90);
 }
 t.end_fill();
  t.pen_up();

}

void spiral(){
 t.pen_down();
 t.pencolor("black");
 int width = 1
 int dist = 10
 for(i = 0, i < 50, i++){
   t.forward(dist);
   t.pensize(width);
   t.left(90)
   dist += 10;
   width ++;
 }

}

int main(){
  ct::TurtleScreen scr;
  ct::Turtle t(scr);
  t.speed(ct::TS_SLOWEST);
  t.fillcolour({"blue"});
  for(int e = 0, e < 2, e++){
  square();
  t.forward(200)
  }
  scr.bye();
  return 0;
}
