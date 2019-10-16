import requests
import random


antena = random.randint(1,5)
code = random.randint(1,50)

def sendData(antena_id, code):

	url = 'http://172.16.8.107:8000/'
	result = requests.Session()
	result.get(url)

	if 'csrftoken' in result.cookies:
		csrftoken = result.cookies['csrftoken']
	else:
		csrftoken = result.cookies['csrf']


	dados = {
	 'csrfmiddlewaretoken':csrftoken,
	 'server': '172.16.8.107',
	 'antena': str(antena_id), 
	 'code': str(code),
	}

	response = result.post(url, data=dados)

	if response.status_code == 200:
		print("Enviado com sucesso!")
		print(response.status_code)
	else:
		print("Falha ao enviar!")
		print(response.status_code)


sendData(antena, code)