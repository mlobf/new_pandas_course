import os
from datetime import datetime
from tkinter import W


EMPRESAS = ['nat', 'tbs', 'avn']
PAISES = ['br', 'ar', 'pe', 'ch', 'co']
ARQUIVOS = ['links.csv', 'input_crm', 'input_hub', 'output_hub', 'output_crm']
TIPO_ARQUIVOS = ['csv']


path = os.path.dirname(os.path.abspath(__file__))
path_files = os.listdir(path + '/arquivos')


def check_empresa(_):
    if _[:3] in EMPRESAS:
        # print('E da empresa Natura!')
        pass
    else:
        print('Empresa nao cadastrada')


def check_pais(_):
    if _[4:6] in PAISES:
        # print('E do pais operado ' + _[4:6])
        pass


def check_nome_arquivo(_):
    # print(_[7:16])
    if _[7:16] in ARQUIVOS:
        pass
    else:
        print('Este cara aqui nao esta na lista de arquivos-> ' + _)


def check_data_formato(_):
    # Separar a data na str
    # print(_[-12:-4])  # Toda a data
    # So pode valer para os tipo csvs
    try:
        # Validar o input da data
        int(_[-12:-4])
        # Ano
        print((datetime.today()).year)
        _[-12:-8] in range(2021, 2029) == True
        # Mês
        _[-8:-6] in range(1, 12) == True
        # Dia
        _[-6:-4] in range(1, 31) == True

    except Exception:
        print('Deu ruim data formato -> ' + _)


def check_csv(_):
    # print(_[-3:])
    if _[-3:] in TIPO_ARQUIVOS:
        pass
    else:
        print('Este cara aqui tipo csv-> ' + _)


def check_path_files(files: list = []) -> str:
    for _ in files:
        print('----------------------')
        # check_empresa(_)
        # check_pais(_)
        check_nome_arquivo(_)
        check_data_formato(_)
        check_csv(_)
        print(' ')


# check_path_files(path_files)
"""
for y in range(1, 12):
    print(y)

"""
print(type((datetime.today()).year))
print(type((datetime.today()).year))
print(type((datetime.today()).year))
print(type((datetime.today()).year))
