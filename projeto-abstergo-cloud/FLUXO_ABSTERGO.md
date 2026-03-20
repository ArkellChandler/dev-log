# 📊 Fluxograma de Arquitetura: Abstergo Cloud

Este documento apresenta o fluxo de processamento de dados genômicos da Abstergo Farmacêutica, destacando a integração entre armazenamento inteligente e computação de baixo custo.

---

## 1. Representação Visual (Mermaid)

```mermaid
graph TD
    %% Estilo das caixas
    classDef storage fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef compute fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px;
    classDef savings fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;

    Start[Início: Sequenciamento Genômico] --> Upload[Upload de Arquivos .fastq / .bam]
    
    subgraph "Camada de Armazenamento Otimizada (S3)"
        Upload --> S3[S3 Intelligent-Tiering]
        S3 -->|Acesso Frequente| S3F[Frequent Access - 30 dias]
        S3 -->|Acesso Raro| S3I[Infrequent Access - 90 dias]
        S3 -->|Arquivamento| S3A[Deep Archive - 180 dias]
    end

    subgraph "Camada de Processamento Elástica (EC2)"
        S3F --> Trigger[Disparo de Processamento]
        Trigger --> Spot[EC2 Spot Instance Request]
        Spot -->|Economia de 90%| Worker[Worker Node: Processamento Batch]
        Worker --> Results[Geração de Resultados .vcf]
    end

    Results --> Output[Bucket de Resultados Finais]
    Output --> End[Fim: Relatório para Laboratório]

    %% Aplicando Estilos
    class S3,S3F,S3I,S3A,Output storage;
    class Spot,Worker compute;
    class S3,Spot savings;
```

---

## 2. Base Teórica do Fluxo

### A. Camada de Armazenamento (S3 Intelligent-Tiering)
O fluxo inicia com o upload de grandes volumes de dados brutos (`.fastq`). O uso do **Intelligent-Tiering** é crucial pois:
- **Automação:** Move os dados entre camadas de acesso frequente e raro sem necessidade de intervenção manual.
- **Custo:** Garante que dados de pesquisas antigas não gerem custos elevados, movendo-os para o *Deep Archive* automaticamente após 180 dias.

### B. Camada de Processamento (EC2 Spot Instances)
O processamento genômico é uma carga de trabalho do tipo **Batch** (em lote). 
- **Instâncias Spot:** São ideais aqui porque permitem utilizar o excesso de capacidade da AWS com descontos de até 90%. 
- **Resiliência:** O fluxo prevê que, se uma instância for interrompida, o processo pode ser reiniciado a partir do último checkpoint (arquivos no S3), mantendo a eficiência financeira.

### C. Resultados e Entrega
Os arquivos resultantes (`.vcf` - Variant Call Format) são armazenados em um bucket final para análise dos cientistas, garantindo que o dado processado esteja sempre disponível para a tomada de decisão clínica.
