from rich.console import Console
from rich.panel import Panel

console = Console()

def verificar_classificacao(pontos):
    """
    Verifica se o jogador alcançou o teto de 100 pontos.
    Retorna a mensagem de sucesso ou o valor booleano False.
    """
    if pontos >= 100:
        return "[bold green]Well done! You have advanced to the qualifying stage.[/]\n[yellow]Win 2 out of your next 3 games to rank up.[/]"
    else:
        # Retorna o valor literal conforme solicitado
        return False

def main():
    # Título do Desafio
    console.print(Panel("[bold cyan]🛡️ SISTEMA DE RANK UP RPG - CLASSE E5[/]", expand=False))
    
    try:
        # Entrada de dados do jogador
        entrada = console.input("[bold yellow]Digite sua pontuação atual (0-100+): [/]")
        pontos = int(entrada)
        
        # A "Máquina de Decisão" entra em ação
        resultado = verificar_classificacao(pontos)
        
        # Verificação do Retorno
        if resultado:
            # Se for uma string (mensagem de sucesso)
            console.print(Panel(resultado, title="[bold green]STATUS: CLASSIFICATÓRIA[/]", border_style="green"))
        else:
            # Se a função devolveu 'False'
            console.print(Panel("[bold red]RANK UP NEGADO[/]\n[white]Você não atingiu os 100 pontos necessários.[/]", title="[bold red]STATUS ATUAL[/]", border_style="red"))
            console.print("[dim white]Dica: Continue jogando na classe E5 para subir de rank.[/]")
            
    except ValueError:
        # Proteção contra erros de digitação (letras em vez de números)
        console.print("[bold red]Erro: Por favor, digite um número inteiro para a sua pontuação![/]")

if __name__ == "__main__":
    main()
