# hlt-final-state-machine

It contains a group of scripts to analyze the workflow of the hlt(humidity,
luminescence and temperature) devices.

## FSM_statistics
It calculates statistics about the sampling time of the hlt devices of
the sensors and it saves them in a '.csv' file . It takes in input '.csv' files,
 which are created by 'create_hlt_file.py' (It can be found in the create_csv directory in
this reposistory).

### Configuration
All these settings can be found in config.json file.

In the "info" section :
* "directory_input_FSM_statistics" is the directory of the input files
* "input_FSM_statistics" is a list with the names of the input files
* "directory_output_FSM_statistics" is the directory where the out file is created
* "output_FSM_statistics" is the out file name

'WARNING' : if an existing file is selected as out file, it will be overwritten.

### Getting Started
```
~$ python3 FSM_statistics.py name_of_configuration_file.json

```

## FSM_state
It is a final state machine of the hlt device of one sensor.
It is made up of four states :
* 'WORKING' : the sensor is properly working
* 'WARNING_NOT_SAMPLE' : it warns that there are some missing samples for the sensor
* 'WARNING_EQUAL_MEASURES': it warns that there is a series of equal measures
* 'NOT_WORKING' : the sensor is not properly working

It takes in input a '.csv' file created by 'create_hlt_file.py' (It can be found in the create_csv directory
in this reposistory).

### Configuration
All these setting can  be found in config.json file.

In the "info" section :
* "path_directory_input_FSM" is the directory of the input file
* "file_input_FSM" is the name of the input file
* "path_directory_output_FSM" is the directory where the out file is created
* "file_output_FSM" is the name of the out file

'WARNING' : if an existing file is selected as out file, it will be overwritten.

In the "FSM_info" section :
* "SAMPLE_TIME" is the sample time of the hlt device
* "MAX_EQUALS_SAMPLES" is the threshold which determines the state changing from 'WARNING_EQUAL_MEASURES'
  to 'NOT_WORKING'.
* "number_missing_sample" is the threshold which determined the state changing from 'WARNING_NOT_SAMPLE'
  to 'NOT_WORKING'.
* "state_values" is a dictionary in which each state name is matched to a value
  (You could change the values but you must not change the key names).
* "sampling_mean" is the mean of the sample time, you can take it from the output of the FSM_statistics

### Getting Started
```

~$ python3 FSM_state.py name_of_configuration_file.json

```  

## FSM_parallel
It creates a csv file which represents the four states of the FSM in every Timestamp. It set for each state the
value 1 if the FSM is in that state and 0 if it is not.
Moreover the program tsl can show parallel plots of the states condition of FSM thanks to this output csv.

It takes in input the output file of FSM_state.py

### Configuration
All these setting can  be found in config.json file.

In the "info" section :
* "path_directory_input_parallel" is the directory of the input file
* "file_input_parallel" is the name of the input file
* "path_directory_output_parallel" is the directory where the out file is created
* "file_output_parallel" is the name of the out file

### Getting Started
```

~$ python3 FSM_parallel.py name_of_configuration_file.json

```

## FSM_final_binary
It creates a csv file which represents the output of the FSM in a binary format.
 * 1 if the FSM is in WORKING state or in a WARNING states
 * 0 if FSM is in NOT_WORKING state

It takes in input the output file of FSM_state.py

### Configuration
All these setting can  be found in config.json file.

In the "info" section :
* "path_directory_input_final_binary" is the directory of the input file
* "file_input_final_binary" is the name of the input file
* "path_directory_output_final_binary" is the directory where the out file is created
* "file_output_final_binary" is the name of the out file

### Getting Started
```

~$ python3 FSM_final_binary.py name_of_configuration_file.json

```
