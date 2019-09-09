# create_csv

It contains a group of scripts to analyze the data coming from the gateway.
They also provide to create the input files for the finite state machine, the simulator and the histogram filter.


## read_ms
It reads the original data  from the gateway and create a csv file with the MovementState measures of a single room only.

### Configuration
All the following settings can  be configured in 'config.json' file.

The names of the input files can be set using the ["input"]["file"] section (each input file  represents a room).
For each one of the input files, an output file is created . Its name can be set in the ["output_read_ms"] section,
using the ["file"] list. The index of the outfile is matched with those of the input files.

### Getting Started
```
~$ python3 read_ms.py name_of_configuration_file.json
``` 

## create_hlt
 It creates a csv file from the original data  from the gateway.The measure of Humidity, Luminescence and 
 Temperature of a single room are saved in these files.
  
### Configuration
All the following settings can  be configured in 'config.json' file.

The names of the input files can be set using the ["input"]["file"] section (each input file  represents a room).
For each one of the input files, an output file is created . Its name can be set in the ["output_create_hlt"] section,
using the ["file"] list. The index of the outfile is matched with those of the input files.


### Getting Started
```
~$ python3 create_hlt.py name_of_configuration_file.json

```

## unify_ms
It unifies the measures of all MovementState files, which are created by read_ms, in a chronological order.

### Configuration
All the following settings can  be configured in 'config.json' file.

The names of the input files can be set using the ["input_unify_ms"]["file"] section (each input file  represents a room).
For each one of the input files, an output file is created . Its name can be set in the ["output_unify_ms"] section,
using the ["file_out_name"] filed. 

 ### Getting Started
```
~$ python3 unify_ms.py name_of_configuration_file.json

```
