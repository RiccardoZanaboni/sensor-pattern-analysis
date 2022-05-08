<h2>The Project</h2>

This project has been created to simulate and analyze movement of one person or more people in a domotic apartment equipped with motion sensor in order to create a system that learns habits and try to understand if something is wrong in the behaviour of people and in this case call assistance; the system is designed especially for older people that live alone.

<h2>The Environment</h2>

The apartment has a motion sensor in each room. The output of a sensor is either '0' or '1'; each second every sensor checks for movement and when it captures it the value change from 0 to 1 and then stays 1 for 3 minutes. After this time the sensor check if there is still someone in the room: if yes, it remains 1 for another 3 minutes otherwise it returns 0. All the output of sensors are sent to a gateway.

<h2>How it works</h2>

The system takes as input a configuration file in `json` format. In this configuration file are specified all the characteristics wanted for the simulation; for example the topology of the apartment, the number of people in the apartment, the probabilities of changing rooms and others.

![Schermata 2022-05-06 alle 19 12 01](https://user-images.githubusercontent.com/48360582/167180291-ef552498-b955-402a-a0c2-263f7e203dc0.png)


https://user-images.githubusercontent.com/48360582/167180303-7000f95a-ad10-4fbf-a8d7-7ae9fe12639e.mov


Once all is set the simulation starts and it gives as output a csv file in which each row corresponds to a second and each column represents the values of a sensor(0-off or 1-on).

This csv file is the used for the 'histogram filter': it calculates the probability in which room a person is in an apartment using the measures of some movement states sensors and then the prediction of the probabilities is compared to the ground truth.

Algorithm used :

>Discrete Bayes Filter

	bel_signed(xt+1)=∑xtP(xt+1∣xt)bel(xt)

	bel(xt+1)=ηP(et+1∣xt+1)bel_signed(xt+1)

<h2>Focus of my work</h2>

In this project the focus of my work was the creation 

