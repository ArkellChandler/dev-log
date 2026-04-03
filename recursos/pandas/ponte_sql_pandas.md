# Integração: Teoria dos Conjuntos (SQL e Pandas)

O SQL e o Pandas são baseados em operações matemáticas entre conjuntos de dados. Entender um ajuda a dominar o outro.

## 01. Operações de Conjunto

```mermaid
graph TD
    subgraph Operacoes_SQL
        A[Tabela A] --- B[Tabela B]
        A ---|INNER JOIN| AB[Intersecção: A ∩ B]
        A ---|LEFT JOIN| AL[A + Parte de B]
        A ---|UNION| AU[União Total: A ∪ B]
    end

    subgraph Operacoes_Pandas
        df1[DataFrame 1] --- df2[DataFrame 2]
        df1 ---|pd.merge| dfM[Resultado Unificado]
    end
```

### Glossário Técnico de Conjuntos:

1.  **Intersecção (INNER JOIN):** Retorna apenas o que as duas fontes têm em comum. No Pandas: `pd.merge(how='inner')`.
2.  **Diferença (LEFT JOIN com Filtro):** Retorna o que existe em A mas não existe em B. No Pandas: `pd.merge(how='left')`.
3.  **União (UNION):** Combina dois conjuntos verticalmente. No Pandas: `pd.concat()`.

---
