# Smart AI-Assisted IV Access System

An AI-assisted portable medical device designed to support healthcare professionals during intravenous (IV) cannulation by combining infrared vein imaging, physiological sensing, vein analysis, and clinical decision support.

The system integrates embedded hardware, computer vision, and machine learning to enhance vein visualization, estimate IV access difficulty using the DIVA (Difficult Intravenous Access) score, differentiate arteries and veins using physiological sensing, and provide real-time patient monitoring through an interactive dashboard.

---

## Clinical Problem

Obtaining intravenous (IV) access can be difficult in pediatric, elderly, obese, dehydrated, or critically ill patients. Multiple failed cannulation attempts increase patient discomfort, delay treatment, and increase healthcare costs.

Current commercial vein finders only improve visualization and often lack intelligent decision support.

This project aims to provide an integrated AI-assisted solution capable of assisting clinicians before and during IV insertion.

---

## Objectives

- Enhance vein visibility using infrared imaging.
- Detect and segment superficial veins.
- Extract clinically relevant vein parameters.
- Differentiate arteries and veins using physiological sensing.
- Predict DIVA score for difficult IV access.
- Monitor patient vitals in real time.
- Provide a portable and rechargeable bedside solution.

---

## Key Features

- Infrared vein imaging
- AI-assisted vein segmentation
- Vein parameter extraction
- DIVA score prediction
- Artery-vein differentiation using MAX30102
- Real-time physiological monitoring
- Oral spectroscopy probe for vital sensing
- Portable rechargeable hardware
- Interactive patient dashboard

---

## System Workflow

Patient

↓

Infrared Image Acquisition

↓

Image Enhancement

↓

Vein Segmentation

↓

Vein Parameter Extraction

↓

MAX30102 Physiological Analysis

↓

Artery / Vein Differentiation

↓

DIVA Score Prediction

↓

Patient Dashboard

↓

Clinical Decision Support

---

## Repository Structure

```text
smart-ai-assisted-iv-access-system/

├── hardware/
├── firmware/
├── ai/
├── medical-analysis/
├── dashboard/
├── docs/
├── dataset/
├── models/
└── images/
```

---

## Hardware Components

| Component | Purpose |
|-----------|----------|
| ESP32 | Embedded controller |
| Infrared Camera | Vein visualization |
| MAX30102 | Pulse and oxygen sensing |
| OLED Display | Local information display |
| Rechargeable Battery | Portable operation |
| Charging Module | Battery charging |

---

## Software Stack

- Arduino IDE
- Python
- OpenCV
- Flask
- NumPy
- Scikit-learn
- TensorFlow (Future)
- PyTorch (Future)

---

## AI Pipeline

Infrared Image

↓

Image Preprocessing

↓

Vein Segmentation

↓

Feature Extraction

↓

DIVA Prediction

↓

Patient Recommendation

---

## Medical Parameters

The system analyzes multiple patient-specific parameters, including:

- Vein diameter
- Vein depth
- Vein visibility
- Skin type
- Body Mass Index (BMI)
- Heart rate
- Oxygen saturation (SpO₂)

---

## Future Improvements

- Deep learning vein segmentation
- Automatic IV insertion assistance
- 3D vein reconstruction
- Wireless cloud synchronization
- Electronic Health Record integration
- Explainable AI recommendations

---

## Project Status

Prototype developed during the ETHiCARE AI Hackathon.

Current repository documents the system architecture, embedded implementation, AI workflow, and future development roadmap.

---

## Contributors

**Wamika Varada**

Hardware Lead

Electronics and Communication Engineering

Dayananda Sagar College of Engineering

---

## License

This project is released under the MIT License.
