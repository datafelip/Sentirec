USE db_sistemas_recomendacao;

INSERT INTO tbl_usuarios (nome_usuario, email) VALUES 
('Felipe Lima', 'felipe@example.com'),
('Ana Souza', 'ana@example.com'),
('Carlos Mendes', 'carlos@example.com');


INSERT INTO tbl_produtos (nome_produto, categoria, preco) VALUES
('Fone de Ouvido Bluetooth', 'Eletrônicos', 199.90),
('Livro - Python para Iniciantes', 'Livros', 59.90),
('Smartwatch Fitness', 'Eletrônicos', 299.90);


INSERT INTO tbl_avaliacoes (id_usuario, id_produto, nota, texto) VALUES
(1, 1, 5, 'Excelente fone! A bateria dura muito e o som é ótimo.'),
(1, 2, 4, 'Livro muito bom, mas achei que poderia ter mais exemplos.'),
(2, 2, 5, 'Simplesmente adorei! Muito didático e direto.'),
(3, 3, 2, 'Esperava mais do produto. A pulseira é desconfortável.'),
(2, 1, 3, 'A qualidade é boa, mas o som não é tão alto quanto imaginei.');

