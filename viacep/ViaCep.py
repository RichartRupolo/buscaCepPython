import json
import requests
from sys import exit

class ViaCEP:

	def __init__(self, cep):
		self.cep = cep

	def getDadosCEP(self):
		url_api = ('http://www.viacep.com.br/ws/%s/json' % self.cep)
		req = requests.get(url_api)
		if req.status_code == 200:
			dados_json = json.loads(req.text)
			return dados_json
		