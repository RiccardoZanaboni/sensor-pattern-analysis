#!/bin/bash 
MAINPATH=/Users/fabiorossanigo/PycharmProjects/sensor-pattern-analysis
CONFPATH=/Users/fabiorossanigo/PycharmProjects/sensor-pattern-analysis/base_configurations1
MAIN_EXE_MS=motion-simulator/TestMotionSimulator.py
MAIN_EXE_HF=HistogramFilter/Main.py
MAIN_EXE_EV=HistogramFilter/EvaluateOutput.py
MAIN_EXE_HIST=Histogram.py


echo "Simulation n.1 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config18.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config18.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config18.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config18 DONE | tee -a log_configurations.txt



echo "Simulation n.2 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config18.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config18.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config18.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config18 DONE | tee -a log_configurations.txt



echo "Simulation n.3 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config22.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config22.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config22.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config22 DONE | tee -a log_configurations.txt



echo "Simulation n.4 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config22.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config22.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config22.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config22 DONE | tee -a log_configurations.txt



echo "Simulation n.5 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config34.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config34.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config34.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config34 DONE | tee -a log_configurations.txt



echo "Simulation n.6 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config34.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config34.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config34.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config34 DONE | tee -a log_configurations.txt



echo "Simulation n.7 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config14.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config14.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config14.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config14 DONE | tee -a log_configurations.txt



echo "Simulation n.8 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config14.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config14.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config14.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config14 DONE | tee -a log_configurations.txt



echo "Simulation n.9 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config43.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config43.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config43.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config43 DONE | tee -a log_configurations.txt



echo "Simulation n.10 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config43.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config43.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config43.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config43 DONE | tee -a log_configurations.txt



echo "Simulation n.11 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config6.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config6.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config6.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config6 DONE | tee -a log_configurations.txt



echo "Simulation n.12 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config6.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config6.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config6.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config6 DONE | tee -a log_configurations.txt



echo "Simulation n.13 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config38.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config38.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config38.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config38 DONE | tee -a log_configurations.txt



echo "Simulation n.14 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config38.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config38.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config38.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config38 DONE | tee -a log_configurations.txt



echo "Simulation n.15 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config39.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config39.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config39.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config39 DONE | tee -a log_configurations.txt



echo "Simulation n.16 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config39.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config39.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config39.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config39 DONE | tee -a log_configurations.txt



echo "Simulation n.17 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config7.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config7.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config7.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config7 DONE | tee -a log_configurations.txt



echo "Simulation n.18 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config7.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config7.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config7.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config7 DONE | tee -a log_configurations.txt



echo "Simulation n.19 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config42.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config42.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config42.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config42 DONE | tee -a log_configurations.txt



echo "Simulation n.20 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config42.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config42.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config42.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config42 DONE | tee -a log_configurations.txt



echo "Simulation n.21 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config15.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config15.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config15.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config15 DONE | tee -a log_configurations.txt



echo "Simulation n.22 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config15.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config15.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config15.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config15 DONE | tee -a log_configurations.txt



echo "Simulation n.23 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config35.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config35.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config35.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config35 DONE | tee -a log_configurations.txt



echo "Simulation n.24 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config35.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config35.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config35.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config35 DONE | tee -a log_configurations.txt



echo "Simulation n.25 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config23.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config23.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config23.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config23 DONE | tee -a log_configurations.txt



echo "Simulation n.26 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config23.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config23.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config23.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config23 DONE | tee -a log_configurations.txt



echo "Simulation n.27 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config19.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config19.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config19.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config19 DONE | tee -a log_configurations.txt



echo "Simulation n.28 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config19.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config19.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config19.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config19 DONE | tee -a log_configurations.txt



echo "Simulation n.29 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config12.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config12.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config12.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config12 DONE | tee -a log_configurations.txt



echo "Simulation n.30 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config12.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config12.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config12.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config12 DONE | tee -a log_configurations.txt



echo "Simulation n.31 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config45.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config45.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config45.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config45 DONE | tee -a log_configurations.txt



echo "Simulation n.32 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config45.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config45.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config45.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config45 DONE | tee -a log_configurations.txt



echo "Simulation n.33 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config28.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config28.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config28.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config28 DONE | tee -a log_configurations.txt



echo "Simulation n.34 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config28.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config28.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config28.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config28 DONE | tee -a log_configurations.txt



echo "Simulation n.35 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config49.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config49.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config49.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config49 DONE | tee -a log_configurations.txt



echo "Simulation n.36 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config49.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config49.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config49.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config49 DONE | tee -a log_configurations.txt



echo "Simulation n.37 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config24.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config24.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config24.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config24 DONE | tee -a log_configurations.txt



echo "Simulation n.38 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config24.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config24.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config24.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config24 DONE | tee -a log_configurations.txt



echo "Simulation n.39 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config32.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config32.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config32.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config32 DONE | tee -a log_configurations.txt



echo "Simulation n.40 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config32.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config32.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config32.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config32 DONE | tee -a log_configurations.txt



echo "Simulation n.41 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config33.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config33.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config33.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config33 DONE | tee -a log_configurations.txt



echo "Simulation n.42 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config33.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config33.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config33.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config33 DONE | tee -a log_configurations.txt



echo "Simulation n.43 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config25.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config25.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config25.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config25 DONE | tee -a log_configurations.txt



echo "Simulation n.44 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config25.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config25.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config25.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config25 DONE | tee -a log_configurations.txt



echo "Simulation n.45 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config48.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config48.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config48.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config48 DONE | tee -a log_configurations.txt



echo "Simulation n.46 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config48.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config48.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config48.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config48 DONE | tee -a log_configurations.txt



echo "Simulation n.47 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config29.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config29.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config29.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config29 DONE | tee -a log_configurations.txt



echo "Simulation n.48 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config29.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config29.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config29.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config29 DONE | tee -a log_configurations.txt



echo "Simulation n.49 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config1.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config1.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config1.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config1 DONE | tee -a log_configurations.txt



echo "Simulation n.50 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config1.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config1.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config1.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config1 DONE | tee -a log_configurations.txt



echo "Simulation n.51 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config44.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config44.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config44.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config44 DONE | tee -a log_configurations.txt



echo "Simulation n.52 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config44.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config44.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config44.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config44 DONE | tee -a log_configurations.txt



echo "Simulation n.53 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config13.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config13.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config13.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config13 DONE | tee -a log_configurations.txt



echo "Simulation n.54 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config13.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config13.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config13.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config13 DONE | tee -a log_configurations.txt



echo "Simulation n.55 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config2.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config2.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config2.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config2 DONE | tee -a log_configurations.txt



echo "Simulation n.56 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config2.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config2.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config2.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config2 DONE | tee -a log_configurations.txt



echo "Simulation n.57 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config47.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config47.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config47.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config47 DONE | tee -a log_configurations.txt



echo "Simulation n.58 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config47.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config47.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config47.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config47 DONE | tee -a log_configurations.txt



echo "Simulation n.59 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config10.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config10.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config10.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config10 DONE | tee -a log_configurations.txt



echo "Simulation n.60 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config10.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config10.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config10.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config10 DONE | tee -a log_configurations.txt



echo "Simulation n.61 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config30.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config30.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config30.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config30 DONE | tee -a log_configurations.txt



echo "Simulation n.62 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config30.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config30.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config30.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config30 DONE | tee -a log_configurations.txt



echo "Simulation n.63 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config26.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config26.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config26.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config26 DONE | tee -a log_configurations.txt



echo "Simulation n.64 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config26.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config26.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config26.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config26 DONE | tee -a log_configurations.txt



echo "Simulation n.65 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config27.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config27.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config27.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config27 DONE | tee -a log_configurations.txt



echo "Simulation n.66 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config27.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config27.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config27.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config27 DONE | tee -a log_configurations.txt



echo "Simulation n.67 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config31.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config31.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config31.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config31 DONE | tee -a log_configurations.txt



echo "Simulation n.68 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config31.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config31.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config31.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config31 DONE | tee -a log_configurations.txt



echo "Simulation n.69 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config11.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config11.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config11.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config11 DONE | tee -a log_configurations.txt



echo "Simulation n.70 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config11.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config11.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config11.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config11 DONE | tee -a log_configurations.txt



echo "Simulation n.71 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config46.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config46.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config46.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config46 DONE | tee -a log_configurations.txt



echo "Simulation n.72 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config46.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config46.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config46.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config46 DONE | tee -a log_configurations.txt



echo "Simulation n.73 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config3.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config3.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config3.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config3 DONE | tee -a log_configurations.txt



echo "Simulation n.74 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config3.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config3.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config3.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config3 DONE | tee -a log_configurations.txt



echo "Simulation n.75 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config50.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config50.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config50.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config50 DONE | tee -a log_configurations.txt



echo "Simulation n.76 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config50.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config50.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config50.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config50 DONE | tee -a log_configurations.txt



echo "Simulation n.77 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config36.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config36.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config36.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config36 DONE | tee -a log_configurations.txt



echo "Simulation n.78 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config36.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config36.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config36.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config36 DONE | tee -a log_configurations.txt



echo "Simulation n.79 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config20.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config20.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config20.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config20 DONE | tee -a log_configurations.txt



echo "Simulation n.80 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config20.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config20.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config20.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config20 DONE | tee -a log_configurations.txt



echo "Simulation n.81 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config8.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config8.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config8.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config8 DONE | tee -a log_configurations.txt



echo "Simulation n.82 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config8.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config8.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config8.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config8 DONE | tee -a log_configurations.txt



echo "Simulation n.83 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config4.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config4.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config4.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config4 DONE | tee -a log_configurations.txt



echo "Simulation n.84 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config4.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config4.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config4.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config4 DONE | tee -a log_configurations.txt



echo "Simulation n.85 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config41.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config41.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config41.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config41 DONE | tee -a log_configurations.txt



echo "Simulation n.86 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config41.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config41.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config41.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config41 DONE | tee -a log_configurations.txt



echo "Simulation n.87 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config16.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config16.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config16.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config16 DONE | tee -a log_configurations.txt



echo "Simulation n.88 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config16.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config16.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config16.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config16 DONE | tee -a log_configurations.txt



echo "Simulation n.89 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config17.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config17.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config17.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config17 DONE | tee -a log_configurations.txt



echo "Simulation n.90 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config17.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config17.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config17.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config17 DONE | tee -a log_configurations.txt



echo "Simulation n.91 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config40.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config40.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config40.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config40 DONE | tee -a log_configurations.txt



echo "Simulation n.92 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config40.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config40.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config40.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config40 DONE | tee -a log_configurations.txt



echo "Simulation n.93 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config5.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config5.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config5.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config5 DONE | tee -a log_configurations.txt



echo "Simulation n.94 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config5.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config5.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config5.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config5 DONE | tee -a log_configurations.txt



echo "Simulation n.95 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config9.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config9.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config9.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config9 DONE | tee -a log_configurations.txt



echo "Simulation n.96 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config9.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config9.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config9.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config9 DONE | tee -a log_configurations.txt



echo "Simulation n.97 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config21.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config21.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config21.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config21 DONE | tee -a log_configurations.txt



echo "Simulation n.98 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config21.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config21.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config21.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config21 DONE | tee -a log_configurations.txt



echo "Simulation n.99 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config37.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config37.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config37.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config37 DONE | tee -a log_configurations.txt



echo "Simulation n.100 out of 100"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config37.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config37.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config37.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config37 DONE | tee -a log_configurations.txt


        
echo "Creating simulation total Histogram..."
python3 $MAINPATH/$MAIN_EXE_HIST $CONFPATH
