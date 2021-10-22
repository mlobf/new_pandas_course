import pandas as pd

"""
	to do:

		Ver a lib de log python, 
                => validar se pode ser essa aqui logging.
                Tutorial https://realpython.com/python-logging/

			-nome do bucket
			-nome das variaveis
			-data da ocorrencia

		Checar se alinks esta preechida.
		Checar se input_crm esta preechida.

		checar se o total de columas do input_hub 
		é igual ao numero de colunas de output_hub

		Validar estrutura do arquivo.
			empresa + pais + processo


		Validar as nas planihas links e input_crm,
			ser as colunas possuem os nomes - pre definidos - e nao possuem columas em branco.
        
        Baixar as planilhas modelo em uma pasta local para emular o funcionamento do programa,
        Criar uma estrutura de Diretorios para emular o funcionamento do programa.




"""

########################################################################################
# trata chegada o evento (object) e cria variáveis para leitura/escrita do dataframe

bucket_name = f"s3://{event['Records'][0]['s3']['bucket']['name']}/"

# Verificar se o prefixo esta indo certo
prefix_event = event['Records'][0]['s3']['object']['key']

file = prefix_event.split('/')[3]
date_proccess = prefix_event.split('.')[0][-8:]

object_links = prefix_event.replace(
    'input_crm', 'links').replace(f'_{date_proccess}', '')
########################################################################################

########################################################################################
# leitura do arquivo input_hub e links

# Falha de leitura do input_crm
try:
    input_crm = pd.read_csv(
        f"{bucket_name}{prefix_event}", encoding="ISO-8859-1", sep=";")
except Exception:
    print("Houve um erro ao ler o arquivo input_crm, favor verificar")

# Falha de leitura do LINKS
try:
    links = pd.read_csv(f"{bucket_name}{object_links}",
                        encoding="ISO-8859-1", sep=";")
except Exception:
    print("Houve um erro ao ler o arquivo link, favor verificar")


########################################################################################

########################################################################################
# padrão do layout para dataframe antes do transpose
column_names = ['Cluster', 'TIPO_ENVIO', 'Data', 'Dia da Semana', 'UTM_CAMPAIGN', 'SUBJECT', 'PRE_HEADER', 'UTM_SOURCE', 'UTM_MEDIUM', 'UTM_TERM', 'UTM_CONTENT', 'Template', 'Ciclo  de Vida', 'Engajamento Abertura', 'Engajamento Clique', 'Primeira Vitrine',
                'Segunda Vitrine', 'Terceira Vitrine', 'CHAMADA_VITRINE_1', 'CHAMADA_VITRINE_2', 'TEXTO_CHAMADA', 'TITULO', 'TEXTO_APOIO', 'ATRIBUTOS', 'TITULO_LINHA', 'CTA', 'LINK_ORIGEM', 'Comentários', 'LOGO_LINK', 'Principal', 'Meio', 'MB1', 'MB2', 'Reengajamento', 'Extra']
########################################################################################

########################################################################################
# regras de criação de campos derivados

# Campo UTM CAMPAING
input_crm["UTM_CAMPAIGN"] = "ncf_bra_email_cco_d_prd_" +\
    input_crm["Cluster"]+'-' +\
    input_crm["Ciclo  de Vida"]+'-'\
    + input_crm["Template"] +\
    '_cliq'+input_crm["Engajamento Cliques"].astype(str)\
    + 'aber'+input_crm["Engajamento Abertura"].astype(str)+'_' +\
    input_crm["Primeira Vitrine"]+'_' +\
    input_crm["Data Arrumada"].astype(str)

# Campos LINK ORIGEM
input_crm["LINK_ORIGEM"] = "https://images.rede.natura.net/html/campanha/" +\
    input_crm["Data Arrumada"].astype(str)+'/' +\
    input_crm["Cluster"]+'_' +\
    input_crm["Ciclo  de Vida"]+'/BANNER_PRINCIPAL.jpg'


cluster = input_crm['Cluster'].unique().tolist()

input_crm["UTM_CONTENT"] = input_crm["Cluster"]
########################################################################################

########################################################################################
# campos fixos
input_crm["UTM_SOURCE"] = "cf_cco"
input_crm["UTM_MEDIUM"] = "news"
input_crm["UTM_TERM"] = "x"
input_crm["LOGO_LINK"] = "www.natura.com.br"
########################################################################################

########################################################################################
# criação do dataframe antes do transpose
data_prep = input_crm[['Cluster', 'Data', 'Dia da Semana', 'UTM_CAMPAIGN', 'UTM_SOURCE', 'UTM_MEDIUM', 'UTM_TERM', 'UTM_CONTENT', 'Template', 'Ciclo  de Vida', 'Engajamento Abertura', 'Engajamento Cliques', 'Primeira Vitrine', 'Segunda Vitrine', 'Terceira Vitrine', 'LINK_ORIGEM', 'Comentários', 'LOGO_LINK', 'Principal', 'Meio', 'MB1', 'MB2', 'Reengajamento', 'Extra']]\
    .reindex(columns=column_names)\
    .rename(columns={'Data': 'DATA_ENVIO', 'Dia da Semana': 'DIA_SEMANA', 'Template': 'TEMPLATE', 'Ciclo  de Vida': 'CICLO_VIDA', 'Engajamento Abertura': 'ENGAJAMENTO_ABERTURA', 'Engajamento Clique': 'ENGAJAMENTO_CLIQUES', 'Primeira Vitrine': 'PRIMEIRA_VITRINE', 'Segunda Vitrine': 'SEGUNDA_VITRINE', 'Terceira Vitrine': 'TERCEIRA_VITRINE', 'Comentários': 'COMENTARIOS'
                     })
########################################################################################

########################################################################################
# transforma colunas Principal, Meio, MB1, MB2, Reengajamento, Extra em linhas do campo
# TIPO_BANNER
transpose = pd.melt(data_prep, id_vars=['Cluster', 'TIPO_ENVIO', 'DATA_ENVIO', 'DIA_SEMANA', 'UTM_CAMPAIGN', 'SUBJECT', 'PRE_HEADER', 'UTM_SOURCE', 'UTM_MEDIUM', 'UTM_TERM', 'UTM_CONTENT', 'TEMPLATE', 'CICLO_VIDA', 'ENGAJAMENTO_ABERTURA', 'ENGAJAMENTO_CLIQUES', 'PRIMEIRA_VITRINE', 'SEGUNDA_VITRINE', 'TERCEIRA_VITRINE', 'CHAMADA_VITRINE_1', 'CHAMADA_VITRINE_2', 'TEXTO_CHAMADA', 'TITULO', 'TEXTO_APOIO', 'ATRIBUTOS', 'TITULO_LINHA', 'CTA', 'LINK_ORIGEM', 'COMENTARIOS', 'LOGO_LINK'],
                    var_name="TIPO_BANNER", value_name="Value")

transpose = transpose.rename(columns={'Value': 'NOME_BANNER'}).sort_values(
    by=['Cluster', 'TIPO_BANNER'], ascending=False)
########################################################################################

########################################################################################
# Ajuste nomenclatura Banner
transpose["TIPO_BANNER"] = transpose['TIPO_BANNER'].replace(
    {'Principal': 'PRINCIPAL'})
transpose["TIPO_BANNER"] = transpose['TIPO_BANNER'].replace({'Meio': 'MEIO'})
transpose["TIPO_BANNER"] = transpose['TIPO_BANNER'].replace({'MB1': 'MINI1'})
transpose["TIPO_BANNER"] = transpose['TIPO_BANNER'].replace({'MB2': 'MINI2'})
transpose["TIPO_BANNER"] = transpose['TIPO_BANNER'].replace(
    {'Reengajamento': 'ENGAJAMENTO'})
transpose["TIPO_BANNER"] = transpose['TIPO_BANNER'].replace({'Extra': 'EXTRA'})
########################################################################################

########################################################################################
# join com tabela de links
join_links = pd.merge(transpose, links, how="left",
                      left_on='NOME_BANNER', right_on='Nome')
########################################################################################

########################################################################################
# ajuste do layout final do input_hub
input_hub = join_links[['Cluster', 'TIPO_ENVIO', 'DATA_ENVIO', 'DIA_SEMANA', 'UTM_CAMPAIGN', 'SUBJECT', 'PRE_HEADER', 'UTM_SOURCE', 'UTM_MEDIUM', 'UTM_TERM', 'UTM_CONTENT', 'TEMPLATE', 'CICLO_VIDA', 'ENGAJAMENTO_ABERTURA', 'ENGAJAMENTO_CLIQUES', 'PRIMEIRA_VITRINE', 'SEGUNDA_VITRINE', 'TERCEIRA_VITRINE',
                        'CHAMADA_VITRINE_1', 'CHAMADA_VITRINE_2', 'TIPO_BANNER', 'NOME_BANNER', 'TEXTO_CHAMADA', 'TITULO', 'TEXTO_APOIO', 'ATRIBUTOS', 'TITULO_LINHA', 'CTA', 'Link', 'Filtros', 'LINK_ORIGEM', 'Texto Legal', 'COMENTARIOS', 'LOGO_LINK']].rename(columns={'Link': 'URL', 'Filtros': 'FILTRO', 'Texto Legal': 'TEXTO_LEGAL'})
########################################################################################

########################################################################################
# separa arquivos por cluster e grava em csv específico

for i in cluster:
    try:
        write_df = input_hub[input_hub.UTM_CONTENT == i]
        write_df.to_csv(f"{bucket_name}{prefix_event.replace(file,'').replace('input_crm','input_hub')}{file.replace('input_crm','input_hub')}",
                        sep=';', index=False, encoding='utf-16')
    except Exception:
        print("Houve um erro durante o processo de escrita em " +
              i + " .", " Favor verificar")

########################################################################################
