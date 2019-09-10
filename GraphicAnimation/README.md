# Graphic Animation
It contains two scripts to show the graphic animation of the three algorithms implemented in this repository:
* Histogram Filter 
* Simulator
* FSM 
## Main
It shows the animation of the output of the histogram filter and simulator.
Thanks to a parameter from command line you can execute one of the two animation.
The histogram filter animation shows the output of the filter and the position of the person inside a map
of the apartment at every timestamp.
The simulator animation  shows the output of the sensor and the position of the person inside a map
of the apartment at every timestamp.

### Configuration
All these settings can be found in config.json file.

In the "info" section :
* "input_file" is an input file for "Main.py" 
* "evaluation_file" is an input file for "Main.py"
* "ground_truth_column_name" the name of column which represents the room where the person is 
* "time_speed" is the millisecond value of one timestamp for the animation 
* "x_lim" and "y_lim" are the dimension of axes
* "figure_size" is the dimension of the figure
* "person_radius" is the dimension of the circle which represents the person
* "default_room_color" is the default color of the room 

"probability_position" is a dictionary where the key are the name of the columns of the room probability in the input file
and the values are the position of the room 

"apartment" is a dictionary where the key are the name of the room in the input file
and the values are the positions of the room 

"room_dictionary" is a dictionary where the keys are the column names of the room probability and the values the room names

In the "text_area" section :
* "position" is the coordinate of the text
* "fonr_size" is the dimension of the text

In the "image" section :
* "position" is the position of the image
* "file" the image selected

In the "ev_level" section :
* "position" is the position of the text which indicates the evaluation of the filter,
* "font_size" is the dimension of the text

### Getting Started
To execute the animation of the histogram filter:
```
~$ python3 Main.py -f name_of_configuration_file.json 

```
To execute the animation of the simulator 
```
~$ python3 Main.py -f name_of_configuration_file.json to execute the animation of histogram filter

```



## Animation_FSM
It shows the animation of the Final State Machine used for the hlt sensors.
It used three figure which represents the state of the FSM.

### Configuration
All these settings can be found in config.json file.

In the "info" section :
* "input_file" is the input file for "Animate_FSM" script
* "time_speed" is the value of one timestamp (10 min) for the animation 
* "x_lim" and "y_lim" are the dimension of axes
* "figure_size" is the dimension of the figure
* "status_radius" is the dimension of the circle which represents the state of the FSM

"state_position" is a dictionary where the values are the states of the fsm and the values their position

"state_color" is a dictionary where the keys are the state of the fsm and the keys the text color 

"index" is a dictionary to match the index of state column in input file with the state name

### Getting Started

To execute the animation of the FSM 
```
~$ python3 Animation_FSM.py name_of_configuration_file.json 

```


