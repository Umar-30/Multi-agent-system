from agents.research_agent import ResearchAgent
from agents.coding_agent import CodingAgent
from agents.summarizer_agent import SummarizerAgent
from communication.message_bus import MessageBus
from rich.console import Console
from rich.panel import Panel
from rich.status import Status

class Coordinator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.coding_agent = CodingAgent()
        self.summarizer_agent = SummarizerAgent()
        self.bus = MessageBus()
        self.console = Console()

    def execute(self, user_task):
        self.bus.send("User", "Coordinator", user_task)

        # 1. Research Phase
        with self.console.status("[bold blue]Research Agent is thinking...", spinner="dots"):
            research = self.research_agent.think(user_task)
            self.bus.send("Coordinator", "Research Agent", user_task)
            self.bus.send("Research Agent", "Coordinator", research)

        self.console.print(Panel(research, title="[bold blue]Research Output", border_style="blue"))

        # 2. Coding Phase
        coding_prompt = f"Based on this research:\n{research}"
        with self.console.status("[bold green]Coding Agent is working...", spinner="dots"):
            code = self.coding_agent.think(coding_prompt)
            self.bus.send("Coordinator", "Coding Agent", coding_prompt)
            self.bus.send("Coding Agent", "Coordinator", code)

        self.console.print(Panel(code, title="[bold green]Coding Output", border_style="green"))

        # 3. Summary Phase
        summary_prompt = f"""
            Research:
            {research}

            Code:
            {code}
            """
        with self.console.status("[bold cyan]Summarizer Agent is finalizing...", spinner="dots"):
            summary = self.summarizer_agent.think(summary_prompt)
            self.bus.send("Coordinator", "Summarizer Agent", summary_prompt)
            self.bus.send("Summarizer Agent", "Coordinator", summary)

        return summary