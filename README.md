# Chicken Disease Classification 🐔🦠

## Workflows

1. Update config.yaml
2. update secrets.yaml [optional]
3. update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the Components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## 📌 Overview  
Chicken Disease Classification is a deep learning-based project designed to detect and classify various chicken diseases using image data. The system leverages **transfer learning (VGG16)** to achieve high accuracy and assist poultry farmers in early disease identification, thereby reducing potential losses and improving farm productivity.

---

## 🚀 Key Features  

- ✅ **Automated Data Ingestion**: 
  - Downloads and extracts dataset efficiently using a configurable pipeline.  

- ✅ **Transfer Learning Model**: 
  - Utilizes **VGG16 architecture** with custom top layers for disease classification.  

- ✅ **Data Augmentation**: 
  - Applies real-time image augmentation (rotation, flipping, zooming) to improve model robustness.  

- ✅ **Training and Validation Pipelines**: 
  - Structured **80:20** split with TensorFlow's `ImageDataGenerator`.  
  - Handles batch processing and shuffling for optimal training.  

- ✅ **Modular Code Structure**: 
  - Separate classes for data ingestion, model preparation, training, and evaluation.  
  - Easy to scale, update, and maintain.  

- ✅ **Performance Evaluation**: 
  - Generates and saves accuracy and loss metrics in JSON format for reproducibility and tracking.  

- ✅ **Configurable via YAML/Entity Files**: 
  - All parameters like image size, batch size, learning rate, and dataset paths are configurable.  

---

## 🛠️ Technologies Used  

- **TensorFlow & Keras** – Deep learning and transfer learning.  
- **Python** – Core programming language.  
- **Librosa (optional)** – For audio processing if extending to sound-based detection.  
- **OS, Zipfile, Pathlib** – File handling and directory management.  
- **Git** – Version control.  

---

## ⚙️ Project Workflow  

1. **Data Ingestion**: Download and extract dataset.  
2. **Prepare Base Model**: Load VGG16 without top layers, configure for transfer learning.  
3. **Training**: Train the model with augmented and validated data.  
4. **Evaluation**: Test on validation data and save performance metrics.  
5. **Model Saving**: Save both base and trained models for deployment.  

---

## 🎯 Impact  

- Early detection of chicken diseases, reducing mortality rates.  
- Improved poultry health management with AI-driven solutions.  
- Scalable framework that can be adapted to other animal disease classification tasks.

---

## 🚧 Future Work  

- Integrate real-time image/audio classification system.  
- Deploy model as an API or web-based application for end-user access.  
- Expand dataset for more diseases and better generalization.
