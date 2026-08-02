# 🫁 LungVision-AI

Deep Learning-based Chest X-ray Classification using **PyTorch** and **ResNet18** for detecting **Pneumonia** from chest X-ray images.

---

# 🚀 Live Demo

**Try the application here:**

https://lungvision-ai-gabksershqno8fndaxk6pj.streamlit.app

---

# 📌 Overview

LungVision-AI is an end-to-end Computer Vision project that classifies chest X-ray images into:

- ✅ Normal
- 🦠 Pneumonia

The project covers the complete machine learning pipeline including:

- Data preprocessing
- Model training
- Transfer Learning using ResNet18
- Model evaluation
- Deployment with Streamlit
- GitHub version control
- Git LFS for large model storage

---

# ✨ Features

- Upload a chest X-ray image
- Instant prediction
- Confidence score
- Raw prediction probability
- Decision threshold visualization
- Medical disclaimer
- Responsive Streamlit interface

---

# 🧠 Model

**Architecture**

- ResNet18 (Transfer Learning)

**Framework**

- PyTorch

**Loss Function**

- BCEWithLogitsLoss

**Optimizer**

- Adam

**Regularization**

- Batch Normalization
- Dropout
- Early Stopping

---

# 🛠 Tech Stack

- Python
- PyTorch
- Torchvision
- Streamlit
- Pillow
- NumPy
- Git
- Git LFS

---

# 📷 Application Preview

## Upload Chest X-ray

![Application](images/app_upload.png)

---

## Prediction Result

![Prediction](images/prediction.png)

---

# 🧪 Sample Predictions

## Normal Chest X-ray

![Normal](images/normal_sample.jpeg)

Prediction

```
NORMAL
```

---

## Pneumonia Chest X-ray

![Pneumonia](images/pneumonia_sample.jpeg)

Prediction

```
PNEUMONIA
Confidence: 99.11%
```

---

# 📂 Project Structure

```
LungVision-AI
│
├── images/
│   ├── app_upload.png
│   ├── prediction.png
│   ├── normal_sample.jpeg
│   └── pneumonia_sample.jpeg
│
├── computer_vision.py
├── best_resnet18.pth
├── requirements.txt
├── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LungVision-AI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run computer_vision.py
```

---

# ⚠️ Disclaimer

This application is intended for educational purposes only and should **not** be used as a substitute for professional medical diagnosis or clinical decision-making.

---

# 👨‍💻 Author

**Rahman**

Building end-to-end Machine Learning and Deep Learning projects with Python.
