import streamlit as st
import torch
import torch.nn as nn

from torchvision import models
from torchvision import transforms

from PIL import Image

st.set_page_config(
    page_title="Pneumonia Detection",
    page_icon="🫁",
    layout="centered"
)

st.title("🫁 Pneumonia Detection")
st.write(
    "Upload a chest X-ray image to predict whether it is Normal or Pneumonia."
)

device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)


def create_resnet18():

    model = models.resnet18(weights=None)

    model.fc = nn.Linear(
        model.fc.in_features,
        1
    )

    return model


@st.cache_resource
def load_model():

    model = create_resnet18()

    model.load_state_dict(
        torch.load(
            "best_resnet18.pth",
            map_location=device
        )
    )

    model = model.to(device)

    model.eval()

    return model


model = load_model()


transform = transforms.Compose([

    transforms.Resize((224, 224)),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )

])


uploaded_file = st.file_uploader(
    "Choose a Chest X-ray image",
    type=["jpg", "jpeg", "png"]
)

THRESHOLD = 0.75

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Chest X-ray",
        use_container_width=True
    )

    input_tensor = transform(image)

    input_tensor = input_tensor.unsqueeze(0)

    input_tensor = input_tensor.to(device)

    with st.spinner("Analyzing image..."):

        with torch.no_grad():

            logits = model(input_tensor)

            probability = torch.sigmoid(logits).item()

    if probability >= THRESHOLD:

        prediction = "🦠 Pneumonia"
        confidence = probability

        st.error(f"Prediction: {prediction}")

    else:

        prediction = "✅ Normal"
        confidence = 1 - probability

        st.success(f"Prediction: {prediction}")

    st.subheader("Confidence")

    st.progress(float(confidence))

    st.metric(
        "Confidence Score",
        f"{confidence*100:.2f}%"
    )

    with st.expander("Prediction Details"):

        st.write(f"**Raw Probability:** {probability:.4f}")
        st.write(f"**Decision Threshold:** {THRESHOLD}")

    st.warning(
        "This application is intended for educational purposes only and "
        "should not be used as a substitute for professional medical diagnosis."
    )