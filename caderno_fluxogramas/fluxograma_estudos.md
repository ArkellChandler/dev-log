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

## 02. Arquitetura de Redes: A Borda e o Núcleo

Este fluxograma divide a internet em suas partes físicas e lógicas fundamentais.

```mermaid
graph TD
    subgraph Borda_da_Rede [1. A Borda da Rede]
        A[Sistemas Finais / Hosts] -->|Conectam-se via| B[Redes de Acesso]
        A1[PCs, Smartphones, Servidores, IoT] --- A
    end

    subgraph Redes_de_Acesso [2. Redes de Acesso]
        B --> B1[Residenciais: DSL, Cabo, FTTH-Fibra]
        B --> B2[Móveis: 4G/5G, Wi-Fi]
        B --> B3[Institucionais: Ethernet de Empresas/Escolas]
    end

    subgraph Meios_Fisicos [3. Meios Físicos]
        C1[Guiados: Cabos de Cobre, Fibra Óptica] --- B
        C2[Não Guiados: Ondas de Rádio, Satélite] --- B
    end

    subgraph Nucleo_da_Rede [4. O Núcleo da Rede]
        B --> D[ISPs de Acesso]
        D --> E[IXP: Ponto de Troca de Tráfego]
        E --> F[ISPs de Nível Superior / Backbone]
    end

    style Borda_da_Rede fill:#f9f,stroke:#333,stroke-width:2px
    style Nucleo_da_Rede fill:#bbf,stroke:#333,stroke-width:2px
```

### Explicação Teórica Direta (Definições de Limites)

1.  **Sistemas Finais (Hosts):** São os dispositivos que nós usamos (computadores, celulares). Eles ficam na "borda" porque são o ponto inicial ou final de qualquer dado.
2.  **Redes de Acesso:** É o caminho físico que liga o seu dispositivo ao primeiro roteador do seu provedor (ISP). 
    *   **Residenciais:** Conexões domésticas.
    *   **Institucionais:** Redes de empresas ou universidades.
3.  **Meios Físicos:** 
    *   **Guiados:** O sinal viaja dentro de um sólido (fio de cobre ou vidro da fibra).
    *   **Não Guiados:** O sinal viaja pelo ar (wireless).
4.  **Núcleo da Rede:** É a "malha" de roteadores que interconectam as redes de acesso em todo o mundo.
5.  **ISP (Internet Service Provider):** É a empresa (ex: Vivo, Claro) que te fornece acesso. Elas são organizadas em hierarquia (locais se conectam a regionais, que se conectam a globais).
6.  **IXP (Internet Exchange Point):** É um local físico onde diferentes ISPs se encontram para trocar dados diretamente entre si, tornando o tráfego mais rápido e barato.

---
*Organizado por Gemini CLI*
