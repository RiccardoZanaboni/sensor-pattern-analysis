<h2>The Project</h2>

This project has been created to simulate and analyze movement of one persone or more people in a domotic apartment equipped with motion sensor in order to create a system that learns habits and try to understand if something is wrong in the behaviour of people and in this case call assitance; the system is designed especially for old people taht live alone.

<h2>The Environment</h2>

The apartment has a motion sensor in each room. The output of a sensor is either '0' or '1'; each second every sensor check for movment and when it captures it the value change from 0 to 1 and then stays 1 for 3 minutes. After this time the sesnor check if there is still someone in the room: if yes it remains 1 for other 3 minutes otherwise it returns 0. All the output of sensors are sent to a gateway.

<h2>How it works</h2>

The system takes as input a configuration file in `json` format. In this configuration file are specified all the caratheristics wanted for the simulation; for example the topology of the apartment, the number of person in the apartment, the probabilites of changing room and others.

![Schermata 2022-05-06 alle 19 12 01](https://user-images.githubusercontent.com/48360582/167180291-ef552498-b955-402a-a0c2-263f7e203dc0.png)


https://user-images.githubusercontent.com/48360582/167180303-7000f95a-ad10-4fbf-a8d7-7ae9fe12639e.mov

