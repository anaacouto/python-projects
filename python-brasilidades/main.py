from documento import Documento

from validate_docbr import CNPJ

cnpj = "35379838000112"
cpf = "15316264754"

documento = Documento.cria_documento(cpf)
print(documento)