import streamlit as st
from deepface import DeepFace
import tempfile

st.title("😊 EmoReflect - Your Emotional Mirror App")
st.write("Upload an image to detect your emotion.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        img_path = tmp_file.name

    st.image(img_path, caption="Uploaded Image", use_column_width=True)

    try:
        result = DeepFace.analyze(img_path=img_path, actions=['emotion'])
        emotion = result[0]['dominant_emotion']

        st.subheader(f"Detected Emotion: {emotion.capitalize()}")

        tips = {
            "happy": "Keep spreading positivity! 🌟",
            "sad": "It's okay to feel sad. Take a break, talk to a friend 💙",
            "angry": "Take deep breaths. Relax, you've got this. ✨",
            "neutral": "Stay mindful and keep balanced 🧘",
            "fear": "Face your fears, you’re stronger than you think 💪",
            "surprise": "Life is full of surprises – enjoy the moment 🎉",
            "disgust": "Let go of negativity, focus on what makes you smile 🌸"
        }
        st.info(tips.get(emotion.lower(), "Stay positive and strong! ❤️"))

    except Exception as e:
        st.error("Could not analyze the image. Please try another one.")
