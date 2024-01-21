
"""cadastro de pessoas """



'''nome  = input("Nome: ")
idade =  input("Idade:" )
email =input(' E-mail: ')
senha = input(' Senah: ')

print(" seu nome e: {0}  idade: {1} email:{2} senha:sasa{3} ".format(nome,idade,email,senha))

print(f" seu nome e: {nome}  idade: {idade} email:{email} senha:sasa{senha} ")'''


'''idade = 19

if idade < 18 :
  print('nao pode dirigir')
elif idade > 18 & idade  < 20:
  print(' ja pode comecar tirar abilitaçao')
else : print('pode dirigir')

print(' fim')

print('/////////////////////////////////')'''


'''test = 0
while test < 1 :
  print('verdadeiro')
  
  test = test +1'''
'''print('tabuada 2')

for x in range(0 , 11):
  print('2 x',x,'=',x * 2)
  
print('')

print('tabuada 3')
  
  
for x in range(0 , 11):
  print('3 x',x,'=',x * 3)'''

from random import choice

print('.')
print('jogo-Pedra-Papel-Tezoura')
print('.')
print('//////////////////////////////////////')

jogador = input('escolha sua arma?: pedra , papel . tezoura: ')


def jogoSorte():
  
    if jogador == 'pedra':
         return jogador 
    elif jogador == 'papel':
        return jogador 
    elif jogador == 'tesoura':
        return jogador 
    else:
         return 'escolha invalida'
  

retorno = jogoSorte()


escolha_jogador = choice(['pedra', 'papel','tesoura'])

print(escolha_jogador)

if (retorno == 'pedra') and (escolha_jogador == 'tesoura') \
  or (retorno == 'papel') and (escolha_jogador == 'pedra') \
    or (retorno == 'tesoura') and (escolha_jogador == 'papel'):
   print('vc ganhou')
elif retorno == escolha_jogador:
  print('Empate')   
else:
  print(' vc perdeu')