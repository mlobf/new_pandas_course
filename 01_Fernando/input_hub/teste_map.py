from cmath import log
import os
from datetime import datetime
import logging

# Global
EMPRESAS = ['nat', 'tbs', 'avn']
PAISES = ['br', 'ar', 'pe', 'ch', 'co']
ARQUIVOS = ['links.csv', 'input_crm', 'input_hub', 'output_hub', 'output_crm']
TIPO_ARQUIVOS = ['csv']

"""
    to do:

        Ver a lib de log python,
                => validar se pode ser essa aqui logging.
                Tutorial https://realpython.com/python-logging/

            -nome do bucket
            ok - nome das variaveis
            ok - data da ocorrencia

        - Checar se alinks esta preechida.
        - Checar se input_crm esta preechida.

        - checar se o total de columas do input_hub
        - é igual ao numero de colunas de output_hub

        ok - Validar estrutura do arquivo empresa + pais + processo


        - Validar as nas planihas links e input_crm,
            ser as colunas possuem os nomes - pre definidos - e nao possuem columas em branco.

        - Baixar as planilhas modelo em uma pasta local para emular o funcionamento do programa,
        - Criar uma estrutura de Diretorios para emular o funcionamento do programa.

"""

path = os.path.dirname(os.path.abspath(__file__))
path_files = os.listdir(path + '/arquivos')


def check_empresa(_):
    if _[:3] in EMPRESAS:
        # print('E da empresa Natura!')
        pass
    else:
        logging.debug(('Empresa nao cadastrada ' + _))


def check_pais(_):
    if _[4:6] in PAISES:
        # print('E do pais operado ' + _[4:6])
        pass


def check_nome_arquivo(_):
    # print(_[7:16])
    if _[7:16] in ARQUIVOS:
        pass
    else:
        logging.debug('Este cara aqui nao esta na lista de arquivos-> ' + _)


def check_data_formato(_):
    # Separar a data na str
    print(_[-12:-4])  # Toda a data
    # So pode valer para os tipo csvs
    try:
        # Validar o input da data
        int(_[-12:-4])
        # Ano
        # print((datetime.today()).year)
        if _[-12:-8] in range((datetime.today().year), 2029) == True:
            pass
        # Mês
        _[-8:-6] in range(1, 12) == True
        # Dia
        _[-6:-4] in range(1, 31) == True

    except Exception:
        # Usar a porcaria da lib de logging
        logging.debug('Deu ruim Data formato -> ' + _)


def check_csv(_):
    # print(_[-3:])
    if _[-3:] in TIPO_ARQUIVOS:
        pass
    else:
        logging.debug('Este cara aqui tipo csv-> ' + _)


# ---------------------------------------------------------------------------------
def check_path_files(files: list = []) -> str:
    for _ in files:
        print('----------------------')
        check_empresa(_)
        check_pais(_)
        check_nome_arquivo(_)
        check_data_formato(_)
        check_csv(_)
        print(' ')


check_path_files(path_files)

"""
for y in range(1, 12):
    print(y)

"""
# print(((datetime.today()).year))
logging.debug((datetime.today()).year)
logging.debug((datetime.today()).year)


# print(((datetime.today()).year))
