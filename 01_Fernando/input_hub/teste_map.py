import os
from re import A
from chardet import UniversalDetector
from datetime import datetime
import logging
import pandas as pb

# Global
EMPRESAS = ['nat', 'tbs', 'avn']
PAISES = ['br', 'ar', 'pe', 'ch', 'co']
ARQUIVOS = ['links.csv', 'input_crm', 'input_hub', 'output_hub', 'output_crm']
TIPO_ARQUIVOS = ['csv']
PD = pb

# ------------------------------------------------------------


def detect_encoding(filename):

    detector = UniversalDetector()
    with open(f, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        result = detector.result
        print('Encoding: ' + str(result['encoding']) + '\n')


# ------------------------------------------------------------
"""
    to do:

        Ver a lib de log python,
                => validar se pode ser essa aqui logging.

                Tutorial https://realpython.com/python-logging/


            -nome do bucket
            ok - nome das variaveis
            ok - data da ocorrencia

        to do :

            - Checar se alinks esta preechida.
            - Checar se input_crm esta preechida.
            - checar se o total de columas do input_hub
            - é igual ao numero de colunas de output_hub

            ok - Validar estrutura do arquivo empresa + pais + processo

            - Validar as nas planihas links e input_crm,
                ser as colunas possuem os nomes - pre definidos - e nao possuem columas em branco.

        done:
            - Realizar o import das planilhas.
            - Validação por nome da empresa.
            - Validação por nome do pais.
            - Validação por tipo de arquivo.
            - Validação por tipo de formatação de data.

"""

path = os.path.dirname(os.path.abspath(__file__))
path_files = os.listdir(path + '/arquivos')
p = path + '/arquivos/nat_br_inputhub_CPC7_20210925.csv'
# print(p)

# Inicio dos


def check_empresa(_):
    if _[:3] in EMPRESAS:
        # print('E da empresa Natura!')
        pass
    else:
        print('Empresa nao cadastrada ' + _)


def check_pais(_):
    if _[4:6] in PAISES:
        print('E do pais operado ' + _[4:6])


def check_nome_arquivo(_):
    # print(_[7:16])
    if _[7:16] in ARQUIVOS:
        pass
    else:
        print('Este cara aqui nao esta na lista de arquivos-> ' + _)


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
        print('Deu ruim Data formato -> ' + _)


def check_csv(_):
    # print(_[-3:])
    if _[-3:] in TIPO_ARQUIVOS:
        pass
    else:
        print('Este cara aqui tipo csv-> ' + _)


# Falta Fazer:
#
#    - checar se o total de columas do input_hub
#    - é igual ao numero de colunas de output_hub


def check_n_col_inpuHub_outputHub():
    import pandas as pd
    # path = os.path.dirname(os.path.abspath(__file__))
    # path_files = os.listdir(path + '/arquivos')
    # p = path + '/arquivos/nat_br_inputhub_CPC7_20210925.csv'
    # p = 'heart.csv'  # Esta ok esta aqui
    p = 'nat_br_input_hub_CPC7_20210925.csv'
    # p = 'nat_br_input_crm_20191005 .csv'  # Este aqui esta ok !!

    try:
        df = pd.read_csv(p, encoding="utf-16", sep=";")
        print(df)
    except:
        df = pd.read_csv(p, encoding="ISO-8859-1", sep=";")
        print(df)
        # df = pd.read_csv(p, encoding="utf-16", sep=";")
    # O problema foi o encoding
    # df = pd.read_csv(p, encoding="utf-16", sep=";")
    # sep=';', index=False, encoding='utf-16')
    # df = pd.read_csv(p, sep=";")


# def read_file(file_name='nat_br_input_hub_CPC7_20210925.csv'):


def check_csv_null(file_name):
    import pandas as pd
    import chardet

    #df = pd.read_csv(file_name, encoding="ISO-8859-1", sep=";")

    # use characterbit
    df = pd.read_csv(file_name, encoding="utf-16", sep=";")

    chardet.UniversalDetector()

    #df = pd.read_csv(file_name, encoding="ISO-8859-1", sep=";")

    #df = df.isnull()
    # print(df.count(True))
    # print(df.size)
    print(df)
    # df.value_counts()

    # print(df[df == "Taz"])


def read_file(file_name):
    import pandas as pd
    # path = os.path.dirname(os.path.abspath(__file__))
    # path_files = os.listdir(path + '/arquivos')
    # p = path + '/arquivos/nat_br_inputhub_CPC7_20210925.csv'
    # file_name = 'heart.csv'  # Esta ok esta aqui
    # p = 'nat_br_input_crm_20191005 .csv'  # Este aqui esta ok !!
    # p = 'nat_br_input_hub_CPC7_20210925.csv'
    # To check the files's encoding and
    #   respective error handling

    """
        Sugestao do Douglas => chardet

        Primeiro ver se o csv é realmente null.
            Para tanto eu tenho que validar se a quantidade de Null que
                aparecera na planilha no tipo utc,  sera maior que not null em cada tipo de utc
                Se o resultado for null para os tipos de utcs, entao a planilha é realmente null
    """

    try:
        df = pd.read_csv(file_name, encoding="ISO-8859-1", sep=";")
    except:
        print('Deu ruim')
        pass
        # df = pd.read_csv(file_name, encoding="ISO-8859-1", sep=";")

        '''

        try:
            df = pd.read_csv(file_name, encoding="ISO-8859-1", sep=";")
        except:
            pass
            # df = pd.read_csv(file_name, encoding="utf-16", sep=";")

        '''

    else:
        return df

    # assert(pd.read_csv(p, encoding="ISO-8859-1", sep=";"))
    # df=pd.read_csv(p, encoding="ISO-8859-1", sep=";")
    # print(df)
    # df = pd.read_csv(p, encoding="utf-16", sep=";")
    # print(df)
    # O problema foi o encoding
    # df = pd.read_csv(p, encoding="utf-16", sep=";")
    # sep=';', index=False, encoding='utf-16')
    # df = pd.read_csv(p, sep=";")


def checkColInpOutHubLen():
    p1 = 'nat_br_input_hub_CPC7_20210925.csv'
    p2 = 'nat_br_input_crm_20191005.csv'
    # nat_br_input_crm_20191005 .csv
    print(read_file(p2))
    # print(p2)

    '''
    try:
        df = pd.read_csv(p, encoding="utf-16", sep=";")
    except:
        df = pd.read_csv(p, encoding="utf-16", sep=";")
        # df = pd.read_csv(p, encoding="ISO-8859-1", sep=";")

    try:
        df = pd.read_csv(p, encoding="utf-16", sep=";")
    except:
        df = pd.read_csv(p, encoding="ISO-8859-1", sep=";")

    print(len(df.columns))
    '''

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


# check_path_files(path_files)

# check_n_col_inpuHub_outputHub2()
# check_equal_col_inpOutHub()
# checkColInpOutHubLen()
# f = 'nat_br_input_crm_20191005 .csv'


# Esta lendo

f = 'nat_br_input_crm_20191005 .csv'

#f = 'nat_br_input_hub_CPC7_20210925.csv'

# print(check_csv_null(f))

# print(read_file(f))
detect_encoding(f)
