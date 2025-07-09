from faker import Faker
from connect import get_connection
import random

conn = get_connection()
cursor = conn.cursor()

faker = Faker('pt-BR')

cursor.execute("SELECT id_cliente FROM cliente;")
clientes_ids = [row[0] for row in cursor.fetchall()]

processos_ids = []

tipos_acao = ['Cobrança', 'Revisão Contratual', 'Execução Fiscal', 'Defesa Trabalhista']
resultados = ['Em andamento', 'Concluído', 'Arquivado', 'Perdido']
status_ids = [1, 2, 3, 4]

for _ in range(100):
    id_cliente = random.choice(clientes_ids)
    tipo_acao = random.choice(tipos_acao)
    resultado = random.choice(resultados)
    valor_acao = round(random.uniform(1000, 100000),2)
    id_status = random.choice(status_ids)
    data_inicio = faker.date_between(start_date='-2y', end_date='today')
    data_fim = faker.date_between(start_date=data_inicio, end_date='today') if resultado != 'Em Andamento' else None

    cursor.execute("""
        INSERT INTO processo (id_cliente, tipo_acao, resultado, valor_acao, id_status, data_inicio, data_fim)
        VALUES (%s, %s, %s, %s, %s, %s,%s)
        RETURNING id_processo;
    """, (id_cliente, tipo_acao, resultado, valor_acao, id_status, data_inicio, data_fim))

    id_processo = cursor.fetchone()[0]
    processos_ids.append(id_processo)

conn.commit()
cursor.close()
conn.close()

print(f"{len(processos_ids)} processos inseridos com sucesso.")

