from faker import Faker
from connect import get_connection
import random

conn = get_connection()
cursor = conn.cursor()

faker = Faker('pt-BR')

cursor.execute("SELECT id_processo, data_inicio FROM processo;")
processos = cursor.fetchall()

tipos_evento = ['Audieência', 'Perícia', 'Sentença', 'Despacho', 'Acordo', 'Juntada']

mov_ids = []


for id_processo, data_inicio in processos:
    num_eventos = random.randint(1,5)

    for _ in range(num_eventos):
        tipo_evento = random.choice(tipos_evento)
        custo_evento = round(random.uniform(500, 100000),2)
        data_evento = faker.date_between(start_date=data_inicio, end_date='today')
        descricao = faker.sentence(nb_words=8)

        cursor.execute("""
            INSERT INTO movimentacao (id_processo, data_evento, tipo_evento, descricao, custo_evento)
            VALUES(%s, %s, %s, %s, %s)
            RETURNING id_mov;
        """, (id_processo, data_evento, tipo_evento, descricao, custo_evento))

        mov_ids.append(cursor.fetchone()[0])

conn.commit()
cursor.close()
conn.close()

print(f"{len(mov_ids)} movimentações inseridas com sucesso.")
