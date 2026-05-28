from agents.base_agent import BaseAgent

class CodingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Coding Agent",
            role="Write Python code solutions."
        )