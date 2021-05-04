import re

class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = url.find('?')
        url_base = url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = url.find('?')
        url_parametros = url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def converter(self):
        dolar = 5.50
        quantidade = self.get_valor_parametro("quantidade")
        moedaOrigem = self.get_valor_parametro("moedaOrigem")
        moedaDestino = self.get_valor_parametro("moedaDestino")
        if moedaOrigem == 'real' and moedaDestino == 'dolar':
            valor_conversao = int(quantidade) / dolar
            return valor_conversao
        elif moedaOrigem == 'dolar' and moedaDestino == 'real':
            valor_conversao = int(quantidade) * dolar
            return valor_conversao
        else:
            raise ValueError("Não é possível fazer a conversão dessas moedas.")

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + '\nParâmetros: ' + self.get_url_parametros() + '\nURL Base: ' + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other

url = "bytebank.com/cambio?quantidade=100&moedaDestino=real&moedaOrigem=dolar"
extrator_url = ExtratorUrl(url)
# valor_quantidade = extrator_url.get_valor_parametro(input("Qual o parametro (quantidade, moedaDestino ou moedaOrigem)? "))
# print(valor_quantidade)
print(extrator_url.converter())