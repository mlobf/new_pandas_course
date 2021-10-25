import os

EMPRESAS = ['nat', 'tbs', 'avn']
PAISES = ['br', 'ar', 'pe', 'ch', 'co']
ARQUIVOS = ['links', 'input_crm', 'input_hub', 'output_hub', 'output_crm']

"""
    Ir para a pasta onde estao os csv s e validar:
        1-Se é csv / py ;
        2-Se possui a seguinte composição:
            a-nat
            b-br/ar/.....
            c-input_crm/input_hub/output_hub/links
            d-data no formato de ano 2021 + mes 10 + dia 05.
"""

path = os.path.dirname(os.path.abspath(__file__))
path_files = os.listdir(path + '/arquivos')
# print(path_files)

# 1-Se é csv, se é py ou é uma pasta;


def check_csv(files: list = []) -> str:
    for _ in files:
        if _[-3:] == '.py':
            print('E python !')
        elif _[-4:] == '.csv':
            print('E csv!')


# Run
# check_csv(path_files)
"""
2-Se possui a seguinte composição:
    a-nat
    b-br/ar/.....
    c-input_crm/input_hub/output_hub/links
    d-data no formato de ano 2021 + mes 10 + dia 05.
"""

# EMPRESAS = ['nat', 'tbs', 'avn']
# filtred_fruits = filter(lambda fruit: fruit.startswith("a") == True, fruits)


def check_empresa(var):
    if var[:3] in EMPRESAS:
        print('E da empresa Natura!')


def check_pais(var):
    print(var[4:6])
    if var[4:6] in PAISES:
        print('E do pais operado' + var[4:6])


def check_path_files(files: list = []) -> str:
    for _ in files:

        # Checar a Empresa
        #print(" O pais e => ", _[4:6])

        check_empresa(_)
        check_pais(_)

        # check_arquivo(_)
        """
        
        # Checar o Pais
        elif _[4:6] in PAISES:
            print('E do pais operado' + _[4:6])
        # Checar a Arquivo
        elif _[-4:] == '.csv':
            pass
        # Checar a Data
        elif _[-4:] == '.csv':
            pass
        """


check_path_files(path_files)

# print(os.path.splitext(mypath)[0])

# print(mypath)

# print(os.getcwd())  # ok

# print(r)

#file_path = os.path.join(mypath, '/arquivos/')
