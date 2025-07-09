CREATE TABLE cliente(
	id_cliente SERIAL NOT NULL,
	nome VARCHAR(100),
	cnpj_cpf VARCHAR(20),
	tipo_empresa VARCHAR(20),
	segmento VARCHAR (50),
	cidade VARCHAR (50),
	uf CHAR(2)
);

ALTER TABLE cliente
	ADD PRIMARY KEY (id_cliente);

CREATE TABLE status_processo (
	id_status SERIAL NOT NULL PRIMARY KEY,
	descricao VARCHAR(30)
);

CREATE TABLE processo (
	id_processo SERIAL NOT NULL PRIMARY KEY,
	id_cliente INT REFERENCES cliente(id_cliente),
	id_status INT REFERENCES status_processo(id_status),
	tipo_acao VARCHAR(50),
	valor_acao NUMERIC(10,2),
	resultado VARCHAR(30),
	data_inicio DATE,
	data_fim DATE NULL
);

CREATE TABLE movimentacao (
	id_mov SERIAL NOT NULL PRIMARY KEY,
	id_processo INT REFERENCES processo(id_processo),
	data_evento DATE,
	tipo_evento VARCHAR(50),
	descricao TEXT,
	custo_evento NUMERIC(10,2)
);