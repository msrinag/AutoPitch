import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import os
from Chains import Chain
from portfolio import Portfolio
from utils import clean_text
import sqlite3
st.write(sqlite3.sqlite_version)
print(sqlite3.sqlite_version)


def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(page_title="AutoPitch", page_icon="🤖")
    st.title("📧 Cold Mail Generator")
    st.write(os.environ["GOOGLE_API_KEY"] )
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-38703")
    submit_button = st.button("Submit")
    
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)


