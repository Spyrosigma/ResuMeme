import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
import pymupdf

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Resu-MeMe 👾")
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
                        "I'm giving you my Resume. In the response, Be short and concise (20-30 lines). Don't say anything about formatting/spacing (how content is written) of the resume, just roast on the content present in it. Find every flaw, cringeworthy line, and every reason why this person shouldn't get hired. Be as ruthless as possible! Don't act like a chatbot/LLM, answer in a real-person manner, use puns and dialogues... Be creative!
                        Here's the RESUME: {text}
                """,
            }
        ],
        model="llama3-8b-8192",
    )

    st.markdown(chat_completion.choices[0].message.content)
    doc.close()
    os.remove(save_path)

