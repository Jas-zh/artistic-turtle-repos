#include "turtle.h"

int main{
    turtle.init(300, 300);
 //basic customization of the pen:
 void turtle_set_pen_color(0,255,0);
 void turtle_set_fill_color(0,102,204);

 //Drawing part
 turtle_set_heading(90);
 turtle_forward(100);

 //export   
    turtle_draw_turtle();
    turtle_save_bpm("itevenexportsasa.bpm");

    return EXIT_SUCCESS;
}

/*
Python is a mess, so I switched to C:
A rant by Zhang Jason

This is in the source code because I want to include :)

Python is such a disappointment of a language, I just don't like it, well maybe because Im used to the 
beautiful structured languages like C, C#, Rust etc. I mean they are annoying sometimes with the limitatons
but overall it makes the code look organized and clean. There's a meme in the programming world, where if you make 
an application, people will say "write it in Rust" well, I haven't tried rust(this is a lie). Not much at least
*Arch Linux Customization flashbacks*
it's because RUst is just so superior in every way. Its a low level language, which, 
*googles How high level languages run*
Ohhhhhh, ok so C and C++ are both high and low level languages, and python is only a high level language,
oh right yea, that's the benefit of C and C++ it's a mix of both high and low level langauges, which means it's both
abstracted while also being in a way that a computer can directly read. Which is different from Python which needs a translator of 
some sorts to help the computer understand what the heck you are writing. 
A lot of people say "An idiot admires complexity, while a Genius admires simplicity" well I feel like, C and C++ are simplistic
(I AM NOT A GENIUS), not as in they are not hard to learn, they are complex in that department, but an experienced programmer
can understand C/C++ resonably quickly as they are structured in a very specific way. Maybe I'm the exception here, since I've been
using C#, C and C++ since 4th grade(in primary school), so I've grown acustomed to the order of these languages.
Another reason I don't like Python, is that it's been milked so much, advertising wise. Everyone says it's an easy to learn
language, and while that is true, I feel like every STEM activity has less focus on the really technical aspects of computers
and more about "WOW WE USE PYTHON BECAUSE ITS POPULAR". It doesn't mean that popular = bad, its just that
Python, as a high level language, doesn't teach you anything about how a computer works. AS someone who likes getting into the 
technical aspects of a computer, I've been drawn away from "normie" stuff and more into very advanced stuff. Like
Linux(Arch linux), which has taught me a lot about how a computer works, from its file system, kernal level operations. How the terminal works
the basics of BASH and shell scripts, how to install drivers etc. and in just 2 months I've gone from someone
who was dependent on Windows, to someone who can basically do everything from a terminal with next to graphics.

Idk what I'm going with this rant, but I like C/C++ so I'm gonna use it. But since the school wants us to use Python so bad, I'll convert it later
*/