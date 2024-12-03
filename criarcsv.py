import csv
from datetime import datetime

transacoes = [
    {'data': '01/01/2023', 'descricao': 'Venda de produto A', 'valor': 30000},
    {'data': '02/01/2023', 'descricao': 'Compra de material B', 'valor': -500},
    {'data': '03/01/2023', 'descricao': 'Serviço prestado C', 'valor': 2000},
    {'data': '04/01/2023', 'descricao': 'Despesa com transporte', 'valor': -300},
    {'data': '05/01/2023', 'descricao': 'Venda de produto D', 'valor': 15000},
    {'data': '06/01/2023', 'descricao': 'Compra de material E', 'valor': -700},
    {'data': '07/01/2023', 'descricao': 'Serviço prestado F', 'valor': 2500},
    {'data': '08/01/2023', 'descricao': 'Despesa com marketing', 'valor': -1200},
    {'data': '09/01/2023', 'descricao': 'Venda de produto G', 'valor': 18000},
    {'data': '10/01/2023', 'descricao': 'Compra de material H', 'valor': -800},
]

agora = datetime.now()
#nome_arquivo = agora.strftime("%d-%m-%Y") + "-Relatorio-Contabil.csv"
nome_arquivo = "Relatorio-Contabil.csv"

valor_total = sum(transacao['valor'] for transacao in transacoes)

with open(nome_arquivo, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['data', 'descricao', 'valor'])
    writer.writeheader()
    for transacao in transacoes:
        writer.writerow(transacao)
    writer.writerow({'data': '', 'descricao': 'Total', 'valor': valor_total})


with open(nome_arquivo, mode='r') as file:
    reader = csv.reader(file)
    linha_count = sum(1 for row in reader)

print(f"O arquivo {nome_arquivo} contém {linha_count - 1} transações financeiras.") 
