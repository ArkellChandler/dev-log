from rich.console import Console
from rich.panel import Panel
import re

console = Console()

def verificar_forca(senha):
    score = 0
    criterios = []

    # Critério 1: Comprimento
    if len(senha) >= 8:
        score += 1
        criterios.append("[green][✔] Mínimo 8 caracteres[/]")
    else:
        criterios.append("[red][✘] Mínimo 8 caracteres[/]")

    # Critério 2: Números
    if any(char.isdigit() for char in senha):
        score += 1
        criterios.append("[green][✔] Contém números[/]")
    else:
        criterios.append("[red][✘] Contém números[/]")

    # Critério 3: Letras Maiúsculas
    if any(char.isupper() for char in senha):
        score += 1
        criterios.append("[green][✔] Letras maiúsculas[/]")
    else:
        criterios.append("[red][✘] Letras maiúsculas[/]")

    # Critério 4: Caracteres Especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        score += 1
        criterios.append("[green][✔] Caracteres especiais[/]")
    else:
        criterios.append("[red][✘] Caracteres especiais[/]")

    return score, criterios

# Interface
console.print(Panel("[bold magenta]VERIFICADOR DE FORÇA DE SENHA[/]", expand=False))
senha_usuario = console.input("[bold cyan]Digite uma senha para testar: [/]")

score, lista_criterios = verificar_forca(senha_usuario)

# Resultado final
niveis = {0: "MUITO FRACA", 1: "FRACA", 2: "MÉDIA", 3: "FORTE", 4: "MUITO FORTE"}
cor_nivel = {0: "red", 1: "red", 2: "yellow", 3: "blue", 4: "green"}

texto_resultado = "\n".join(lista_criterios)
texto_resultado += f"\n\n[bold {cor_nivel[score]}]NÍVEL: {niveis[score]}[/]"

console.print(Panel(texto_resultado, title="Resultado da Análise"))
