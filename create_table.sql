CREATE TABLE Pessoa(
    cpf_cnpj VARCHAR(14),
    nome VARCHAR(100) ,
    email VARCHAR(100) ,
    celular VARCHAR(20) ,
    PRIMARY KEY(cpf_cnpj)
);
CREATE TABLE Mensagem(
    id VARCHAR(36),
    data_hora DATE ,
    tipo VARCHAR(5) ,
    situacao INT,
    assunto VARCHAR(100) ,
    conteudo VARCHAR(255) ,
    de VARCHAR(14),
    para VARCHAR(14),
    FOREIGN KEY (de) REFERENCES Pessoa(cpf_cnpj),
    FOREIGN KEY (para) REFERENCES Pessoa(cpf_cnpj),
    PRIMARY KEY(id)
);