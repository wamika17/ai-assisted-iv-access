# Firmware Connections

## ESP32 Pin Allocation

| Peripheral | Interface |
|------------|-----------|
| Infrared Camera | SPI / Parallel Camera Interface |
| MAX30102 | I²C |
| OLED Display | I²C |
| Battery Monitor | ADC |

---

## Communication

Sensor Data

↓

ESP32 Firmware

↓

Serial Communication

↓

Python Dashboard

↓

AI Analysis
