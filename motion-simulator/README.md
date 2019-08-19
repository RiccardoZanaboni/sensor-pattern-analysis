# Motion Simulator (Movements State)

Simulates the movement of one person in the apartment and simulates the behaviour of the movementState sensors in a selected time slice.
The program gives four output csv files. 
	"HF_input.csv" represents the measures of each sensor, used as input for the histgram filter
	"out.csv" represents the room where the person is
	"out_sensors.csv" represents the measure of the sensor of the room where the person is
	"simulation_info.txt" which contains the info about the simulation, the name of this file is created using python's
	    time module so that it is not overwritten in future simulations.
	    
These files name can be set in configurations.json
["info"]
  * ["output_histogram_filter"]["HF_input.csv"]
  * ["output_movement"]["out.csv"]
  * ["output_sensors"]["out_sensors.csv"]

## Behaviour

The simulated person can choose to stay in a room or not thanks to the parameter "probability_of_staying"
The waiting time in a room (the time before the next movement) is drawn from two uniform distributions.
One represents a short time waiting the second a long time waiting. The simulation can be done with one of this waiting time or both.

# Configuration information
All these settings can be found in configurations.json file.

It's necessary to define the apartment of the simulation, showing the adjacenses.
To do it use configurations.json, using the section "room".
Use a room as key and its adjacenses rooms as values.

To decide the slice time of the simulation, set the value of ["time"]["START_TIME"] and ["time"]["STOP_TIME"].

To set the uniform distributions for the behaviour of the person's movement use these parameters.
* ["time"]["lower_long_waiting_time"]
* ["time"]["upper_long_waiting_time"]
* ["time"]["seed_long_waiting_time"]
* ["time"]["lower_short_waiting_time"]
* ["time"]["upper_short_waiting_time"]
* ["time"]["seed_short_waiting_time"]

The sensors are represented by two parameters.
* ["time"]["sensor_sleep_time"] --> the amount of time the sensor sleeps after it reveals a movment
* ["time"]["sensor_sample_time"] --> sampling time of sensor

The amount of time by which the system timer is incremented can be configured by (["time"]["system_time_delta"])
* ["time"]["epsilon"] is used to compare two timestamps

The probability of error of the sensors is represented by
* ["probability"]["sensor_prob_error"]

The probability of choosing to stay in a room or not is represented by
* ["probability"]["probability_of_staying"]

The probability of a short time permanence is represented by
* ["probability"]["probability_of_short_moving_behaviour"]

## Debug mode

In the configurations.json file there is the possibility to run the simulation in debug mode.
To do so , in the "info" section of the configurations.json file set the value of "debug_mode" to "on". If this 
parameter is set to "off" the seeds of the simulation (the one of the long waiting time model and the one of the short 
waiting time model) are set using python's time module. Instead, in debug mode the seeds are set using the parameter in 
section "time" of  configurations.json file :
* "seed_short_waiting_time"
* "seed_long_waiting_time"
  

# Output Information

The simulator creates a file for each simulation, in which the info about the simulation are saved.
These files are saved in the simulation-info directory, but they are ignored by git.
These files includes both the seed used by the long waiting time model and the one used by the short 
waiting time model.



