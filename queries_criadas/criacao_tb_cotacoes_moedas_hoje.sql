use db_projeto_cotacao_online

CREATE TABLE [dbo].[tb_cotacao_moedas_hoje] (
    [hora_extracao]        DATETIME       NOT NULL,
    [codigo_cotacao]       NVARCHAR (7)   NOT NULL,
    [nome_transacao]       NVARCHAR (100) NOT NULL,
    [data_retorno_cotacao] DATETIME       NOT NULL,
    [valor_compra]         DECIMAL (8)    NOT NULL,
    [valor_venda]          DECIMAL (8)    NOT NULL,
    [valor_maximo]         DECIMAL (8)    NOT NULL,
    [valor_minimo]         DECIMAL (8)    NOT NULL,
    CONSTRAINT [PK_tb_cotacao_moedas_hoje] PRIMARY KEY CLUSTERED ([hora_extracao] ASC, [codigo_cotacao] ASC)
);

