import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
import pymupdf

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Resu-MeMe")
st.subheader("Upload on your own risk, we can Roast you badly !")

uploaded_file = st.file_uploader("Upload your Resume/CV", type="pdf")
text = ""
if uploaded_file is not None:
    save_path = os.path.join("uploads", uploaded_file.name)
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
                "content": 
                f"""
                        "Hey, I need you to absolutely tear apart this resume. Rip into it like there's no tomorrow. Find every flaw, every cringeworthy line, and every reason why this person shouldn't get hired. Spare no details and be as ruthless as possible! I want to make sure this person never makes these mistakes again. Let's do this!" Don't act like a chatbot, answer in a real-person manner.
                        Here's the RESUME: {text}
                """,
            }
        ],
        model="llama3-8b-8192",
    )

    st.markdown(chat_completion.choices[0].message.content)
    doc.close()
    os.remove(save_path)

