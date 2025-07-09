from connect import get_connection

conn = get_connection()
cursor = conn.cursor()

status_list = ['Em andamento', 'Concluído', 'Arquivado', 'Perdido']

for status in status_list:
    cursor.execute("INSERT INTO status_processo (descricao) VALUES (%s)", (status,))

conn.commit()
cursor.close()
conn.close()

print(f"{len(status_list)} status inseridos com sucesso.")