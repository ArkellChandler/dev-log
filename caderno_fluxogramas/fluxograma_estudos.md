# Caderno de Fluxogramas: Engenharia de Dados

Este diretório contém diagramas e fluxogramas para auxiliar na visualização de processos técnicos.

## 01. Ciclo de Estudo SQL
```mermaid
graph TD
    A[Sintaxe Básica] --> B[Consultas JOIN]
    B --> C[Modelagem de Dados]
    C --> D[Otimização de Queries]
    D --> A
```

## 03. Hierarquia de ISPs (Provedores)

A internet é uma "rede de redes". Elas se organizam em níveis (Tiers) baseados em sua abrangência.

```mermaid
graph TD
    T1[Tier 1: Provedores Globais / Backbone] --- IXP[IXP: Pontos de Troca]
    T1 --- T2[Tier 2: Provedores Regionais]
    T2 --- T3[Tier 3: Provedores Locais / Acesso]
    T3 --- User[Usuário Final / Empresa]

    subgraph Legenda_Hierarquia
        L1[Tier 1: Conectam continentes, não pagam tráfego entre si]
        L2[Tier 2: Pagam ao Tier 1, cobram do Tier 3]
        L3[Tier 3: Onde você contrata sua internet]
    end
```

## 04. Atrasos, Perda e Vazão (Métricas de Performance)

### Tipos de Atraso (Delay)
O atraso total de um pacote em um nó (roteador) é a soma de 4 componentes:

1.  **Processamento ($d_{proc}$):** Tempo para o roteador ler o cabeçalho e decidir para onde enviar. (Limite: Microsegundos).
2.  **Fila ($d_{queue}$):** Tempo que o pacote espera para ser transmitido. Depende do tráfego. (Limite: Variável).
3.  **Transmissão ($d_{trans}$):** Tempo para "empurrar" todos os bits do pacote para o cabo. Fórmula: $L/R$ ($L$ = bits, $R$ = velocidade do cabo).
4.  **Propagação ($d_{prop}$):** Tempo para o sinal viajar fisicamente pelo cabo (velocidade da luz). Fórmula: $Distância/Velocidade$.

### Equação do Atraso Fim a Fim (N+1)
Se você tem uma rede com **$N$** roteadores entre a origem e o destino, você terá **$N+1$** trechos (links) de conexão.
*   **Atraso Total de Transmissão** = $(N+1) \times (L/R)$
*   *Explicação:* Cada roteador precisa receber o pacote inteiro antes de enviar para o próximo link. Se há 2 roteadores, o pacote será transmitido 3 vezes ($N+1$).

### Influência dos Parâmetros nas Aplicações

| Parâmetro | Unidade | Definição Literal | Exemplo de Uso |
| :--- | :--- | :--- | :--- |
| **Latência (ms)** | Milissegundos | Tempo total de ida e volta do sinal. | Jogos Online (Ping < 50ms é ideal). |
| **Vazão (Mbps)** | Megabits/s | Quantidade de dados que passam por segundo. | Streaming 4K (Exige > 25 Mbps). |
| **Perda (Loss)** | Porcentagem % | Pacotes que "caem" quando a fila do roteador lota. | Chamadas de Vídeo (Causa travamentos). |

**Conceitos Importantes:**
*   **Latência (ms):** É a "velocidade de resposta". Se for alta, a ação demora a acontecer.
*   **Vazão (Throughput):** É a "largura do cano". Se for baixa, arquivos grandes demoram a baixar.


