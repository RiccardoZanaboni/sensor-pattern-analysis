# Graphic Animation
It contains a script to show the graphic animation of two algorithms implemented in this repository:
* Histogram Filter 
* Simulator

## Main
It shows the animation of the output of the histogram filter and simulator.
Thanks to a parameter from command line you can execute one of the two animation.
The histogram filter animation shows the output of the filter and the position of the person inside a map (a graph
defined by the room adjacencies) of the apartment at every timestamp.
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

In "prob_text_name" section you can set the position of the name of the rooms on the figure

In "prob_text_area" section you can chose the position of the probability of the rooms

In "adj" section the adjacencies of the apartment are defined.
Chose the center that must be linked by the edges

The dictionary "evaluation_thresholds" defines the color for each range of probability 


### Getting Started
To execute the animation of the histogram filter:
```
~$ python3 Main.py -f name_of_configuration_file.json 

```
To execute the animation of the simulator 
```
~$ python3 Main.py -f name_of_configuration_file.json to execute the animation of histogram filter

```

