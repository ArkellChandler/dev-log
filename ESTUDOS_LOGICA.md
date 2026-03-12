# 🧠 Estudos de Lógica de Programação - Bootcamp TOTVS

Este documento contém a representação visual da lógica dos sistemas desenvolvidos neste repositório.

---

## 1. Verificador de Força de Senha 🛡️
Este fluxo mostra como o programa analisa cada critério para dar uma nota à senha.

```mermaid
graph TD
    Start([Início]) --> Input[/Usuário digita a senha/]
    Input --> Score[Definir Score = 0]
    
    Score --> Crit1{Tamanho >= 8?}
    Crit1 -- Sim --> S1[Score + 1]
    Crit1 -- Não --> Crit2
    S1 --> Crit2{Tem Números?}
    
    Crit2 -- Sim --> S2[Score + 1]
    Crit2 -- Não --> Crit3
    S2 --> Crit3{Tem Maiúsculas?}
    
    Crit3 -- Sim --> S3[Score + 1]
    Crit3 -- Não --> Crit4
    S3 --> Crit4{Tem Especiais?}
    
    Crit4 -- Sim --> S4[Score + 1]
    Crit4 -- Não --> Result
    S4 --> Result[Exibir Nível Baseado no Score]
    Result --> End([Fim])
```

---

## 2. Sistema de Segurança (Dicionários + Funções) 🔑
Como o programa "pensa" ao receber um objeto de usuário e decidir o acesso.

```mermaid
graph TD
    A([Início]) --> B[Criar Dicionário: usuario, nivel]
    B --> C[[Chamar Função: checar_acesso]]
    C --> D{Nível >= 5?}
    D -- Sim --> E[Retornar 'Acesso Concedido']
    D -- Não --> F[Retornar 'Acesso Negado']
    E --> G[Exibir Mensagem na Tela]
    F --> G
    G --> H([Fim])
```

---

## 3. Gerenciador de Tarefas (CRUD + Persistência JSON) 📝
O ciclo completo de como os dados saem do HD, são editados e voltam para o HD.

```mermaid
graph STR
    Start([Abrir Programa]) --> Load[Carregar tarefas.json]
    Load --> Menu{Escolha uma Opção}
    
    Menu -- 1. Adicionar --> Add[Pedir Nome -> Adicionar na Lista]
    Add --> Save[Salvar tarefas.json]
    Save --> Menu
    
    Menu -- 2. Listar --> List[Loop FOR: Mostrar Tabela]
    List --> Menu
    
    Menu -- 3. Concluir --> Comp[Pedir ID -> Mudar Status]
    Comp --> Save
    
    Menu -- 4. Remover --> Rem[Pedir ID -> Remover da Lista]
    Rem --> Save
    
    Menu -- 5. Sair --> End([Fechar Programa])
```

---

### 💡 Dica de Estudo:
Tente olhar para esses desenhos e imaginar qual linha de código em Python representa cada "caixinha" do fluxograma. Isso vai te ajudar a "ler" algoritmos no futuro de forma muito mais rápida!
