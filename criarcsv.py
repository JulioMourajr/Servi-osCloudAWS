import csv
from datetime import datetime

transacoes = [
    {'data': '01/11/2024', 'descricao': 'Venda de notebook', 'valor': 4500},
    {'data': '05/11/2024', 'descricao': 'Compra de suprimentos de escritório', 'valor': -300},
    {'data': '10/11/2024', 'descricao': 'Serviço de consultoria', 'valor': 2000},
    {'data': '15/11/2024', 'descricao': 'Despesa com transporte', 'valor': -150},
    {'data': '20/11/2024', 'descricao': 'Venda de smartphone', 'valor': 3500},
    {'data': '25/11/2024', 'descricao': 'Compra de material de limpeza', 'valor': -200},
    {'data': '30/11/2024', 'descricao': 'Serviço de manutenção', 'valor': 1200},
    {'data': '05/12/2024', 'descricao': 'Despesa com marketing', 'valor': -500},
    {'data': '10/12/2024', 'descricao': 'Venda de tablet', 'valor': 2500},
    {'data': '15/12/2024', 'descricao': 'Compra de software', 'valor': -800},
    {'data': '05/12/2024', 'descricao': 'Salário funcionário', 'valor': -5800},
    {'data': '01/11/2024', 'descricao': 'Venda de PS5', 'valor': 4000},
    {'data': '05/11/2024', 'descricao': 'Compra de suprimentos de escritório', 'valor': -300},
    {'data': '10/11/2024', 'descricao': 'Serviço de consultoria', 'valor': 2000},
    {'data': '15/11/2024', 'descricao': 'Despesa com transporte', 'valor': -150},
    {'data': '20/11/2024', 'descricao': 'Venda de smartphone', 'valor': 3500},
    {'data': '25/11/2024', 'descricao': 'Compra de material de limpeza', 'valor': -200},
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
