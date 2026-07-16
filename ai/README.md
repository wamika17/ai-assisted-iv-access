# Artificial Intelligence

This module contains the AI pipeline responsible for vein analysis and clinical decision support.

Instead of replacing clinical judgment, the AI assists healthcare professionals by processing infrared images, extracting vein-related features, estimating IV access difficulty, and supporting vessel identification.

---

## AI Pipeline

Infrared Image

↓

Image Enhancement

↓

Vein Segmentation

↓

Vein Feature Extraction

↓

DIVA Score Prediction

↓

Clinical Recommendation

---

## AI Modules

- vein_segmentation.py
- vein_mapping.py
- artery_vein_classifier.py
- diva_prediction.py

---

## Future Improvements

- Deep Learning Segmentation
- Real-time Edge AI
- Explainable AI
- Personalized IV Recommendations
