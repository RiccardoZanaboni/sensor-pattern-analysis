# Motion Simulator (Movements State)

Simulates the movement of one person in the apartment and simulates the behaviour of the movmentState sensors in a selected time slice.
The program gives three output csv files. 
	"HF_input.csv" represents the measures of each sensor, used as input for the histgram filter
	"out.csv" represents the room where the person is
	"out_sensors.csv" represents the measure of the sensor of the room where the person is
These files name can be set in the configurations.json
	["info"]
    		["output_histogram_filter"]["HF_input.csv"]
    		["output_movement"]["out.csv"]
    		["output_sensors"]["out_sensors.csv"]

## Behaviour

The simulated person can chooeses to stay in a room or not thanks to the parameter "probability_of_staying"
The waiting time in a room (the time before the next movement) is drown from two uniform distributions.
One represents a short time wating the second one a long time wating. The simulation can be done with one of this wating time or both.

# Configuration information

It's necessary to define the appartment of the simulation, showing the adjacenses.
To do it use the configurations.json, using the section "room".
Use a room as key and its ajacenses rooms as values.

To deciede the slice time of simulation set the value of ["time"]["START_TIME"] and ["time"]["STOP_TIME"].

To set the uniform distributions for the behaviour of the person's movment use these parameters.
["time"]["lower_long_waiting_time"]
["time"]["upper_long_waiting_time"]
["time"]["seed_long_waiting_time"]
["time"]["lower_short_waiting_time"]
["time"]["upper_short_waiting_time"]
["time"]["seed_short_waiting_time"]

The sensors are represented by two parameters.
["time"]["sensor_sleep_time"] --> the amount of time the sensor sleeps after it reveals a movment
["time"]["sensor_sample_time"] --> sampling time of sensor

The amount of time by which the system timer is incremented(["time"]["system_time_delta"])
["time"]["epsilon"] is used to compare two timestamps

The probability of error of the sensors is represented by
["probability"]["sensor_prob_error"]

The probability of choosing to stay in a room or not is represented by
["probability"]["probability_of_staying"]

The probability of a short time permanence is represented by
["probability"]["probability_of_short_moving_behaviour"] 



