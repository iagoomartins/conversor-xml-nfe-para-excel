import os
import xmltodict
import pandas as pd
import json
import openpyxl

# Função para ler informações de um arquivo XML e extrair dados específicos
def ler_informacoes(nome_arquivo, valores):
    print(f'pegou as informações {nome_arquivo}')
    try:
        # Abre o arquivo XML para leitura
        # Inserir o local das NFes aqui
        with open(f'nfes/{nome_arquivo}', 'rb') as arquivo_xml:
            # Converte o conteúdo XML para um dicionário Python
            dicionario_arquivo = xmltodict.parse(arquivo_xml)
            # Imprime o dicionário para depuração
            print(json.dumps(dicionario_arquivo, indent=4))
            # Acessa a seção específica do XML ( Personalize com os campos da NFe de sua preferência )
            if "NFe" in dicionario_arquivo:
                infos_nf = dicionario_arquivo["NFe"]["infNFe"]
            else:
                infos_nf = dicionario_arquivo["nfeProc"]["NFe"]["infNFe"]
            # Exemplos de campos de NFe
            numero_nota = infos_nf["@Id"]
            empresa_emissora = infos_nf['emit']['xNome']
            nome_cliente = infos_nf['dest']['xNome']
            # Adiciona os valores extraídos à lista de valores
            valores.append([numero_nota, empresa_emissora, nome_cliente])
    except Exception as e:
        # Tratamento de erro caso ocorra algum problema ao processar o arquivo
        print(f'Erro ao processar {nome_arquivo}: {e}')
        return None

# Lista todos os arquivos no diretório 'ctes' => mudar para a pasta com as NFes
lista_arquivos = os.listdir('nfes')

# Define as colunas para o DataFrame
colunas = ['Numero da nota', 'Empresa Emissora', 'Nome Cliente']
valores = []
# Itera sobre cada arquivo na lista de arquivos
for arquivo in lista_arquivos:
    ler_informacoes(arquivo, valores) # Chama a função para ler e extrair informações do arquivo


# Cria uma tabela com os dados extraídos
tabela = pd.DataFrame(columns=colunas, data=valores)
# Salva a tabela em uma planilha Excel
tabela.to_excel('NFes.xlsx', index=False)

