from rich.console import Console
import time # Vamos usar isso para dar um efeito de carregamento

console = Console()

# CONSTANTE: O prefixo da rede (não muda durante o script)
PREFIXO_REDE = "192.168.0."

# LISTA (Snake Case): Os finais dos IPs que queremos testar
finais_ip = [1, 10, 15, 22, 254]

console.print("[bold yellow]Iniciando Varredura de Segurança...[/]\n")

# O laço FOR: Para cada 'fim' dentro da nossa lista 'finais_ip'
for fim in finais_ip:
    ip_completo = f"{PREFIXO_REDE}{fim}"
    
    console.print(f"[*] Testando conexão em: [cyan]{ip_completo}[/]")
    
    # Simula um pequeno atraso de 0.5 segundos
    time.sleep(0.5) 
    
    console.print(f"[bold green][+][/] Dispositivo {ip_completo} está ativo!")

console.print("\n[bold blue]Varredura concluída.[/]")
