from connect import get_connection
from faker import Faker
import random

conn = get_connection()
cursor = conn.cursor()

faker = Faker ('pt-BR')

clientes_ids = []

segmentos = ['comércio', 'serviço', 'tecnologia', 'educação', 'saúde']
tipos_empresa = ['MEI', 'EI', 'LTDA', 'EIRELI']

for _ in range(50):
    nome = faker.name()
    cnpj_cpf = faker.cnpj()
    tipo_empresa = random.choice(tipos_empresa)
    segmento = random.choice(segmentos)
    cidade = faker.city()
    uf = faker.estado_sigla()

    cursor.execute("""
        INSERT INTO cliente (nome, cnpj_cpf, tipo_empresa, segmento, cidade, uf)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_cliente;
        """, (nome, cnpj_cpf, tipo_empresa, segmento, cidade, uf))
    

    id_cliente = cursor.fetchone()
    clientes_ids.append(id_cliente)

conn.commit()
cursor.close()
conn.close()

print(f"{len(clientes_ids)} clientes inseridos com suceso.")
