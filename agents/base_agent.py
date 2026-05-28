import cohere
import os
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:

    def __init__(self, name, role):

        self.name = name
        self.role = role

        self.client = cohere.Client(
            os.getenv("COHERE_API_KEY")
        )

    def think(self, task):

        prompt = f"""
You are {self.name}.

Your role:
{self.role}

Task:
{task}
"""

        response = self.client.chat(
            model="command-r-08-2024",
            message=prompt
        )

        return response.text