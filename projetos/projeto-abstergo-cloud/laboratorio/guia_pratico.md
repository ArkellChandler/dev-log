# 🧪 Guia Prático: Otimização de Custos Genômicos (Abstergo)

Este guia detalha como configurar a infraestrutura AWS para reduzir em até 90% os custos de processamento de sequenciamento genômico, utilizando computação elástica e armazenamento inteligente.

---

## 1. Amazon EC2 Spot Instances (Economia de ~90% em CPU)

As Instâncias Spot utilizam a capacidade ociosa da AWS. Elas são ideais para o processamento genômico, que pode ser interrompido e reiniciado (Batch Processing).

### Passo a Passo:
1.  **Console AWS:** Acesse `EC2 > Spot Requests > Request Spot Instances`.
2.  **Launch Template:** Crie um template com a AMI (imagem) contendo as ferramentas de sequenciamento.
3.  **Fleet Composition:** Selecione várias famílias de instâncias (ex: `m5.large`, `r5.large`, `c5.large`) para aumentar a disponibilidade da frota.
4.  **Interruption Behavior:** Configure para `Hibernate` ou `Stop`. Como o sequenciamento é longo, o estado da memória será preservado.
5.  **Provisioning:** Defina o preço máximo que a Abstergo está disposta a pagar (geralmente o preço padrão da On-Demand).

---

## 2. S3 Intelligent-Tiering (Automação de Armazenamento)

Dados genômicos brutos são acessados com frequência no início e raramente após o processamento. O Intelligent-Tiering move os arquivos automaticamente entre camadas de custo.

### Passo a Passo:
1.  **Bucket S3:** Acesse o bucket `abstergo-sequenciamento-genomico`.
2.  **Upload:** Ao fazer o upload dos arquivos `.fastq` ou `.bam`, selecione a classe de armazenamento `Intelligent-Tiering`.
3.  **Monitoramento:** 
    - **Frequent Access:** Primeiros 30 dias (Preço padrão).
    - **Infrequent Access:** Após 30 dias sem acesso (Economia de ~40%).
    - **Archive Instant Access:** Após 90 dias sem acesso (Economia de ~68%).
4.  **Configuração de Ciclo de Vida:** Ative o `Deep Archive` para dados com mais de 180 dias que precisam ser guardados por regulação farmacêutica, mas raramente acessados.

---

## 3. Resumo Técnico de Impacto

| Recurso | Estratégia | Impacto Estimado |
| :--- | :--- | :--- |
| **Computação** | EC2 Spot Fleet | -90% no custo por genoma processado |
| **Armazenamento** | S3 Intelligent-Tiering | Redução progressiva sem intervenção manual |
| **Transferência** | CloudFront (CDN) | Menor latência para laboratórios globais |

---
*Documento confidencial: Propriedade da Abstergo Farmacêutica.*
