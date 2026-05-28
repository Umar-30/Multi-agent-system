from core.coordinator import Coordinator
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

def main():
    console = Console()
    
    # Welcome Banner
    banner = Text("\nMulti-Agent System CLI", style="bold magenta")
    banner.append("\n-----------------------", style="magenta")
    console.print(Panel(banner, border_style="magenta", expand=False))

    task = Prompt.ask("\n[bold yellow]Enter your task[/bold yellow]")

    coordinator = Coordinator()

    result = coordinator.execute(task)

    console.print("\n" + "="*20 + " FINAL OUTPUT " + "="*20 + "\n", style="bold cyan")
    console.print(Panel(result, title="[bold white]Final Summary", border_style="cyan"))
    
    # Show message bus count as proof of integration
    console.print(f"\n[dim]Total messages recorded in MessageBus: {len(coordinator.bus.get_messages())}[/dim]")

if __name__ == "__main__":
    main()