import torch
from model import get_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from torchvision import transforms
from PIL import Image, ImageOps
import numpy as np

Net = get_model()

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
if device == "cpu":
    device = torch.device("mps" if torch.cuda.is_available() else "cpu")

model = Net()
model.load_state_dict(torch.load("model/mnist.pth", map_location=device))
model.eval()

transform = transforms.Compose(
    [
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
    ]
)

st.title("MNIST Hello world")
st.markdown("Draw a digit below and click Predict to classify it")

drawing_mode = "freedraw"

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=11,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=280,
    width=280,
    drawing_mode=drawing_mode,
    key="canvas",
)

if st.button("Predict"):
    if canvas_result.image_data is not None:
        img_data = canvas_result.image_data
        img = Image.fromarray(np.uint8(img_data)).convert("L")
        img_inverted = ImageOps.invert(img)

        img_inverted.save("drawn_digit.png")

        input_tensor = transform(img_inverted)
        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            prediction = model(input_batch).max(1, keepdim=True)[1].item()

        st.subheader(f"Predicted Digit: {prediction}")
else:
    st.write("Draw a digit to predict")
