from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()
from browser_use import Controller, ActionResult

import asyncio

llm = ChatOpenAI(model="gpt-4o")


# Initialize the controller
controller = Controller()

@controller.action('Ask user for information')
def ask_human(question: str) -> str:
    answer = input(f'\n{question}\nInput: ')
    return ActionResult(extracted_content=answer)

@controller.action('Create a personalized resume using the job description as the input')
def personalized_resume(job_description) -> str:
    answer = personalize_resume(job_description)
    return ActionResult(extracted_content=answer)

#Collect the linkedin link of the person who is responsible in the hiring team
#Find the job description of this, and then personalize the resume
#When you reach the upload resume page, you will call the upload_personalized_resume function:
# This then uploads the resume to the website
# After uploading the resume, you can function as normal
#Todo:

#Add the planner agent functionality to the controller 
#Add a system prompt that describes the tools?



async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())