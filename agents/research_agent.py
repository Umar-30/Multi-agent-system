from agents.base_agent import BaseAgent
from tavily import TavilyClient
import os

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            role="Find detailed information from the internet and explain concepts."
        )
        self.tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def think(self, task):
        # 1. Search the internet using Tavily
        search_result = self.tavily.search(query=task, search_depth="advanced")
        
        # 2. Format the search results for the LLM
        context = "\n".join([f"- {res['title']}: {res['content']} (Source: {res['url']})" for res in search_result['results']])
        
        # 3. Create a prompt that includes the real-time search data
        prompt = f"""
You are the Research Agent.
Your role: {self.role}

The user wants to know about: {task}

Here is the real-time information I found on the internet:
{context}

Please synthesize this information and provide a detailed research report.
"""

        response = self.client.chat(
            model="command-r-08-2024",
            message=prompt
        )

        return response.text