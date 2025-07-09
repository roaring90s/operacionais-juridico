# 📊 Finanças Operacionais Jurídicas — Análise para Microempreendedores

Projeto de simulação e análise de custos operacionais de processos jurídicos voltado ao atendimento de microempreendedores. Combina modelagem de dados com **PostgreSQL**, automação com **Python**, visualização com **Power BI**, e uso de **DAX** para extração de insights relevantes.

---

## 🧠 Objetivo

Demonstrar domínio prático em ferramentas de dados aplicadas a um cenário realista de gestão jurídica-financeira, oferecendo indicadores estratégicos para a tomada de decisão em empresas que prestam serviços a microempreendedores.

---

## 🛠️ Tecnologias utilizadas

- **PostgreSQL** — criação do banco e estrutura relacional via SQL
- **Python** (`psycopg2`, `dotenv`) — automação da população do banco com dados simulados
- **Power BI** — construção de dashboard interativo com múltiplas abas
- **DAX** — criação de KPIs e medidas no Power BI

---

## ⚡ Automação com Python

Todos os dados foram gerados e inseridos no banco via scripts Python com as bibliotecas `faker` e `random`, conectando-se ao PostgreSQL por meio da biblioteca `psycopg2`.  
As variáveis de acesso foram protegidas via `.env`.

Cada script insere dados simulados consistentes com o modelo relacional:

- **Clientes**: nomes fictícios e cidades reais do Brasil
- **Status de processo**: Em andamento, Concluído, Arquivado, Perdido
- **Processos**: associados a clientes e status
- **Movimentações**: eventos com descrição, tipo e custo aleatório

---

## 🧾 SQL no projeto

- Usado para a criação direta do banco e tabelas (`CREATE TABLE`, `PRIMARY KEY`, `FOREIGN KEY`)
- Consultas básicas de verificação com `SELECT`, `SUM`, `GROUP BY`
- O restante da lógica analítica foi tratada diretamente no Power BI com **DAX**

---

## 📊 Dashboard Power BI

O relatório foi dividido em **quatro abas principais**, com layout minimalista e foco em insights estratégicos.

---

### 🔹 1. Visão Geral

![visão geral](https://github.com/roaring90s/operacionais-juridico/blob/main/img/VISAO%20GERAL.png)

- Custo Total
- Quantidade de Processos
- Custo por Tipo de Ação
- Distribuição por Status
- Filtro por Cidade
- Evolução dos Custos ao longo dos anos

---

### 🔹 2. Clientes e Processos

![Clientes e Processos](https://github.com/roaring90s/operacionais-juridico/blob/main/img/CLIENTES.png)

- Processos por Cliente
- Custo Total por Cliente
- Custo Médio por Cliente


---

### 🔹 3. Análise de Custos Jurídicos

![Custos Jurídicos](https://github.com/roaring90s/operacionais-juridico/blob/main/img/CUSTOS.png)

- Evolução dos Custos ao longo do tempo
- Custo Médio por Tipo de Evento
- Distribuição de Custo por Ação
- Análise temporal acumulada

---

### 🔹 4. Status & Performance

![Status e Performance](https://github.com/roaring90s/operacionais-juridico/blob/main/img/STATUS.png)

- Processos por Status
- Processos em Aberto (com base no status)
- Tempo Médio de Tramitação

---

## 📌 Como rodar o projeto

1. Configure um banco PostgreSQL local
2. Crie as tabelas com os scripts SQL
3. Insira as credenciais no arquivo `.env`
4. Execute os scripts Python para popular os dados
5. Abra o `.pbix` no Power BI para explorar o dashboard

---

## 👤 Autor

**Marco Sousa**  
Estudante de Análise e Desenvolvimento de Sistemas  
Foco em projetos com dados, TI e automação  
🔗 [https://www.linkedin.com/in/marcos-sousa-616375249/](https://www.linkedin.com/in/marcos-sousa-616375249/)

