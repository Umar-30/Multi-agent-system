from agents.base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Summarizer Agent",
            role="""You are a professional summarizer. Your task is to take the Research findings and the generated Code, 
            and create a clear, concise final response for the user. Highlight the key points of the research 
            and explain what the code does."""
        )