import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# --- MÁQUINAS DE PERSISTÊNCIA (HD) ---

def salvar_tarefas(lista):
    """Grava a lista de tarefas no arquivo JSON."""
    with open("tarefas.json", "w") as arquivo:
        json.dump(lista, arquivo)

def carregar_tarefas():
    """Lê o arquivo JSON e traz as tarefas de volta."""
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return [] # Se não houver arquivo, começa do zero

# --- INTERFACE ---

def exibir_menu():
    console.print("\n[bold blue]       MENU PRINCIPAL[/]")
    console.print("1. Adicionar Tarefa")
    console.print("2. Listar Tarefas")
    console.print("3. Marcar como Concluída")
    console.print("4. Remover Tarefa")
    console.print("5. Sair")

def main():
    # 1. Carregamos o que já existe no HD ao iniciar
    lista_tarefas = carregar_tarefas()

    while True:
        console.print(Panel("[bold green]📝 GERENCIADOR DE TAREFAS (COM PERSISTÊNCIA)[/]", expand=False))
        exibir_menu()
        
        opcao = console.input("\n[bold cyan]Escolha uma opção: [/]")

        if opcao == '1':
            nome = console.input("[yellow]Nome da tarefa: [/]")
            nova_tarefa = {"nome": nome, "concluida": False}
            lista_tarefas.append(nova_tarefa)
            # 2. Salvamos no HD após adicionar
            salvar_tarefas(lista_tarefas)
            console.print("[bold green]✔ Tarefa adicionada e SALVA![/]")

        elif opcao == '2':
            if not lista_tarefas:
                console.print("[bold red]Nenhuma tarefa cadastrada![/]")
            else:
                tabela = Table(title="Minhas Tarefas")
                tabela.add_column("ID", justify="center", style="cyan")
                tabela.add_column("Tarefa", style="magenta")
                tabela.add_column("Status", justify="center")

                for indice, tarefa in enumerate(lista_tarefas):
                    status = "[green]✔[/]" if tarefa["concluida"] else "[red]✘[/]"
                    tabela.add_row(str(indice + 1), tarefa["nome"], status)
                
                console.print(tabela)

        elif opcao == '3':
            try:
                id_selecionado = int(console.input("[yellow]ID da tarefa para concluir: [/]"))
                indice = id_selecionado - 1
                lista_tarefas[indice]["concluida"] = True
                # 3. Salvamos no HD após concluir
                salvar_tarefas(lista_tarefas)
                console.print("[bold green]✔ Status atualizado e SALVO![/]")
            except (ValueError, IndexError):
                console.print("[bold red]Erro: ID inválido![/]")

        elif opcao == '4':
            try:
                id_para_remover = int(console.input("[red]ID da tarefa para REMOVER: [/]"))
                indice = id_para_remover - 1
                tarefa_removida = lista_tarefas.pop(indice)
                # 4. Salvamos no HD após remover
                salvar_tarefas(lista_tarefas)
                console.print(f"[bold red]✘ Tarefa '{tarefa_removida['nome']}' removida e SALVA![/]")
            except (ValueError, IndexError):
                console.print("[bold red]Erro: Não foi possível remover![/]")

        elif opcao == '5':
            console.print("[bold red]Saindo... Suas tarefas estão seguras no HD![/]")
            break
        else:
            console.print("[bold red]Opção inválida![/]")

if __name__ == "__main__":
    main()
