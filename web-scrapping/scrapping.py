import requests 
from bs4 import BeautifulSoup

#dada a URL da página de anuncios da OLX retorna a lista de links do anuncios da página
def get_list_of_ads(url=''):
	#realiza request na pagina
	r = requests.get(url)
	#print(r.status_code)

	#checa se a pagina foi recebida com sucesso
	if r.status_code == 200:
		html_doc = r.text #instancia a variavel html_doc com o HTML recebido
	else:
		return [] #em caso de falha no recebimento da página retorna lista vazia

	#transforma pagina recebida em um obj do bs4 
	soup = BeautifulSoup(html_doc, 'html.parser') #faz o parse do HTML da página recebida

	#resgata os elementos que contem os anuncios da página do OLX
	anuncios = soup.findAll('a', {"class": 'OLXad-list-link'})

	#inicializa a lista de links
	ad_link = []

	for anuncio in anuncios:
		ad_link.append(anuncio['href']) # inclui o link do objeto HTML do anuncio na lista 

	#retorna a lista de links de anuncio
	return ad_link

#retorna metadados do anuncio dado o link da página do anuncio da OLX
def get_ad_info(url=''):
	r = requests.get(url) #realiza request na página

	#checa se a página foi carregada com sucesso
	if r.status_code == 200:
		#print('tentando regastar dados de ' + url)
		try:
			soup = BeautifulSoup(r.text, 'html.parser') #faz o parse da página HTML
			info = dict() #instancia o dicionário que será retornado
			info['tilulo'] = soup.findAll('h1', {'class': 'OLXad-title'})[0].string #inclui o titulo do anuncio no DICT
			info['preco'] = soup.findAll('span', {'class': 'actual-price'})[0].string #inclui o preço do anuncio no DICT
			info['descricao'] = soup.findAll('div', {'class': 'OLXad-description mb30px'})[0].find('p').getText()
			
			detalhes = soup.findAll('div', {'class': 'OLXad-details mb30px'})
			detalhes = detalhes[0].findAll('strong', {'class': 'description'})
			info['tipo'] = detalhes[0].getText()
			info['estado'] = detalhes[1].getText()
			
			localizacao = soup.findAll('div', {'class': 'OLXad-location mb20px'})
			localizacao = localizacao[0].findAll('strong', {'class': 'description'})
			info['cidade'] = localizacao[0].getText()
			info['cep'] = localizacao[1].getText()
			info['bairro'] = localizacao[2].getText()
			return info
		except IndexError:
			return {}
	#em caso de falha no carregamento da página retorna DICT vazio
	else:
		return {}