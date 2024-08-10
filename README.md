# Portal coop scrollwheel benchmark
This is a tool to get a feeling how fast you should scroll in coop. 
Because coop needs -jump action after +jump we have to scroll ~30cps rate to make each jump have less than 2 groundframes

# Usage
Open the exe and start scrolling. The line will correspond to single scroll, each scroll tick will be colored. The program will have internal 60 tickrate.
By default light blue stands for getting it right, red stands for a miss (so 2 jump inputs without tick delay happen, so the jump input gets ignored entirely), yellow stands for 2/3 groundframes and lastly orange for >3 groundframes
Generally if the line is mostly red that means that you scroll too fast, if the line mostly yellow then it is too slow. If the line has both yellows and reds that means that you are not scrolling with constant speed. The line being light blue is what should be the goal

# Config
The gui is somewhat customizable, settings can be altered in settings.cfg
