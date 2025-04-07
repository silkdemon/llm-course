import getpass
import os

from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello World")


    summary_template = """
    given the information {information} about a person from i want you to create:
    1) a short summary
    2) two interesting facts
    """

    summary_prompt_template = PromptTemplate(
        template=summary_template, input_variables=["information"]
    )

    llm = OllamaLLM(model="llama3", temperature=0)
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    information = scrape_linkedin_profile()

    print(chain.run(information=information.json()))
