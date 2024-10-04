import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


class Chain:
    def __init__(self):
        self.llm =  ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links,name="Mohan", role="business development executive",
               organization="AtliQ", organization_description="an AI & Software Consulting company dedicated to facilitating the seamless integration of business processes through automated tools"):
        prompt_email = PromptTemplate.from_template(
            """
             ### JOB DESCRIPTION:
        {job_description}

        ### INSTRUCTION:
        You are {name}, a {role} at {organization}. {organization} is {organization_description}. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of {organization} 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase {organization}'s portfolio: {{link_list}}
        Remember you are {name}, {role} at {organization}.
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):  
        ### WHILE MENTIOING PORTFOLIO LINK JUST THE LINK ITSELF IS ENOUGH DONT ADD TEXT FOR IT JUST INTRODUCE AND MENTION LINK
        """)
                   
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({
        "job_description": str(job), 
        "link_list": links, 
        "name": name, 
        "role": role, 
        "organization": organization, 
        "organization_description": organization_description
    })
        return res.content

if __name__ == "__main__":
    print("api")
    print(os.getenv("GOOGLE_API_KEY"))
