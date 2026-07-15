# Firmware

This folder contains the embedded firmware responsible for controlling the Smart AI-Assisted IV Access System.

The firmware running on the ESP32 acquires data from imaging and physiological sensors, monitors battery status, and communicates with the AI software running on the host computer.

---

## Responsibilities

- Initialize all sensors
- Acquire physiological measurements
- Capture infrared image frames
- Monitor battery voltage
- Transmit data to the software application

---

## Firmware Modules

- main.ino
- camera_interface.cpp
- max30102_driver.cpp
- battery_monitor.cpp
- serial_comm.cpp

---

## Firmware Workflow

Power On

↓

Initialize ESP32

↓

Initialize Sensors

↓

Acquire Sensor Data

↓

Transmit Data

↓

Repeat
