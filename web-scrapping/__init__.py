from scrapping import get_list_of_ads
from scrapping import get_ad_info
import pandas as pd

url = 'https://rn.olx.com.br/rio-grande-do-norte/natal/celulares'

if __name__ == '__main__':

	pare_o_loop = True #condicao para finalizar o while que resgata a lista de links de produtos
	list_all = [] #lista de urls de produtos
	i = 1 #contador de página

	while pare_o_loop:
		print('tentando resgatar a lista ' + str(i))
		listing = get_list_of_ads(url + '?o=' + str(i))
		if not listing:
			pare_o_loop = False
		else:
			i += 1
			list_all += listing

	print('tentando resgatar metadados de ' + str(len(list_all)) + ' anuncios...')
	print('vai demorarr...')

	info_ads = []

	count = 0
	
	for i in list_all:
		info_ads.append(get_ad_info(i))
		count += 1
		print ('(' + str(count) + '/' + str(len(list_all)) + ')')


	df = pd.DataFrame(info_ads).dropna()

	df['preco'] = df['preco'].str.replace('[R$ .]', '')

	df['tilulo'] = df['tilulo'].str.replace('([\n\t])', '')
	df['tilulo'] = df['tilulo'].str.replace('(\s{3,})', '')

	df['bairro'] = df['bairro'].str.replace('([\n\t])', '')
	df['bairro'] = df['bairro'].str.replace('(\s{3,})', '')

	df['cep'] = df['cep'].str.replace('([\n\t])', '')
	df['cep'] = df['cep'].str.replace('(\s{3,})', '')

	df['cidade'] = df['cidade'].str.replace('([\n\t])', '')
	df['cidade'] = df['cidade'].str.replace('(\s{3,})', '')

	df['descricao'] = df['descricao'].str.replace('([\n\t])', '')
	df['descricao'] = df['descricao'].str.replace('(\s{3,})', ' ')

	df['estado'] = df['estado'].str.replace('([\n\t])', '')
	df['estado'] = df['estado'].str.replace('(\s{3,})', ' ')

	df['tipo'] = df['tipo'].str.replace('([\n\t])', '')
	df['tipo'] = df['tipo'].str.replace('(\s{3,})', ' ')

	df['preco'] = df['preco'].astype(str).astype(int)

	print(df)

	df.to_csv('resultados.csv')
