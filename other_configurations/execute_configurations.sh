#!/bin/bash 
MAINPATH=/Users/fabiorossanigo/PycharmProjects/sensor-pattern-analysis
CONFPATH=/Users/fabiorossanigo/PycharmProjects/sensor-pattern-analysis/other_configurations
MAIN_EXE_MS=motion-simulator/TestMotionSimulator.py
MAIN_EXE_HF=HistogramFilter/Main.py
MAIN_EXE_EV=HistogramFilter/EvaluateOutput.py
MAIN_EXE_HIST=Histogram.py


echo "Simulation n.1 out of 1"
python3 $MAINPATH/$MAIN_EXE_MS configurations_MS/config1.json
python3 $MAINPATH/$MAIN_EXE_HF configurations_HF/config1.json
python3 $MAINPATH/$MAIN_EXE_EV configurations_HF/config1.json
echo "[$(date +"%Y-%m-%d %T.%3N")]" config1 DONE | tee -a log_configurations.txt


        
echo "Creating simulation total Histogram"
python3 $MAINPATH/$MAIN_EXE_HIST $CONFPATH
