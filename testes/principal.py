from dominio import Usuario, Lance, Leilao

gui = Usuario("Gui")
yuri = Usuario("yuri")

lance_do_gui = Lance(gui, 100.0)
lance_do_yuri = Lance(yuri, 150.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')