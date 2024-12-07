### Projeto Final ADA tech Serviços Cloud

## Cenário

A Ada Contabilidade enfrenta um desafio operacional diário: os contadores precisam enviar arquivos manualmente para armazenamento e, em seguida, registrar no banco de dados a quantidade de linhas contidas nesses arquivos. Esse processo manual é ineficiente e propenso a erros.

Será Criada uma solução para automatizar a arquitetura em todo o seu fluxo, se baseando em práticas DevOps para simplificar o fluxo de trabalho e garantir a confiabilidade do processo.

O código vai enviar arquivos de forma automática para um bucket s3 de forma automatizada.

Usar os serviços da AWS, como SNS, SQS, Lambda e DynamoDB, Gravando em um banco de dados o nome do arquivo e o número de linhas.
