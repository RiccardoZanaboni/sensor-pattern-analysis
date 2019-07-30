# Histogram Filter Movement States

Calculates the probability in which room a person is in an apartment using the measures of some movement states sensors.

'EvaluateOutput.py' evaluates the output of the filter using an index. Index = Probability of GroundTruth/max(Probability to be in a room).
The script plots this index and save it in "output_evaluation.csv". 
(It's possible to change the name in config.json ["info"]["output_evaluation"]).


## Algorithm 

Discrete Bayes Filter

	bel_signed(xt+1)=∑xtP(xt+1∣xt)bel(xt)

	bel(xt+1)=ηP(et+1∣xt+1)bel_signed(xt+1)

# Configuration information

The program takes in input a CSV file, the name of the input file can be set in config.json (["info"]["file_name"]).
The input file is created by the simulator program to respect the requirements:

1. The first column labelled `Timestamp` is the timestamp
2. The other columns labelled as the rooms of the appartment are considered for the output sensor of each room. (The room columns must have the same order of the 'state_domain')

A CSV file which represents the real movments of the person during the simualation (the ground truth), is also required.
The name of this file can be set in config.json (["info"]["ground_truth_file_name"]).
It must have two columns, the first 'Timestamp'(the time of the system) the second 'Room' (where the person goes) and it is created by the simulator program.

The output is a CSV file with a column for the 'Timestamp', a column for the output sensor of each room and a column for the probability of each room. 
The name of the file can be set in config.json (["info"]["output_file_name"])

The program uses the file 'config.json' to set a list of parameter:
* ["info"]["state_domain"] the letters that represent the rooms (the possible states of the person)
* ["probability"]["bel_t0"] the initial state of the probability to be in a room. (the room is selected by the index, in the order of the state_domain)

A dictionary of the probability to be in a room at the timestamp t1 knowing to be in a determinated room at the time t0.
The key represents the room at the time t0. The value is an array of probability to go in a room at t1. 
The room where to go is identified by the position in the array (it MUST BE in the same order of 'state_doamin').
Example:
* ["probability"]["probA"] Probability to go in each room at t1 being in room 'A' at t0
* ["probability"]["probB"] Probability to go in each room at t1 being in room 'B' at t0
* ["probability"]["probL"] Probability to go in each room at t1 being in room 'L' at t0
   .... for each room in the apartment.

A dictionary of the probability to be in each room after the measurement of a sensor in a determinated room.
The key represents the room where the measure happens. The value is the key of another dictionary and represent the possible value of the measures(0/1).
The value of this dictionary is an array of probability to be in a room with that sensor output. The position in the array represents which room is considered.(same order 'state_domain')
* [sensor_error_probability"] ["sA"] [1]
* [sensor_error_probability"] ["sA"] [0]
* [sensor_error_probability"] ["sb"] [1]
   .... for each room in the apartment.


