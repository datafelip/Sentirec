USE db_sistemas_recomendacao;

CREATE TABLE IF NOT EXISTS tbl_usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome_usuario VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS tbl_produtos(
	id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(150) NOT NULL,
    categoria VARCHAR(50),
    preco DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS tbl_avaliacoes(
	id_avaliacao INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_produto INT NOT NULL,
    nota INT CHECK (nota BETWEEN 1 AND 5),
    texto TEXT,
    data_avaliacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES tbl_usuarios(id_usuario),
    FOREIGN KEY (id_produto) REFERENCES tbl_produtos(id_produto)
);

CREATE TABLE IF NOT EXISTS tbl_sentimentos(
	id_avaliacao INT NOT NULL,
    sentimento VARCHAR(20),
    polaridade FLOAT,
    subjetividade FLOAT,
    FOREIGN KEY (id_avaliacao) REFERENCES tbl_avaliacoes(id_avaliacao)
);
CREATE TABLE IF NOT EXISTS tbl_recomendacoes (
    id_usuario INT,
    id_produto_recomendado INT,
    score FLOAT,
    PRIMARY KEY (id_usuario, id_produto_recomendado),
    FOREIGN KEY (id_usuario) REFERENCES tbl_usuarios(id_usuario),
    FOREIGN KEY (id_produto_recomendado) REFERENCES tbl_produtos(id_produto)
);




