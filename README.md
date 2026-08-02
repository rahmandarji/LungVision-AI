# 🫁 LungVision-AI

An end-to-end Deep Learning project for detecting **Pneumonia** from pediatric chest X-ray images using **Transfer Learning with ResNet18** and **PyTorch**.

This project was built to gain hands-on experience with the complete Deep Learning workflow—from preprocessing medical images and training a convolutional neural network to deploying the model as an interactive web application.

---

# 🚀 Live Demo

https://lungvision-ai-gabksershqno8fndaxk6pj.streamlit.app

---

# 🎯 Project Objective

The objective of this project was to understand and implement an end-to-end Computer Vision pipeline.

Instead of only training a model, the project focuses on the complete machine learning lifecycle:

- Data preprocessing
- Image augmentation
- Transfer Learning
- Model training
- Model evaluation
- Deployment using Streamlit
- Version control using Git
- Large model management using Git LFS

---

# 🧠 What I Learned

Through this project I gained practical experience with:

- Building image classification models using PyTorch
- Transfer Learning with ResNet18
- Medical image preprocessing
- Data augmentation
- Batch Normalization
- Dropout
- BCEWithLogitsLoss
- Early Stopping
- Model evaluation
- Saving and loading trained models
- Deploying Deep Learning applications using Streamlit
- Managing large model files using Git LFS
- Debugging deployment and dependency issues

---

# 🛠 Technologies Used

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

![Upload](images/Prediction.png)

---

## Prediction & Confidence

![Prediction](images/Confidence.png)

---

# 🧪 Example Predictions

## Normal Chest X-ray

![Normal](images/Normal.jpeg)

Prediction:

✅ Normal

---

## Pneumonia Chest X-ray

![Pneumonia](images/Pneumonia.jpeg)

Prediction:

🦠 Pneumonia

Confidence:

**99.11%**

---

# 📂 Project Structure

```text
LungVision-AI/

│── images/
│   ├── Prediction.png
│   ├── Confidence.png
│   ├── Normal.jpeg
│   └── Pneumonia.jpeg
│
├── computer_vision.py
├── best_resnet18.pth
├── requirements.txt
├── README.md
```

---

# ⚙️ Running the Project

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
# 📌 Future Improvements

- Support additional chest diseases
- Add Grad-CAM visualization for model explainability
- Improve calibration of prediction confidence
- Train and compare multiple CNN architectures (EfficientNet, DenseNet, Vision Transformer)
- Containerize the application with Docker

---

# ⚠️ Disclaimer

This application is intended for educational purposes only and should **not** be used as a substitute for professional medical diagnosis or clinical decision-making.

---

# 👨‍💻 Author

Rahman Darji

Machine Learning • Deep Learning • Computer Vision
