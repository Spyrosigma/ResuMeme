import streamlit as st
import pandas as pd
from io import StringIO
import pymupdf
import fitz 
from pypdf import PdfReader

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    data = PdfReader(uploaded_file.read())
    st.write(data)
      
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # string_data = stringio.read()
    # st.write(string_data)
    '''
    00:01 Initial package does not matter, growth and learning do
02:35 Consider work-life balance, Equity, and learning curve over high salary
03:55 Software development can impact work-life balance negatively
05:15 Explore different coding languages and tech stacks to grow your skills
06:38 Acquire specific knowledge for high income
08:05 Taking calculated risks in career choices
09:29 Consider holding onto equity in startups if you believe in the team
10:52 Choose technically strong teams for long-term growth

'''