# Histogram Filter Movment States

Calculate a probability in which room a person is in an apartment using the measures of some movment states sensors.

'EvaluateOutput.py' evaluates the output of the filter using an index. Index = Probability of GroundTruth/max(Probability to be in a room).
The script plot this index and save it inthe file "output_evaluation.csv". 
(It's possible to change the name in the config.json ["info"]["output_evaluation"]).


## Algorithm 

Discrete Bayes Filter

	bel_signed(xt+1)=∑xtP(xt+1∣xt)bel(xt)

	bel(xt+1)=ηP(et+1∣xt+1)bel_signed(xt+1)

# Configuration information

The program takes in input a CSV file, the name of the input file can be setted in config.json (["info"]["file_name"]).
The input file is created by the simulator program to rispect the requiremnts:

1. The first column labelled `Timestamp` is considered for the timestamp
2. The other columns labelled as the rooms in the appartment are considered for the otput sensor of each room.(The room columns must have the same order of the 'state_domain')

It is also necessary a CSV file which represents the real movments of the person during the simualation(the ground truth).
The name of the file can be setted in config.json (["info"]["ground_truth_file_name"]).
It must have two columns, the first 'Timestamp'(the time of system) the second 'Room'(where the persone goes) and it is created by the simulator program.

The output is a  CSV file whith a column for the 'Timestamp' , a column for the output sensor for each room and a column for the probability of each room. 
The name of the file can be setted in config.json (["info"]["output_file_name"])

The program uses a file 'config.json' to set a list of parameter:
* ["info"]["state_domain"] here are setted the lecters which represent the rooms(the possible states of the person)
* ["probability"]["bel_t0"] the initialization of the array which represents the probability to be in a room.(the room is selected by the index, in the order of the state_domain)

A dictionary of the probability to be in a room at the timestamp t1 knowing to be in a determinated room at the time t0.
The key represents the room at the time t0. The value is an array of probability to go in the room at t1. 
The room where to go is identiried by the position in the arrey(NEEDED the same order of 'state_doamin').
* ["probability"]["probA"] Probability to go in each room at t1 being in room 'A' at t0
* ["probability"]["probB"] Probability to go in each room at t1 being in room 'B' at t0
* ["probability"]["probL"] Probability to go in each room at t1 being in room 'L' at t0
   .... for each room in the apartment.
A dictionary of the probability to be in each room after the measure of a sensor in a determinated room.
The key represents the room where the measure happens. The values are the key of another dictionary and represent the possible value of the measures(0/1).
The value of this dctionary is an array of probability to be in a room with that sesnor output. The position in the array represnts which room is considered.(same order 'state_domain')
* [sensor_error_probability"] ["sA"] [1]
* [sensor_error_probability"] ["sA"] [0]
* [sensor_error_probability"] ["sb"] [1]
   .... for each room in the apartment.


