Código Python Extrator de Informações de NFes

Este código em Python é projetado para ler arquivos XML de Notas Fiscais Eletrônicas (NFes), extrair informações específicas e salvar esses dados em uma planilha Excel. Abaixo está uma visão geral das principais funcionalidades do script.

Funcionalidades
- Abre e lê arquivos XML de um diretório especificado.
- Utiliza a biblioteca xmltodict para converter o conteúdo XML em um dicionário Python.
- Extrai campos específicos da NFe, como número da nota, empresa emissora e nome do cliente.
- Armazena os dados extraídos em um DataFrame do Pandas.
-  Exporta o DataFrame para um arquivo Excel (NFes.xlsx).
  
Você vai precisar das bibliotecas:
- os: Para operações de sistema, como listar arquivos em diretórios.
- xmltodict: Para conversão de XML para dicionário.
- pandas: Para manipulação e armazenamento de dados.
- json: Para depuração (opcional).
- openpyxl: Para manipulação de arquivos Excel.
