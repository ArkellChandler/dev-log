from rich.console import Console
from rich.panel import Panel

console = Console()

# Entrada de dados
n1 = int(console.input("[bold cyan]Digite um número para análise:[/] "))

# Lógica de Decisão
if n1 % 2 == 0:
    status = "[bold green]PAR[/]"
    detalhe = "Este número pode ser dividido igualmente por 2."
else:
    status = "[bold yellow]ÍMPAR[/]"
    detalhe = "Este número deixa resto 1 quando dividido por 2."

# Resultado Visual
resultado_texto = f"O número {n1} é {status}\n\n{detalhe}"

console.print(Panel(resultado_texto, title="ANALISADOR "))
