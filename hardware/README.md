# Hardware

This folder contains the embedded hardware architecture of the Smart AI-Assisted IV Access System.

The hardware combines infrared imaging, physiological sensing, and embedded processing to assist clinicians in locating suitable veins for intravenous (IV) cannulation.

---

## Hardware Architecture

The prototype integrates multiple sensing modalities into a portable handheld device capable of collecting physiological and imaging data in real time.

The embedded hardware communicates with the software application where AI algorithms analyze patient-specific information and provide clinical decision support.

---

## Hardware Components

| Component | Purpose |
|-----------|----------|
| ESP32 | Main embedded controller |
| Infrared Camera | Vein visualization |
| MAX30102 | Pulse and oxygen sensing |
| OLED Display | Local status display |
| Rechargeable Battery | Portable operation |
| TP4056 Charging Module | Battery charging |
| 3D Printed Enclosure | Compact portable housing |

---

## Hardware Workflow

Patient

↓

Infrared Imaging

↓

Physiological Sensing

↓

ESP32 Processing

↓

Serial Communication

↓

AI Software

↓

Patient Dashboard

---

## Folder Structure

```text
hardware/

README.md

components.md

circuit_description.md

firmware_connections.md
```

---

## Future Improvements

- PCB implementation
- Higher-resolution infrared camera
- Integrated touchscreen
- Wireless charging
