# 📖 Instruções de Configuração e Uso - Abstergo Cloud

Este guia orienta a configuração do ambiente local para gerenciar a infraestrutura da Abstergo Farmacêutica via Terraform e PowerShell.

---

## 1. Clonando o Repositório

Para obter uma cópia local do projeto, execute o comando abaixo no terminal:

```powershell
git clone https://github.com/ArkellChandler/dev-log.git
cd dev-log/excel/projeto-abstergo-cloud
```

---

## 2. Configuração de Credenciais (Login)

### AWS (Amazon Web Services)
Para que o Terraform consiga criar recursos na sua conta AWS, você deve configurar suas credenciais no PowerShell:

1. Instale o AWS CLI.
2. Execute o comando de configuração:
   ```powershell
   aws configure
   ```
3. Insira sua `AWS Access Key ID`, `AWS Secret Access Key` e a região padrão (`us-east-1`).

### Google Cloud (GCP) - Opcional
Caso precise interagir com recursos do Google Cloud:
1. Instale o Google Cloud SDK.
2. Autentique-se via navegador:
   ```powershell
   gcloud auth application-default login
   ```

---

## 3. Comandos do Terraform

Navegue até a pasta onde o arquivo `main.tf` está localizado (`/laboratorio`) e execute os comandos na ordem abaixo:

### A. Inicialização
Prepara o diretório, baixa os provedores (AWS) e inicializa os módulos:
```powershell
terraform init
```

### B. Planejamento (Dry Run)
Exibe uma prévia de quais recursos serão criados, alterados ou destruídos sem aplicar as mudanças:
```powershell
terraform plan
```

### C. Aplicação
Executa as mudanças na nuvem AWS. **Atenção:** Este comando pode gerar custos reais:
```powershell
terraform apply
```
*Digite `yes` quando solicitado para confirmar a execução.*

### D. Destruição (Limpeza)
Para remover todos os recursos criados e evitar custos desnecessários após os testes:
```powershell
terraform destroy
```

---
*Nota: Certifique-se de que o binário do `terraform` está adicionado ao PATH do seu sistema Windows.*
