
import matplotlib.pyplot as plt
import networkx as nx
import os

# Definir o caminho de saída para a mesma pasta do script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "fluxograma_devlog.png")

# Criar o grafo para o fluxograma
G = nx.DiGraph()

# Definir os nós (Etapas do Dev-Log baseadas no README.md)
nodes = [
    ("Dev-Log", "Repositório Principal"),
    ("05_SQL", "Estudos SQL\n(JOINs, Filtros)"),
    ("06_MySQL", "Conexão Web\n(PHP/mysqli)"),
    ("Bootcamp TOTVS", "Lógica &\nProjetos Mercado"),
    ("Integração", "Python + PHP\n+ Bancos de Dados")
]

for node, label in nodes:
    G.add_node(node, label=label)

# Definir as conexões (Fluxo de dados e conhecimento)
edges = [
    ("05_SQL", "06_MySQL"),
    ("05_SQL", "Integração"),
    ("06_MySQL", "Integração"),
    ("Bootcamp TOTVS", "Integração"),
    ("Dev-Log", "05_SQL"),
    ("Dev-Log", "Bootcamp TOTVS")
]

G.add_edges_from(edges)

# Configurar o layout e desenho
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, with_labels=False, node_size=3000, node_color="skyblue", 
        font_size=10, font_weight="bold", arrows=True, edge_color="gray")

# Adicionar labels personalizados
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels, font_size=9)

plt.title("Fluxograma de Integração: Dev-Log", fontsize=15, pad=20)
plt.axis('off')

# Salvar a imagem
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Fluxograma gerado com sucesso em: {output_path}")
