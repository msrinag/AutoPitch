import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import os

from Chains import Chain
from portfolio import Portfolio
from utils import clean_text



def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    # User inputs for name, role, organization, and organization description
    name = st.text_input("Enter your name:", value="Mohan")
    role = st.text_input("Enter your role:", value="business development executive")
    organization = st.text_input("Enter your organization:", value="AtliQ")
    organization_description = st.text_area("Enter organization description:", 
        value="an AI & Software Consulting company dedicated to facilitating the seamless integration of business processes through automated tools")

    # URL input and submit button
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-40387")
    submit_button = st.button("Submit")
    
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = ', '.join(job.get('skills', []))
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links,name, role,organization, organization_description)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)


