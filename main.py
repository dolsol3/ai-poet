# .eev 불러오는 기능 / 설치 : pip install python-dotenv
# 로컬에서 사용. stremlit에서는 사용 안함.
# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI


# content = "프로그래밍 코딩"

# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result)

chat_model = ChatOpenAI()
st.title('인공지능 시인')
content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성해줘'):
    with st.spinner('시 작성중'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)
