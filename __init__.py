import requests 
from bs4 import BeautifulSoup

url = 'https://rn.olx.com.br/rio-grande-do-norte/natal/celulares'

def get_list_of_ads(url=''):
	#realiza request na pagina da OLX
	r = requests.get(url)

	#checa se a pagina foi recebida com sucesso
	if r.status_code == 200:
		html_doc = r.text
	else:
		return []

	#transforma pagina recebida em um obj do bs4 
	soup = BeautifulSoup(html_doc, 'html.parser')

	#resgata os elementos que contem os anuncios da página do OLX
	anuncios = soup.findAll('a', {"class": 'OLXad-list-link'})

	#inicializa a lista de links
	link_list = []

	for anuncio in anuncios:
		link_list.append(anuncio['href'])

	return link_list

def get_ad_info(url=''):
	r = requests.get(url)

	if r.status_code == 200:
		#faca aqui
		soup = BeautifulSoup(r.text, 'html.parser')
		info = dict()
		info['tilulo'] = soup.findAll('h1', {'class': 'OLXad-title'})[0].string
		info['preco'] = soup.findAll('span', {'class': 'actual-price'})[0].string
		return info
	else:
		return {}

pare_o_loop = True

list_all = []
i = 1

while pare_o_loop:
	print('tentando resgatar a lista ' + str(i))
	listing = get_list_of_ads(url + '?o=' + str(i))
	if not listing or i == 2:
		pare_o_loop = False
	else:
		i += 1
		list_all += listing

info_ads = dict()

for i in list_all:
	print(get_ad_info(i))

print(list_all)

#imprime a pagina recebida
#print(soup.prettify())

