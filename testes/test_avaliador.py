from unittest import TestCase
from dominio import Avaliador, Lance, Leilao, Usuario

class TestAvaliador(TestCase):

    def test_avalia(self):
        gui = Usuario('gui')
        yuri = Usuario('yuri')
        lance_do_gui = Lance(gui, 100.0)
        lance_do_yuri = Lance(yuri, 150.0)
        leilao = Leilao('celular')
        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)
        avaliador = Avaliador()
        avaliador.avalia(leilao)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)