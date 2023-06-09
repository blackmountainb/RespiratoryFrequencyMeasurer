# RespiratoryFrequencyMeasurer
This repository contains instructions and the code for a 3D printed mask to measure respiratory frequency rate, using an Arduino and a MCP9808 temperature sensor.

This work was developed as a project for final evaluation, under Instrumentation and Control Techniques course for Biomedical Engineering Master Degree at University of Coimbra.

Authors: Beatriz Negromonte (negromontebs@gmail.com) and Disa Palma (disaaqp@gmail.com)

## Goal:
Create a low cost respiratory frequency rate measurer with 3D print mask, Arduino and a temperature sensor. 

## Material:
- Arduino MKR1000
- MCP9808 Sensor
- Breadboard
- 4 connectors
- 3D printed mask + adaptor

## How to:
1 - Download and print one of the mask body files, from: https://www.thingiverse.com/thing:4225667

For our tests, we printed a Mask Body Wide M size as we were not sure of how big the masks would be, but just turned out a good size.

2 - Download and print the Adaptor.stl file above - this one we designed considering the Mask Body Wide M size measures

It should be like this - you can attach to either nose or mouth level, but they will have different results for breath measurement, which is the expected behavior and the code is adapted for it as well but you will need to declare where is the source of breath: 
<div>
  <img src="https://github.com/blackmountainb/RespiratoryFrequencyMeasurer/blob/main/Images/suporte.png" alt="Adaptor image" width="300"/>&nbsp;
</div>

3 - Connect Arduino as Image below: 

<div>
  <img src="https://github.com/blackmountainb/RespiratoryFrequencyMeasurer/blob/main/Images/montagem.jpeg" alt="Adaptor image" width="300"/>&nbsp;
</div>

On our work, we used a solder and a plug adaptor to maintain the sensor attached to the mask adaptor, as seen below:

<div>
  <img src="https://github.com/blackmountainb/RespiratoryFrequencyMeasurer/blob/main/Images/mask.jpeg" alt="Adaptor image" width="300"/>&nbsp;
</div>

4 - Download and setup ArduSpreadSheet, from https://circuitjournal.com/arduino-serial-to-spreadsheet - this is a library that will generate the csv file with the information for Temperature detection from the sensor

5.1 - Execute Arduino code and collect csv file

5.2 - Chose csv collected on code export_csv_code.py

OR 

6. - Generate and plot data in real time with real_time.py code
