from rich.console import Console
import time

console = Console()

# CONSTANTES (Regras que não mudam)
IP_ALVO = "192.168.1.1"
PORTA_INICIAL = 75
PORTA_FINAL = 80

console.print(f"[bold red]SCANNING {IP_ALVO}...[/]\n")

# O range vai de 75 até 80 (por isso usamos PORTA_FINAL + 1)
for porta in range(PORTA_INICIAL, PORTA_FINAL + 1):
    console.print(f"[*] Verificando porta [yellow]{porta}[/]...", end="\r")
    
    time.sleep(0.4) # Simula o tempo de resposta
    
    if porta == 80:
        console.print(f"[bold green][+] Porta {porta} (HTTP) aberta!    [/]")
    else:
        console.print(f"[dim red][-] Porta {porta} fechada.          [/]")

console.print("\n[bold blue]Varredura completa.[/]")
