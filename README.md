# Pipeline de Dados Econômicos do Brasil
## Problema: Os dados econômicos do Brasil estão espalhados em várias fontes (Banco Central, IBGE, SIDRA) cada uma com formato diferente, atualização diferente, e sem conexão entre elas. 
## O projeto resolve isso criando um pipeline que centraliza, organiza e relaciona essas fontes num único lugar, permitindo análises que nenhuma fonte isolada consegue responder.

## O que vai responder:
- Quando a Selic  (Taxa básica de juros da economia brasileira) sobe, o desemprego aumenta ou diminui?
- Quais estados têm maior renda média e como isso se relaciona com a inflação local?
- Como o dólar se comportou nos períodos de maior desemprego?
- A inflação afeta mais estados com renda baixa ou alta?
- Qual o impacto de crises econômicas (2015, 2020) nos indicadores combinados?

# Arquitetura
BCB API + IBGE API + SIDRA API
          ↓
     Python + requests
          ↓
     AWS S3 (Parquet) ← dados brutos
          ↓
     dbt Core (transformações)
          ↓
     PostgreSQL local (DW)
          ↓
     Power BI ou Streamlit