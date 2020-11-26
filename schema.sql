DROP TABLE regiao CASCADE;
DROP TABLE concelho CASCADE;
DROP TABLE instituicao CASCADE;
DROP TABLE medico CASCADE;
DROP TABLE consulta CASCADE;
DROP TABLE prescricao CASCADE;
DROP TABLE analise CASCADE;
DROP TABLE venda_farmacia CASCADE;
DROP TABLE prescricao_venda CASCADE;

CREATE TABLE regiao
    (num_regiao NUMERIC(1, 0) NOT NULL UNIQUE,
    nome VARCHAR(80) NOT NULL CONSTRAINT nomes_regiao CHECK (nome IN ('Norte', 'Centro', 'Lisboa', 'Alentejo', 'Algarve')),
    num_habitantes NUMERIC(10,0),
    CONSTRAINT pk_num_regiao PRIMARY KEY(num_regiao));

CREATE TABLE concelho
    (num_concelho NUMERIC(10, 0) NOT NULL UNIQUE,
    num_regiao NUMERIC(1, 0) NOT NULL,
    nome VARCHAR(80) CONSTRAINT nomes_concelho CHECK (nome IN('Agueda', 'Albergaria-a-Velha', 'Anadia', 'Arouca', 'Aveiro', 'Castelo de Paiva', 'Espinho', 'Estarreja', 'ilhavo', 'Mealhada', 'Murtosa', 'Oliveira de Azemeis', 'Oliveira do Bairro', 'Ovar', 'Santa Maria da Feira', 'Sao Joao da Madeira', 'Sever do Vouga', 'Vagos', 'Vale de Cambra', 'Aljustrel', 'Almodovar', 'Alvito', 'Barrancos', 'Beja', 'Castro Verde', 'Cuba', 'Ferreira do Alentejo', 'Mertola', 'Moura', 'Odemira', 'Ourique', 'Serpa', 'Vidigueira', 'Amares', 'Barcelos', 'Braga', 'Cabeceiras de Basto', 'Celorico de Basto', 'Esposende', 'Fafe', 'Guimaraes', 'Povoa de Lanhoso', 'Terras de Bouro', 'Vieira do Minho', 'Vila Nova de Famalicao', 'Vila Verde', 'Vizela', 'Alfandega da Fe', 'Braganca', 'Carrazeda de Ansiaes', 'Freixo de Espada a Cinta', 'Macedo de Cavaleiros', 'Miranda do Douro', 'Mirandela', 'Mogadouro', 'Torre de Moncorvo', 'Vila Flor', 'Vimioso', 'Vinhais', 'Belmonte', 'Castelo Branco', 'Covilha', 'Fundao', 'Idanha-a-Nova', 'Oleiros', 'Penamacor', 'Proenca-a-Nova', 'Serta', 'Vila de Rei', 'Vila Velha de Rodao', 'Arganil', 'Cantanhede', 'Coimbra', 'Condeixa-a-Nova', 'Figueira da Foz', 'Gois', 'Lousa', 'Mira', 'Miranda do Corvo', 'Montemor-o-Velho', 'Oliveira do Hospital', 'Pampilhosa da Serra', 'Penacova', 'Penela', 'Soure', 'TAbua', 'Vila Nova de Poiares', 'Alandroal', 'Arraiolos', 'Borba', 'Estremoz', 'Evora', 'Montemor-o-Novo', 'Mora', 'Mourao', 'Portel', 'Redondo', 'Reguengos de Monsaraz', 'Vendas Novas', 'Viana do Alentejo', 'Vila Vicosa', 'Albufeira', 'Alcoutim', 'Aljezur', 'Castro Marim', 'Faro', 'Lagoa', 'Lagos', 'Loule', 'Monchique', 'Olhao', 'Portimao', 'Sao Bras de Alportel', 'Silves', 'Tavira', 'Vila do Bispo', 'Vila Real de Santo Antonio', 'Aguiar da Beira', 'Almeida', 'Celorico da Beira', 'Figueira de Castelo Rodrigo', 'Fornos de Algodres', 'Gouveia', 'Guarda', 'Manteigas', 'Mêda', 'Pinhel', 'Sabugal', 'Seia', 'Trancoso', 'Vila Nova de Foz Coa', 'Alcobaca', 'AlvaiAzere', 'Ansiao', 'Batalha', 'Bombarral', 'Caldas da Rainha', 'Castanheira de Pêra', 'Figueiro dos Vinhos', 'Leiria', 'Marinha Grande', 'Nazare', 'Obidos', 'Pedrogao Grande', 'Peniche', 'Pombal', 'Porto de Mos', 'Alenquer', 'Amadora', 'Arruda dos Vinhos', 'Azambuja', 'Cadaval', 'Cascais', 'Lisboa', 'Loures', 'Lourinha', 'Mafra', 'Odivelas', 'Oeiras', 'Sintra', 'Sobral de Monte Agraco', 'Torres Vedras', 'Vila Franca de Xira', 'Alter do Chao', 'Arronches', 'Avis', 'Campo Maior', 'Castelo de Vide', 'Crato', 'Elvas', 'Fronteira', 'Gaviao', 'Marvao', 'Monforte', 'Nisa', 'Ponte de Sor', 'Portalegre', 'Sousel', 'Amarante', 'Baiao', 'Felgueiras', 'Gondomar', 'Lousada', 'Maia', 'Marco de Canaveses', 'Matosinhos', 'Pacos de Ferreira', 'Paredes', 'Penafiel', 'Porto', 'Povoa de Varzim', 'Santo Tirso', 'Trofa', 'Valongo', 'Vila do Conde', 'Vila Nova de Gaia', 'Abrantes', 'Alcanena', 'Almeirim', 'Alpiarca', 'Benavente', 'Cartaxo', 'Chamusca', 'Constancia', 'Coruche', 'Entroncamento', 'Ferreira do Zêzere', 'Golega', 'Macao', 'Ourem', 'Rio Maior', 'Salvaterra de Magos', 'Santarem', 'Sardoal', 'Tomar', 'Torres Novas', 'Vila Nova da Barquinha', 'Alcacer do Sal', 'Alcochete', 'Almada', 'Barreiro', 'Grandola', 'Moita', 'Montijo', 'Palmela', 'Santiago do Cacem', 'Seixal', 'Sesimbra', 'Setubal', 'Sines', 'Arcos de Valdevez', 'Caminha', 'Melgaco', 'Moncao', 'Paredes de Coura', 'Ponte da Barca', 'Ponte de Lima', 'Valenca', 'Viana do Castelo', 'Vila Nova de Cerveira', 'Alijo', 'Boticas', 'Chaves', 'Mesao Frio', 'Mondim de Basto', 'Montalegre', 'Murca', 'Peso da Regua', 'Ribeira de Pena', 'Sabrosa', 'Santa Marta de Penaguiao', 'Valpacos', 'Vila Pouca de Aguiar', 'Vila Pouca de Aguiar', 'Vila Real', 'Armamar', 'Carregal do Sal', 'Castro Daire', 'Cinfaes', 'Lamego', 'Mangualde', 'Moimenta da Beira', 'Mortagua', 'Nelas', 'Oliveira de Frades', 'Penalva do Castelo', 'Penedono', 'Resende', 'Santa Comba Dao', 'Sao Joao da Pesqueira', 'Sao Pedro do Sul', 'Satao', 'Sernancelhe', 'Tabuaco', 'Tarouca', 'Tondela', 'Vila Nova de Paiva', 'Viseu', 'Vouzela')),
    num_habitantes NUMERIC(10,0),	
    CONSTRAINT pk_concelho PRIMARY KEY(num_concelho, num_regiao),
    CONSTRAINT fk_num_regiao FOREIGN KEY(num_regiao) REFERENCES regiao(num_regiao) ON DELETE CASCADE);
	
CREATE TABLE instituicao
    (nome VARCHAR(80) NOT NULL UNIQUE,
    tipo VARCHAR(80) NOT NULL CONSTRAINT tipo_instituicao CHECK (tipo IN('farmacia', 'laboratorio', 'clinica', 'hospital')),
    num_regiao NUMERIC(1, 0),
    num_concelho NUMERIC(10, 0),
    CONSTRAINT pk_nome PRIMARY KEY(nome),
    CONSTRAINT fk_num_regiao FOREIGN KEY(num_regiao) REFERENCES regiao(num_regiao) ON DELETE CASCADE,
    CONSTRAINT fk_num_concelho FOREIGN KEY(num_concelho) REFERENCES concelho(num_concelho) ON DELETE CASCADE);

CREATE TABLE medico
    (num_cedula NUMERIC(10, 0) NOT NULL UNIQUE,
    nome VARCHAR(255),
    especialidade VARCHAR(80),
    CONSTRAINT pk_num_cedula PRIMARY KEY(num_cedula));

CREATE TABLE consulta
    (num_cedula NUMERIC(10, 0) NOT NULL,
    num_doente NUMERIC(10, 0) NOT NULL,
    data_consulta DATE NOT NULL CONSTRAINT data_fds CHECK(EXTRACT(DOW FROM data_consulta) NOT IN(0, 6)),
    nome_instituicao VARCHAR(80),
    CONSTRAINT pk_consulta PRIMARY KEY(num_cedula, num_doente, data_consulta),
    CONSTRAINT fk_num_cedula FOREIGN KEY(num_cedula) REFERENCES medico(num_cedula) ON DELETE CASCADE,
    CONSTRAINT fk_nome_instituicao FOREIGN KEY(nome_instituicao) REFERENCES instituicao(nome) ON DELETE CASCADE,
	CONSTRAINT ri_consulta UNIQUE(num_doente, data_consulta, nome_instituicao));

CREATE TABLE prescricao
	(num_cedula NUMERIC(10, 0) NOT NULL,
	num_doente NUMERIC(10, 0) NOT NULL,
	data_consulta DATE NOT NULL,
	substancia VARCHAR(80) NOT NULL,
	quant NUMERIC(10, 0),
	CONSTRAINT pk_prescricao PRIMARY KEY(num_cedula, num_doente, data_consulta, substancia),
	CONSTRAINT fk_consulta FOREIGN KEY(num_cedula, num_doente, data_consulta) REFERENCES consulta(num_cedula, num_doente, data_consulta) ON DELETE CASCADE);

CREATE TABLE analise
	(num_analise NUMERIC(10, 0) NOT NULL, 
	especialidade VARCHAR(80) NOT NULL,
	num_cedula NUMERIC(10, 0),
	num_doente NUMERIC(10, 0),
	data_consulta DATE,
	data_registo DATE NOT NULL,
	nome VARCHAR(80) NOT NULL,
	quant NUMERIC(3, 0) NOT NULL,
	inst VARCHAR(80) NOT NULL,
	CONSTRAINT pk_analise PRIMARY KEY(num_analise),
	CONSTRAINT fk_consulta FOREIGN KEY(num_cedula, num_doente, data_consulta) REFERENCES consulta(num_cedula, num_doente, data_consulta) ON DELETE CASCADE,
	CONSTRAINT fk_instituicao FOREIGN KEY(inst) REFERENCES instituicao(nome) ON DELETE CASCADE
	/* RI-analise: a consulta associada pode estar omissa; não estando, a especialidade da consulta tem de ser igual à do médico. */
);

CREATE TABLE venda_farmacia
	(num_venda NUMERIC(10, 0) NOT NULL,
	data_registo DATE NOT NULL,
	substancia VARCHAR(80),
	quant NUMERIC(10, 0) NOT NULL,
	preco NUMERIC(5, 2) NOT NULL,
	inst VARCHAR(80) NOT NULL,
	CONSTRAINT pk_venda_farmacia PRIMARY KEY(num_venda),
	CONSTRAINT fk_instituicao FOREIGN KEY(inst) REFERENCES instituicao(nome) ON DELETE CASCADE);

CREATE TABLE prescricao_venda
	(num_cedula NUMERIC(10, 0) NOT NULL,
	num_doente NUMERIC(10, 0) NOT NULL,
	data_consulta DATE NOT NULL,
	substancia VARCHAR(80) NOT NULL,
	num_venda NUMERIC(10, 0) NOT NULL,
	CONSTRAINT pk_prescricao_venda PRIMARY KEY(num_cedula, num_doente, data_consulta, substancia, num_venda),
	CONSTRAINT fk_num_venda FOREIGN KEY(num_venda) REFERENCES venda_farmacia(num_venda) ON DELETE CASCADE,
	CONSTRAINT fk_prescricao FOREIGN KEY(num_cedula, num_doente, data_consulta, substancia) REFERENCES prescricao(num_cedula, num_doente, data_consulta, substancia) ON DELETE CASCADE);