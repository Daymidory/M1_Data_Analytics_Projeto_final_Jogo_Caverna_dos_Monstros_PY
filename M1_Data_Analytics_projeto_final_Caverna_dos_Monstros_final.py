print(""" 
 ▄████▄  ▄▄▄   ██▒   █▓█████ ██▀███  ███▄    █ ▄▄▄                                              
▒██▀ ▀█ ▒████▄▓██░   █▓█   ▀▓██ ▒ ██▒██ ▀█   █▒████▄                                            
▒▓█    ▄▒██  ▀█▓██  █▒▒███  ▓██ ░▄█ ▓██  ▀█ ██▒██  ▀█▄                                          
▒▓▓▄ ▄██░██▄▄▄▄█▒██ █░▒▓█  ▄▒██▀▀█▄ ▓██▒  ▐▌██░██▄▄▄▄██                                         
▒ ▓███▀ ░▓█   ▓██▒▀█░ ░▒████░██▓ ▒██▒██░   ▓██░▓█   ▓██▒                                        
░ ░▒ ▒  ░▒▒   ▓▒█░ ▐░ ░░ ▒░ ░ ▒▓ ░▒▓░ ▒░   ▒ ▒ ▒▒   ▓▒█░                                        
  ░  ▒    ▒   ▒▒ ░ ░░  ░ ░  ░ ░▒ ░ ▒░ ░░   ░ ▒░ ▒   ▒▒ ░                                        
░         ░   ▒    ░░    ░    ░░   ░   ░   ░ ░  ░   ▒                                           
░ ░           ░  ░  ░    ░  ░  ░             ░      ░  ░                                        
▓█████▄ ▒█████   ██████     ███▄ ▄███▓▒█████  ███▄    █  ██████▄▄▄█████▓██▀███  ▒█████   ██████ 
▒██▀ ██▒██▒  ██▒██    ▒    ▓██▒▀█▀ ██▒██▒  ██▒██ ▀█   █▒██    ▒▓  ██▒ ▓▓██ ▒ ██▒██▒  ██▒██    ▒ 
░██   █▒██░  ██░ ▓██▄      ▓██    ▓██▒██░  ██▓██  ▀█ ██░ ▓██▄  ▒ ▓██░ ▒▓██ ░▄█ ▒██░  ██░ ▓██▄   
░▓█▄   ▒██   ██░ ▒   ██▒   ▒██    ▒██▒██   ██▓██▒  ▐▌██▒ ▒   ██░ ▓██▓ ░▒██▀▀█▄ ▒██   ██░ ▒   ██▒
░▒████▓░ ████▓▒▒██████▒▒   ▒██▒   ░██░ ████▓▒▒██░   ▓██▒██████▒▒ ▒██▒ ░░██▓ ▒██░ ████▓▒▒██████▒▒
 ▒▒▓  ▒░ ▒░▒░▒░▒ ▒▓▒ ▒ ░   ░ ▒░   ░  ░ ▒░▒░▒░░ ▒░   ▒ ▒▒ ▒▓▒ ▒ ░ ▒ ░░  ░ ▒▓ ░▒▓░ ▒░▒░▒░▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒ ▒░░ ░▒  ░ ░   ░  ░      ░ ░ ▒ ▒░░ ░░   ░ ▒░ ░▒  ░ ░   ░     ░▒ ░ ▒░ ░ ▒ ▒░░ ░▒  ░ ░
 ░ ░  ░░ ░ ░ ▒ ░  ░  ░     ░      ░  ░ ░ ░ ▒    ░   ░ ░░  ░  ░   ░       ░░   ░░ ░ ░ ▒ ░  ░  ░  
   ░       ░ ░       ░            ░      ░ ░          ░      ░            ░        ░ ░       ░  
 ░                                                                                              
""")
print("featuring Power Puff Girls")
print()
intro = print("Três irmãs, Florzinha, Lindinha e Docinho, decidiram fazer uma viagem de carro juntas.")
print("Florzinha é estudante de veterinária e sempre leva consigo um kit de primeiros socorros e medicamentos para os bichinhos.")
print("Lindinha é estudante de engenharia, bastante metódica e pragmática.")
print("Florzinha, por sua vez, é a mais artista do grupo e dedica-se ao estudo da música. Muito sensível, acredita que a música opera mágica.\nPor isso, sempre traz consigo o seu violino.")
print("Distraídas, não perceberam quando os comandos do carro começaram a falhar logo que adentraram em um longo túnel.\nO susto veio quando, sem qualquer ação da motorista, a velocidade subitamente começou a aumentar.\nApavoradas, tentaram retomar o controle do carro, em vão...\nTudo que se lembram é de serem atingidas por uma forte luz que vinha na direção  contrária e, então,um profundo silêncio.")
print()

#Capítulo1: Escolhendo o personagem.
jogadoras = ["Florzinha","Lindinha","Docinho"]

h1 = ("******Capítulo 1******Escolhendo o jogador*******************************").upper()
print(h1)
print()
print("[-Meu deus! O que aconteceu? Minha cabeça dói… Onde estou? Cadê todo mundo?]")
print()
print("~~~Escolha uma personagem para jogar e preencha o campo abaixo.~~~")
jogadoraEscolhida = input("Digite o nome da personagem: ").capitalize()

while jogadoraEscolhida not in jogadoras:
    print("Erro!!! Você deve escolher uma das seguintes personagens: Florzinha, Lindinha ou Docinho")
    print()
    jogadoraEscolhida = input("Digite o nome da personagem: ").capitalize()

if jogadoraEscolhida in jogadoras:
    print("Você escolheu: ", jogadoraEscolhida)
    print('Boa sorte!!!')

#Capítulo2: Escolhendo um item de auxílio.
print()
print()
h2 = ("******Capítulo 2 ******Escolhendo um item de auxílio*********************").upper()
print(h2)

A = "kit_de_primeiros_socorros_para_animais"
B = "smartphone"
C = "violino"
listaItens = ["A", "B", "C"]


print("- Que lugar esquisito! Parece uma caverna…\nO carro está completamente destruído, não vai servir para me tirar daqui …\nTalvez alguma coisa das nossas bagagens possa ser útil …\nQue sorte a minha! Olha o que encontrei: \n um kit de primeiros socorros para animais,\num smartphone e um violino!")
print()
print("~Você deve escolher apenas um dos itens referidos para ajudar", jogadoraEscolhida, " nesta jornada.~")
print("A - kit de primeiros socorros para animais\nB - smartphone\nC - violino")
print()
itemEscolhido = input("Digite a letra correspondente ao item escolhido: ").upper()


while itemEscolhido not in listaItens:
  print("ERRO!! Você deve escolher uma das seguintes opções: A, B ou C")
  itemEscolhido = input("Digite a letra correspondente ao item escolhido: ")

if itemEscolhido in listaItens:
    if itemEscolhido == "A":
      print()
      print(jogadoraEscolhida, "devidamente equipada com", A, "está pronta para o game!!")
    elif itemEscolhido == "B":
      print()
      print(jogadoraEscolhida, "devidamente equipada com", B, "está pronta para o game!!")
    elif itemEscolhido == "C":
      print()
      print(jogadoraEscolhida, "devidamente equipada com", C, "está pronta para o game!!")

print()
print()
#Capitulo3: Monstros à vista.
h3 = ("******Capítulo 3 ******Monstros à vista!!********************************").upper()
print(h3)
print("[-Olha! Algumas inscrições na parede.. deixe-me ver o que dizem..]")
print()
print("~~~", jogadoraEscolhida, " se aproxima da parede e lê a seguinte mensagem:~~~")
print()
print("[Bem vindo à gruta dos monstros!\nVocês, humanos, se consideram tão espertos…\nProve ou morrerá neste lugar.]\n")
print("~~~", jogadoraEscolhida, " encontrará alguns monstros pelo caminho.\nO monstro não a deixará passar a menos que o enigma proposto seja solucionado…\nou o monstro neutralizado.\nPara neutralizá-lo, tente usar o utensílio escolhido no início do jogo.~~~\n")
print("Vamos para o primeiro desafio!")
print()
#Capítulo4: Primeiro desafio: encontrando a Esfinge.
h4 = ("******Capítulo 4******Primeiro desafio: encontrando a Esfinge do Mal*****").upper()
print(h4)
print()
print("-Perfeito! E eu achando que as provas da facul do final de semestre seriam o meu maior problema...\nVejo uma sombra mais à frente, parecem asas…\nO que pode ser?")
print("""
..................................*VM$$$$$$$$$$$$$$NIIIIV.....
...............................:VM$$$$$$$$$$$$$$$$$NN$NF:.....
.............................:VN$$$$$$$$$$$$$$$$$$MIIIV.......
............................*N$$$$$$$$$$$$$$$$$$$$NN$N*.......
...........................F$$$$$$$$$$$$$$$$$$$$$$MIV:........
..........................:M$$$$$$$$$$$$$$$$$MIIIIMNV.........
...............**::::::....*$$$$$$$$$$$$$$$$$$$$$$MV:.........
...............*$NN$$$NI*...F$$$$$$$$$$$$$$$$$$MIV:...........
...............:FIIN$$$$$V..:M$$$$$$$$$$$$$NIIMNM:............
...............:MMVM$$$$$M:..V$$$$$$$$$$$$$$$$MV:.............
...............*N$VN$$$$$M:..:N$$$$$$$$$MIIIIV................
................VNV$$$$$$M:...F$$$$$$$$$MN$$N*................
................V*V$$$NMI*...*V$$$$$$$$$NMII:.................
...............:MVMMIIIFV:..*VM$$$$$NIIIMMNI:.................
...............*VVIIIIII::*FIF$$$$$$$$$NMIV...................
...............**IIM$$$MVMIIM$$$$$$$$MMM$M*...................
..............:VN$$$$$$NVM$$$$$$$$$$NMMI*:....................
.............*M$$N$$$$$$V$$$$$$$$$NMIMMV......................
.............F$$$VM$$$$$NVN$$$$$$$$$$N*.......................
.............:VN$VN$$$MN$NIIMMNNNMIV*:........................
...............:MVI$$$IF$$$$MMIIMIIFV*:.......................
...............:VFV$$$NV$$$$$$$$$$$$$$M*......****:...........
................VMVV$$$VM$$NIIM$$$$$$$$$V.....V*..............
................*$MV$$$VMNFIN$$$$$$$$$$$M:....:VV:............
................:NFI$$M:*VM$$$$$$$$$$$$FN*......:VV:..........
................:NVN$$*.*V$$$$$$$$$$$N*.VF........*F*.........
................:MV$$V...*N$$$$$$$$NF*..:M*........:I:........
................*FI$I:....*VN$$$$$$NNI:..*I:........I*........
..............::*V$M:......:*VVFIIM$$$I:..*F*......VI:........
""")

print("~~~", jogadoraEscolhida," se depara com a esfinge, uma criatura imponente, com o corpo de leão e a cabeça de um humano.\nA Esfinge lhe propõe um desafio:~~~")
print()
print("- Decifra-me ou te devoro. Que animal anda pela manhã sobre quatro patas, à tarde sobre duas e à noite, sobre três? Se errar, ainda te ofereço três novas chances.")

#Primeiro enigma

solucao1 = "Homem"
resposta1Jogadora = input("O animal é o (a) ").capitalize()
chance = 0

while solucao1 != resposta1Jogadora and chance < 3:
      print("Você errou!")
      print()
      chance = chance +1

      print("chance:", chance)
      resposta1Jogadora = input("O animal é o (a) ").capitalize()
      print()

if resposta1Jogadora == solucao1:
    print("Você acertou!")
    print("Preparada para o próximo desafio?")

# chances esgotadas. Ativando o item escolhido.

if chance == 3 and resposta1Jogadora != solucao1:
    print("Suas chances acabaram. Deseja tentar neutralizar o monstro com o item escolhido?")
    neutralizacao1 = input("Digite S/N: ").upper()

    if neutralizacao1 != ("S" or "N"):
        print: ("Você deve digitar S ou N")

        if neutralizacao == "N":
            print("Você morreu.")
            print("GAME OVER")
            print("**********************************************************************")

        elif neutralizacao == "S":
            if itemEscolhido == "A" and jogadoraEscolhida == "Florzinha":
                print("O item escolhido foi o kit_de_primeiros_socorros_para_animais")
                print(
                    "Parabéns, Florzinha! Você foi muito esperta por trazer em seu kit sedativo suficiente para apagar um touro! A Esfinge do Mal sequer percebeu a injeção que você aplicou. Dormirá, agora, o sono dos justos.")

            elif itemEscolhido == "C" and jogadoraEscolhida == "Lindinha":
                print("O item escolhido foi o smartphone")
                print("Um smartphone com sinal e bateria salva a vida, não é, Lindinha! God bless the Google!")

            elif itemEscolhido == "B":
                print("O item escolhido foi o violino.")
                print("A Esfinge do Mal não viu graça alguma no instrumento e o destruiu...junto com você!")
                print("Você morreu. GAME OVER.")

            elif itemEscolhido == "A" and jogadoraEscolhida != "Florzinha":
                print("O item escolhido foi o kit_de_primeiros_socorros_para_animais")
                print(
                    "Que sorte encontrar um sedativo para animais tão potente... Pena que você, sem experiência, se atrapalhou e não conseguiu aplicar a injeção.")
                print("Você morreu. GAME OVER.")

print()
print()

#Capítulo5: Segundo desafio: encontrando o Minotauro.
h5 = ("******Capítulo 5******Segundo desafio: encontrando o Minotauro**********").upper()
print(h5)
print()
print("[-Vejo outro monstro… aquilo são ... CHIFRES?!]")
print("""
....::................:::..............
....:*::..............**:..............
....:V*:.............:**:..............
...:*V*:..............*V*..............
...:*VV****VVVVVV*****VV*:.............
.....::*VMNNNNNNNNNMV*::...............
........::M$NNNN$N*:...................
.....::**VNNNNNNN$I*:::................
....:*VVVVINMMMM$MVVV*::...............
....*VVVVVVIN$$NIVVVVVV:..:::***:......
...:VVVVVVVVVVVVVVVVVVV*::**VV*::......
..:*VVVV*VVVVVVVVVV*VVV*:*VVVVV****:...
.::VVVV::*VVVVVVVV*:*VVV:**:**VVVV*::::
.:*VVV*::*MMIIIIMF:::*VVV*:::*VVVVV****
::*MMM*:*IMMMMMMMNI*:*VMNI*VV*::*VVVV*:
:.:IMI**IMMMMMMMMMNM:::VFVVV:::*****::.
:::*VVVMNMMMMMMMMMNN**VFV***:..:::::...
..:**VIN$$NMMMMNN$$NIIV*::.............
...:*M$$$$VVIMIN$$$NV*:................
...:VNN$$V::**::INN$V::................
....*VM$$N*:::.:VN$$I:.................
....:::*VM$M*:.:FN$$N*.................
........*MNV:...*IN$V:.................
.......*M$V:....::I$*:.................
......:VFV*:.....:*$M*:................
......:VV**:......*VMV::...............
......::::........**V*:................
.......................................
""")
print("~~Eis que", jogadoraEscolhida," se depara com o Minotauro, uma criatura bestial, com o corpo de homem e a cabeça de um touro.\nEntre berros e urros, o Minotauro apresenta o enigma:")
print()
print("-Dois pais e dois filhos sentaram-se para comer ovos no café da manhã. Cada um comeu um ovo. Quantos ovos eles comeram no total? Se errar, lhe dou duas outras chances de acerto.")
print("1 ovo")
print("3 ovos")
print("5 ovos")
print("8 ovos")


#Segundo enigma

solucao2 = "3"
resposta2Jogadora = input("A quantidade de ovos é: ")
chance = 0

while solucao2 != resposta2Jogadora and chance < 2:
    print("Você errou!")
    chance = chance + 1
    print("chance", chance)
    resposta2Jogadora = input("A quantidade de ovos é: ")

if resposta2Jogadora == solucao2:
    print("Você acertou!")
    print("Preparada para o último desafio?")

# Chances esgotadas. Ativando o item escolhido.

if chance == 2 and resposta2Jogadora != solucao2:
    print("Suas chances acabaram.Deseja tentar neutralizar o monstro com o item escolhido?")
    neutralizacao = input("Digite S/N: ").upper()

    if neutralizacao != ("S" or "N"):
        print: ("Você deve digitar S ou N")

    if neutralizacao == "N":
        print("Você morreu.")
        print("GAME OVER")
        print("*********************************************************************")

    elif neutralizacao == "S":
        if itemEscolhido == "A" and jogadoraEscolhida == "Florzinha":
            print("O item escolhido foi o kit_de_primeiros_socorros_para_animais")
            print(
                "Parabéns, Florzinha! Você foi muito esperta por trazer em seu kit sedativo suficiente para apagar um touro! O Minotauro sequer percebeu a injeção que você aplicou. Dormirá, agora, o sono dos justos.")

        elif itemEscolhido == "C" and jogadoraEscolhida == "Lindinha":
            print("O item escolhido foi o smartphone")
            print("Um smartphone com sinal e bateria salva a vida, não é, Lindinha! God bless the Google!")

        elif itemEscolhido == "B":
            print("O item escolhido foi o violino.")
            print("O Minotauro não viu graça alguma no instrumento e o destruiu...junto com você!")
            print("Você morreu. GAME OVER.")

        elif itemEscolhido == "A" and jogadoraEscolhida != "Florzinha":
            print("O item escolhido foi o kit_de_primeiros_socorros_para_animais")
            print(
                "Que sorte encontrar um sedativo para animais tão potente... Pena que você, sem experiência, se atrapalhou e não conseguiu aplicar a injeção.")
            print("Você morreu. GAME OVER.")

        elif itemEscolhido == "C" and jogadoraEscolhida != "Lindinha":
            print("O item escolhido foi o smartphone")
            print("Um smartphone com sinal e bateria realmente salva a vida... pena que somente a dona, que é a Lindinha, consegue desbloqueá-lo.")
            print("Você morreu. GAME OVER.")

    print()
    print("Vamos para o último desafio!!!")
print()
print()
#Capítulo6: Último desafio: encontrando a Sereia Malévola
h6 = ("******Capítulo 6******Terceiro desafio: encontrando a Sereia Malévola****").upper()
print(h6)
print()
print("[-Ufa! Nem acredito que cheguei até aqui!\nVejo uma luz ao fundo.... escuto uma voz bonita no ar.. o que será???]")
print()
print("~~", jogadoraEscolhida," corre em direção à luz e chega ao fim da gruta. À sua frente, um imenso mar e, logo adiante, avista quase serena, repousando sobre um barco e entoando uma cantiga.\nFinda a cantoria, a criatura lhe propõe um último desafio.\n")
print()
print("""
............................................
............................................
:*VVVVVVVVV*:......:*VVV*......:*VVVVVVVVV*:
..*M$$$$$$$$M:....*NMVVINV:...:F$$$$$$$$$V:.
..:F$$$$$$$$$*...*N$VVVVN$*...:M$$$$$$$$N*..
..*N$$$$$$$$$V:..V$$MVVI$$I...*$$$$$$$$$$V:.
..:*F$$$$$$$$$V:*F$$NVVM$$M*::M$$$$$$$$M*:..
....:MNN$$$$$$MFFINMVVVVINMFFI$$$$$$NNN*....
.::.:**FN$$$NIVVVVMVVVVVVIFVVVFM$$$$IV**.:..
........*MMMVVVVVVVVVVVVVVVVVVVVIIMV........
.........::*VVV***VVVVVVVVV***VVV:::........
...........:*VV*:.*VVVVVV*::*VVV*...........
.............:*VV**VVVVVVV*VVV*:............
..............*VVVVVVVVVVVVVVV:.............
...........:..:***VVVVVVVV***:..............
.................*VVVVVVVV*.................
.................*VVVVVVVV*.................
................::VVVVVVV*:..:****:.........
.............:**VV******V*..:F$$F:..........
......:....:*VVVVVV*****VV**I$$N*...........
...........*VVVV*:*VVVVVV**VN$N*............
...........*VVVV***VVVVV*:.V$$$*............
...........:*VVVVVVVVVVV*..*N$I:............
............:*VVVVVVVV*:....:VV:............
.............::******:......................
""")

print("- Eis o desafio, cuja solução poderá levar-te, com este barco em que estou, de volta ao seu mundo. Ofereço uma nova tentativa, apenas.")
print("Eu tenho a mesma idade que eu tinha no nascimento mais os anos desde então.\nQuando a minha sobrinha tiver a mesma idade que eu tenho agora, as nossas idades juntas irão somar 142 anos.\n Eu tenho o dobro dos anos que eu tinha quando minha idade era metade do que eu tenho agora.\n Eu sou onze anos mais velha do que quando tinha a mesma idade de um primo meu que é onze anos mais novo que eu.\n Quando o meu sobrinho tiver a idade que tenho agora, nossas idades juntas vão somar 133 anos.\n Tenho dois anos a mais do que um amigo meu que é dois anos mais novo do que um primo dele que tem a minha idade.\n Eu tenho quatro vezes a idade que meu sobrinho tinha quando eu tinha a idade que ele tem agora.")

# Último enigma

solucao3 = "56"
resposta3Jogadora = input("A idade que tenho é: ")
chance = 0

while solucao3 != resposta3Jogadora and chance < 1:
    print("Você errou!")
    chance = chance + 1
    print("chance", chance)
    resposta3Jogadora = input("A idade que tenho é: ")

if resposta3Jogadora == solucao3:
    print("Você acertou!\nVocê derrotou todos os monstros!!Partiu casa!")

# chances esgotadas. Ativando o item escolhido.

if chance == 1 and resposta3Jogadora != solucao3:
    print("Suas chances acabaram.Deseja tentar neutralizar o monstro com o item escolhido?")
    neutralizacao = input("Digite S/N: ").upper()

    if neutralizacao != ("S" or "N"):
        print: ("Você deve digitar S ou N")

    elif neutralizacao == "N":
        print("Você morreu.")
        print("GAME OVER")
        print("*********************************************************************")

    elif neutralizacao == "S":
        if itemEscolhido == "B" and jogadoraEscolhida == "Docinho":
            print("O item escolhido foi o violino")
            print("Que bela música! A Sereia está hipnotizada e não a atacará.")

        elif itemEscolhido == "C" and jogadoraEscolhida == "Lindinha":
            print("O item escolhido foi o smartphone")
            print("Um smartphone com sinal e bateria salva a vida, não é, Lindinha! God bless the Google!")

        elif itemEscolhido == "A":
            print("O item escolhido foi o kit_de_primeiros_socorros_para_animais.")
            print(
                "Que sorte encontrar um sedativo para animais tão potente... Pena que a Sereia Malévola parece estar tão distante, tão inalcançável...")
            print("Você morreu. GAME OVER.")

        elif itemEscolhido == "B" and jogadoraEscolhida != "Docinho":
            print("O item escolhido foi o violino.")
            print(
                "Realmente a música é um ponto fraco da Sereia.. pena que não se dá para chamar de música esse barulho que sai quando você toca.")
            print("Você morreu. GAME OVER.")

        elif itemEscolhido == "C" and jogadoraEscolhida != "Lindinha":
            print("O item escolhido foi o smartphone")
            print(
                "Um smartphone com sinal e bateria realmente salva a vida... pena que somente a dona, que é a Lindinha, consegue desbloqueá-lo.")
            print("Você morreu. GAME OVER.")
    print()
    print()
    print("FIM DO JOGO!!!")