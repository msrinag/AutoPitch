# 📧 Cold Email Generator

## Overview

The Cold Email Generator is a tool designed to help **managers and executives from consultancy firms**. When these professionals come across job postings, they can use this tool to scan job descriptions and relate them to their portfolios. The tool is built with **LangChain** and integrates **Google Gemini Pro 1.5** for generating AI-powered cold emails. 

By leveraging a vector space model to match the skills required for jobs with relevant projects from a portfolio, this tool generates tailored cold emails that highlight the organization's capabilities. Additionally, it allows for customization of the sender's name, role, and organization details, making it highly versatile for different users and job postings.


## Demo

![Demo GIF](assets/AutoPitch_Demo.gif)


## Features

- **Job Extraction**: Automatically extract key job details (role, experience, skills, description) from job posting pages.
- **Cold Email Generation**: Craft personalized cold emails by matching job skills with the user’s portfolio.
- **Customizable User Information**: Users can input their name, role, organization, and description to personalize the emails.
- **Portfolio Integration**: Uses a **vector space model** (powered by FAISS) to match job requirements with relevant past work from the portfolio.
- **Streamlit Interface**: An intuitive web interface to input job URLs, customize user information, and generate emails seamlessly.

## How It Works

1. **Input a Job Posting URL**: Enter a URL to a job posting (publicly accessible without login).
2. **Extract Job Details**: The tool scrapes the job page and extracts key information such as role, experience, skills, and description.
3. **Portfolio Matching**: The tool uses a vector space model to match the job’s skills with your past work, based on your portfolio.
4. **Email Generation**: An AI-generated cold email is created based on your input and matched portfolio items.
5. **Customization**: You can tailor the sender’s name, role, and organization description to match your preferences.

## Tech Stack

- **LangChain**: Used for orchestrating the job extraction and email generation pipeline.
- **Google Gemini Pro 1.5**: For powerful, AI-generated emails.
- **FAISS**: Vector search engine to match skills from job descriptions with portfolio items.
- **Streamlit**: For the user-friendly web interface



