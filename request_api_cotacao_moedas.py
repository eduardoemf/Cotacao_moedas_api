from datetime import datetime
import pandas as pd
import requests as r
from conexao_sqlserver import cnxn, cursor
import warnings # Biblioteca usada para ocultar os avisos do Executor do Terminal

warnings.filterwarnings('ignore')
warnings.warn('DelftStack')
warnings.warn('Do not show this message')



lista_cotacoes = ['USD-BRL','EUR-BRL','ARS-BRL','GBP-BRL','JPY-BRL','UYU-BRL','PYG-BRL','CLP-BRL', 'BTC-BRL']


lista_df_cotacoes = []

for i in lista_cotacoes:
    url = f"https://economia.awesomeapi.com.br/last/{i}"
    cotacao = r.get(url)
    cotacoes = cotacao.json()
    for resultado in cotacoes:
        nome = cotacoes[resultado]['name']
        hora_coleta_api = cotacoes[resultado]['create_date']
        valor_compra = float(cotacoes[resultado]['bid'])
        valor_venda = float(cotacoes[resultado]['ask'])
        valor_maximo = float(cotacoes[resultado]['high'])
        valor_minimo = float(cotacoes[resultado]['low'])

        lista_itens = [str(datetime.now())[:19], resultado, nome, hora_coleta_api, valor_compra, valor_venda, valor_maximo, valor_minimo]
        lista_df_cotacoes.append(lista_itens)


query = """select 
codigo_cotacao + '|' + hora_disponibilidade_api as 'chave'
from tb_cotacao_moedas_hoje"""

cotacoes_ja_importadas_no_banco = []
consulta_sql = pd.read_sql_query(query, cnxn)
for i in consulta_sql.index:
    cotacoes_ja_importadas_no_banco.append(consulta_sql['chave'][i])


itens_inseridos = []
for item in lista_df_cotacoes:
    chave = str(item[1]) + "|" + str(item[3])
    if chave in cotacoes_ja_importadas_no_banco:
        pass
    else:
        cursor.execute(f"""
        INSERT INTO tb_cotacao_moedas_hoje (importacao, codigo_cotacao, nome, hora_disponibilidade_api, valor_compra, valor_venda, valor_maximo, valor_minimo)
        VALUES ('{item[0]}',
                '{item[1]}',
                '{item[2]}',
                '{item[3]}',
                '{item[4]}',
                '{item[5]}',
                '{item[6]}',
                '{item[7]}'
                ) """)

        cnxn.commit()
        itens_inseridos.append(1)

print(f'Total de cotações atualizadas coletadas e inseridas no banco de dados: {len(itens_inseridos)}')


# cd /home/eduardo/Documentos/GitHub/Cotacao_moedas_api && python3 request_api_cotacao_moedas.py