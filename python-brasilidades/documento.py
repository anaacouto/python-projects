from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!")


class DocCpf:
    def __init__(self, documento):
        if self.valida_documento(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format()

    def valida_documento(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida_documento(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.format()
    
    def valida_documento(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)