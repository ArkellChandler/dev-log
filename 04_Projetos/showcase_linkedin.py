import time
from rich.console import Console
from rich.syntax import Syntax
from rich.tree import Tree
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table

console = Console()

def gerar_magia():
    # 1. Título de Inicialização
    console.clear()
    console.print(Panel.fit("[bold cyan]INICIALIZANDO AMBIENTE DE DESENVOLVIMENTO - ARKELL CHANDLER[/]", border_style="blue"))
    time.sleep(1)

    # 2. Árvore do Projeto
    tree = Tree("📂 [bold blue]PythonEstudos[/]")
    basico = tree.add("📁 01_Basico")
    basico.add("📄 fluxo_caixa.py")
    basico.add("📄 scanner_de_rede.py")
    
    logica = tree.add("📁 03_Logica")
    logica.add("📄 verificador_senha.py")
    logica.add("📄 sistema_seguranca.py")
    logica.add("📄 ESTUDOS_LOGICA.md")
    
    projetos = tree.add("📁 04_Projetos")
    projetos.add("📄 [bold green]gerenciador_tarefas.py[/]")
    projetos.add("📄 tarefas.json")
    
    console.print("\n[bold]ESTRUTURA DO REPOSITÓRIO:[/]")
    console.print(tree)
    time.sleep(1.5)

    # 3. Amostra de Código com Sintaxe
    console.print("\n[bold]ANALISANDO CÓDIGO FONTE (gerenciador_tarefas.py):[/]")
    code = """
def buscar_tarefas(lista, termo):
    \"\"\"Filtra a lista por um termo de busca (ignora maiúsculas/minúsculas).\"\"\"
    resultados = []
    for tarefa in lista:
        if termo.lower() in tarefa["nome"].lower():
            resultados.append(tarefa)
    return resultados
    """
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
    time.sleep(1.5)

    # 4. Simulação de Deploy / Push
    console.print("\n")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task1 = progress.add_task("[cyan]Sincronizando com GitHub...", total=100)
        task2 = progress.add_task("[magenta]Gerando Fluxogramas...", total=100)
        
        while not progress.finished:
            progress.update(task1, advance=0.9)
            progress.update(task2, advance=0.6)
            time.sleep(0.02)

    # 5. Painel Final de Sucesso
    console.print("\n")
    mensagem = "[bold green]PROJETO ATUALIZADO COM SUCESSO NO GITHUB![/]\n\n"
    mensagem += "[white]Repositório:[/][cyan] github.com/ArkellChandler/dev-log[/]\n"
    mensagem += "[white]Status:[/][green] Public[/]\n"
    mensagem += "[white]Bootcamp:[/][yellow] TOTVS 2026[/]"
    
    console.print(Panel(mensagem, title="[bold blue]DEVOPS STATUS[/]", expand=False, border_style="green"))

if __name__ == "__main__":
    gerar_magia()
