# 🏥 Projeto Abstergo Cloud: Relatório de Implementação

Este relatório detalha a transição da infraestrutura física da Abstergo Farmacêutica para a nuvem AWS, com foco em segurança, escalabilidade e otimização de custos.

---

## 1. Visão Geral do Projeto
A Abstergo Farmacêutica migrou seus sistemas críticos de pesquisa laboratorial para a AWS para garantir a integridade dos dados e a disponibilidade global de seus ensaios clínicos.

---

## 2. Arquitetura Implementada
- **Região Principal:** `us-east-1` (N. Virginia) para baixa latência.
- **Alta Disponibilidade:** Deploy em 3 Availability Zones (AZs) distintas.
- **Compute:** Uso de **Amazon EC2** para servidores de aplicação e **AWS Lambda** para processamento de logs sem servidor (Serverless).
- **Storage:** **Amazon S3** para armazenamento de dados brutos de pesquisa com políticas de ciclo de vida (S3 Glacier para arquivamento).

---

## 3. Estratégia de Custos (FinOps)
Na subpasta `/laboratorio`, foram incluídos scripts para automação de custos:
- **Tagging Strategy:** Todos os recursos são tageados por departamento (`Dept: Laboratorio`).
- **Scheduling:** Instâncias de teste são desligadas automaticamente fora do horário comercial (18h - 08h).
- **Alertas de Budget:** Configuração de alarmes de faturamento para evitar surpresas no final do mês.

---

## 4. Próximos Passos
1. Implementação de **AWS CloudFormation** para toda a infraestrutura (IaC).
2. Auditoria de segurança mensal via **AWS Trusted Advisor**.

---
*Relatório gerado em 20 de Março de 2026.*
