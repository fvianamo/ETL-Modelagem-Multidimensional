from scrapping import get_list_of_ads
from scrapping import get_ad_info

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

	info_ads = dict()

	for i in list_all:
		print(get_ad_info(i)) #imprime as informações resgatadas no anuncio

	#TODO: persistir a base de dados de anuncios resgatos em um arquivo .csv

