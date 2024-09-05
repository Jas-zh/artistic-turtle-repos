# artistic-turtle-repos
S3
# DEATH TO PYTHON!!
## THERE'S TURTLE GRAPHICS FOR C
Ever feel like Python is too annoying with it's dynamic style?
Ever want to be more restrictive and have more organized code?
Ever wish that people would stop shilling Python for anything besides statistical use?
WELL HERE'S A SOLUTION!!
There is a C library for turtle graphics, with all the features python has[citation needed]
Just create a new .c file in your IDE of choice: VScode, Notepad++, Eclipse, Code::blocks etc. and type: 
> #include "turtle.h"
> int main{
>  turtle_init(300, 300);          // initialize the image to be 600x600

    turtle_forward(50);
    turtle_turn_left(90);
    turtle_forward(50);
    turtle_draw_turtle();

    turtle_save_bmp("output.bmp");  // save the turtle drawing

    return EXIT_SUCCESS;
>
> }
INSTANT success, organized, beautiful code.
# EVEN WORKS ON ARCH LINUX!!

source:
https://w3.cs.jmu.edu/lam2mo/cs240_2015_08/turtle.html
