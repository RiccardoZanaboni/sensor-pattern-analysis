<h2>The Project</h2>

This project has been created to simulate and analyze movement of one person or more people in a domotic apartment equipped with motion sensors in order to create a system that learns habits and tries to understand if something is wrong in the behaviour of people and in this case call assistance; the system is designed especially for older people that live alone.

<h2>The Environment</h2>

The apartment has a motion sensor in each room. The output of a sensor is either '0' or '1'; each second every sensor checks for movement and when it captures it the value change from 0 to 1 and then stays 1 for 3 minutes. After this time the sensor checks if there is still someone in the room: if yes, it remains 1 for another 3 minutes otherwise it returns 0. All output of sensors are sent to a gateway.

<h2>How it works</h2>

The system takes as input a configuration file in `json` format. In this configuration file are specified all the characteristics wanted for the simulation; for example the topology matrix of the apartment, the number of people in the apartment, the probabilities of changing the room and others.


https://user-images.githubusercontent.com/48360582/167180303-7000f95a-ad10-4fbf-a8d7-7ae9fe12639e.mov


Once all is set the simulation starts and it gives as output a csv file in which each row corresponds to a second and each column represents the values of a sensor(0-off or 1-on).

This csv file is then used for the **Histogram Filter**: it calculates the probability in which room a person is in an apartment using the measures of some movement states sensors and then the prediction of the probabilities is compared to the ground truth.

Algorithm used :

>Discrete Bayes Filter

	bel_signed(xt+1)=∑xtP(xt+1∣xt)bel(xt)

	bel(xt+1)=ηP(et+1∣xt+1)bel_signed(xt+1)

<h2>Focus of my work</h2>

<h3>Graphical interface</h3>

In this project the focus of my work was initially the creation of a **graphical interface** representing the simulated person moving in the house.

The apartment is modeled using a graph that highlights the connections between the different rooms, represented through nodes. A stylized man is placed to the left of the room where the subject really is in order to immediately represent his position. Similarly, a light bulb placed to the right of a node symbolizes the switching on of the sensor in that room. Each node is characterized by the probability coming out of the filter that the subject is in the corresponding room. The different forecasts are depicted on a white to red color scale where white represents the least probable forecast and red the most probable one. All this information is summarized in text form at the bottom of the interface.

https://user-images.githubusercontent.com/48378307/167291441-7161581c-df6a-4254-b721-1ba61be87cae.mp4


<h3>Unknown Topology</h3>

After dealing with the management of the interface, I dedicated myself to evaluating the Histogram Filter if the **topology was unknown**.
The topology matrix in the json file is initially approximated as a totally interconnected apartment, as can be seen in the figure, in which the probabilities are all equal.

![image](https://user-images.githubusercontent.com/48378307/167291875-0d4e54ca-9cbb-4f48-b3bd-7c85ccb58d79.png)

Although the filter differs greatly from the correct configuration, it is **able to obtain a reconstruction of the topology** of the house in question through the path given by the highest probability out of the filter moment by moment.
To improve this task an initial time window is exploited in order to obtain a reconstruction of the topology as correct as possible,then the topology is updated at each instant based on the reconstructed adjacencies until the end of the simulation. This is called **Dynamic Filter**.

Once the execution of the dynamic filter is finished, the last topology matrix obtained dynamically is displayed through a pair of heatmaps.  
In the first, the real existing adjacencies are shown in green, introducing a color scale from the lightest green for the lowest probabilities to the darkest green for the highest ones.Similarly, non-existent adjacencies are shown in red, introducing a color scale from the lightest red for the lowest probabilities to the darkest red for the highest ones.    
In the second, instead, the goodness of reconstruction of the topology of the apartment is displayed through a red scale, in which the darker color (burgundy) represents two possibilities:
* the filter has correctly recognized an existing adjacency with a high probability;
* the filter has correctly recognized a non-existent adjacency with a low probability.
   
The lighter color (white) represents the two complementary possibilities, that is:
* the filter has mistakenly recognized a non-existent adjacency with a high probability;
* the filter has mistakenly recognized an existing adjacency with a low probability.


![Immagine1](https://user-images.githubusercontent.com/48378307/167292845-5ec464da-507a-4a20-8362-64db2515471f.png)



