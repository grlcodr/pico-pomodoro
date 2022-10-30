
# Pico Pomodoro

Pomodoro /pɒməˈdɔːrəʊ/ 

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It uses a kitchen timer to break work into intervals, typically 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato, after the tomato-shaped kitchen timer Cirillo used as a university student.

I love the pomodoro technique - the only issue? Relying on an internet connection for pomodoro sites, or having to set timers on a mobile phone which pulls focus from the task at hand. 

_"Just use a kitchen timer!"_ I hear you cry, but where's the fun in that?

Enter Pico Pomodoro, a physical pomodoro timer created with a Raspberry Pico H, a Pico Explorer Base and MicroPython.

## Features

- Customizable images and text for each interval 'start' screen
- Adjustable timers for each interval
  
## Development (WIP)

This project is a work in progress - Python and MicroPython are fairly new to me, and I hope to clean up this repo as I learn more! 

The Pico Pomodoro will eventually work in the following way

1. Basic loading screen to advise user to press 'A' to start
2. Button 'A' starts a 25 minute **focus** timer 
3. Button 'B' starts a 5 minute **short break** timer
4. Button 'C' starts a 15 minute **long break** timer 
5. Button 'D' resets any stored timer information

As I develop this project, I plan to add more functionality to make it more fun, smarter and easier to use.

TODO:

- Add logic to track button presses and prevent wrong timer from being selected
- Add RGB light
- Add speaker/sound functionality 
- Killswitch/reset button 

## Acknowledgements

 - [Larry Bank's JPEGDEC](https://github.com/bitbank2/JPEGDEC)
  