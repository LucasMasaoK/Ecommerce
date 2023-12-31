-- Inserções para a tabela FORMA_PAGAMENTOS
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (1, 'Dinheiro');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (2, 'Cartão de Crédito');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (3, 'Cartão de Débito');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (4, 'Transferência Bancária');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (5, 'Pix');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (6, 'Boleto Bancário');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (7, 'Cheque');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (8, 'Vale Alimentação');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (9, 'Vale Refeição');
INSERT INTO FORMA_PAGAMENTOS (ID_PAGAMENTO, NOME) VALUES (10, 'Cartão Presente');

-- Inserções para a tabela CLIENTES
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('João Silva', '1990-05-15', '1234567890', 'Rua A, 123');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Maria Oliveira', '1985-08-22', '9876543210', 'Avenida B, 456');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Carlos Rocha', '1978-12-10', '4567890123', 'Travessa C, 789');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Ana Souza', '1995-04-03', '7890123456', 'Rua D, 234');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Luiz Santos', '1980-11-27', '2345678901', 'Avenida E, 567');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Fernanda Lima', '1992-07-18', '9012345678', 'Travessa F, 890');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Ricardo Pereira', '1973-09-05', '3456789012', 'Rua G, 123');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Camila Costa', '1987-02-14', '6789012345', 'Avenida H, 456');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Pedro Almeida', '1998-06-30', '0123456789', 'Travessa I, 789');
INSERT INTO CLIENTES (NOME, DT_NASCIMENTO, CPF, ENDERECO) VALUES ('Beatriz Santos', '1982-10-20', '5432109876', 'Rua J, 234');


-- Inserções para a tabela fornecedor
INSERT INTO fornecedor (nome, cnpj) VALUES ('ElectroTech Inc.', '12345678901234');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Gadget Galaxy Ltda', '56789012345678');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Tech Solutions S.A.', '90123456789012');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Inovação Eletrônica Ltda', '34567890123456');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Global Electronics Corp.', '78901234567890');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Future Devices Inc.', '23456789012345');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Digital Innovations Ltda', '67890123456789');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Smart Technologies S.A.', '01234567890123');
INSERT INTO fornecedor (nome, cnpj) VALUES ('EletroMega Corp.', '45678901234567');
INSERT INTO fornecedor (nome, cnpj) VALUES ('Inovação Digital Ltda', '89012345678901');


-- Inserções para a tabela PRODUTOS com produtos eletrônicos
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (1, 'Smartphone Modelo X', 50, 799.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (2, 'Notebook UltraSlim', 30, 1499.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (3, 'Smart TV 4K', 40, 899.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (1, 'Câmera Digital Profissional', 20, 1299.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (2, 'Fones de Ouvido Bluetooth', 80, 79.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (3, 'Tablet Avançado', 25, 499.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (1, 'Console de Videogame', 60, 349.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (2, 'Monitor Gamer Curvo', 35, 599.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (3, 'Impressora 3D', 15, 899.99);
INSERT INTO PRODUTOS (id_fornecedor, nome, estoque, vl_venda) VALUES (1, 'Robô Aspirador Inteligente', 45, 249.99);

-- Inserções para a tabela FUNCIONARIO
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('João Silva', '1234567890', 'A', '1985-03-15');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Maria Oliveira', '9876543210', 'B', '1990-08-22');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Carlos Rocha', '4567890123', 'A', '1978-12-10');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Ana Souza', '7890123456', 'C', '1995-04-03');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Luiz Santos', '2345678901', 'B', '1980-11-27');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Fernanda Lima', '9012345678', 'A', '1992-07-18');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Ricardo Pereira', '3456789012', 'C', '1973-09-05');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Camila Costa', '6789012345', 'A', '1987-02-14');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Pedro Almeida', '0123456789', 'B', '1998-06-30');
INSERT INTO FUNCIONARIO (NOME, CPF, TIPO, DT_NASCIMENTO) VALUES ('Beatriz Santos', '5432109876', 'C', '1982-10-20');


-- Inserções para a tabela VENDAS
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (1, 1, 1, 1500.00, 100.00, '2023-01-15');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (2, 2, 2, 2500.00, 150.00, '2023-02-20');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (3, 3, 3, 1800.00, 120.00, '2023-03-10');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (4, 1, 1, 1200.00, 80.00, '2023-04-05');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (5, 2, 2, 2200.00, 200.00, '2023-05-15');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (6, 3, 3, 1600.00, 100.00, '2023-06-20');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (7, 1, 1, 2000.00, 150.00, '2023-07-10');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (8, 2, 2, 1400.00, 90.00, '2023-08-05');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (9, 3, 3, 1900.00, 120.00, '2023-09-15');
INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA) VALUES (10, 1, 1, 2100.00, 180.00, '2023-10-20');

--RELATORIO DE VENDAS POR FUNCIONARIO
SELECT V.ID_CLIENTE, V.ID_FUNCIONARIO, V.ID_FORMAPGTO, V.VL_TOTAL, V.DESCONTO, V.DATA_VENDA FROM VENDAS AS V
JOIN FUNCIONARIO AS F ON V.ID_FUNCIONARIO= F.ID_FUNCIONARIO
WHERE F.ID_FUNCIONARIO=1 

SELECT * FROM 

