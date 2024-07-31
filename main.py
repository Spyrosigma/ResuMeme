import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
import pymupdf

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Resume-Roaster")
st.write("Upload on your own risk, we can Roast you badly !")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
text = ""
if uploaded_file is not None:
    save_path = os.path.join("uploaded_files", uploaded_file.name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    doc = pymupdf.open(save_path)
    for page in doc:
        text = page.get_text()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""This is a Resume/CV, your task is to roast the things that this person has written in resume in very badly, make no mercy ! Try to keep it short and use puns.
                    Here's the RESUME: {text}
                """,
            }
        ],
        model="llama3-8b-8192",
    )

    st.markdown(chat_completion.choices[0].message.content)
    doc.close()
    os.remove(save_path)

