import sys
import os


pergunta1 = "Qual personagem folclórico costuma ser agradado pelos caçadores com a oferta de fumo?\n a) Caipora\n b) Sacic\n c) Lobisomem\n d) Boitatá\n e) Negrinho do Pastoreio\n"

pergunta2 = "Qual o número mínimo de jogadores numa partida de futebol?\n a)2 b)5 c)3 d)11"

pergunta3 = "Em qual local da Ásia o português é língua oficial\n ? a) Índia\n b) Filipinas\n c) Moçambique\n d) Macau\n e) Portugal\n"

pergunta4 = " Quanto tempo a luz do Sol demora para chegar à Terra?\n a) 12 minutos\n b) 1 dia \nc) 12 horas\n d) 8 minutos\n"

pergunta5 = "Qual a nacionalidade de Che Guevara?\n a) Cubana\n b) Peruana\n c) Panamenha\n d) Boliviana\n"

pergunta6 = ". Quem é o autor de “O Príncipe”?\n a) Maquiavel\n b) Antoine de Saint-Exupéry c) Montesquieu\n d) Thomas Hobbes\n e) Rousseau\n"

dificuldade = input("Insira a dificuldade: \n 1 - Fácil 2 - Normal 3 - Difícil \n")



jogador1 = input("Insira o nome jogador 1: ")

pontos = 0 

def facil():
  if dificuldade == '1':
    
    print(pergunta1)
    resposta = input("" )
    
  if resposta == 'a':
    print('você acertou')
    pontos = 20
    print(jogador1 + ": " + str(pontos) + "pontos")
    
    
  else:
      
      print('você errou')
      print(jogador1 + ": " + str(pontos) + "pontos")
      print("Game Over")
      continuar = False
    


  print(pergunta4)
  resposta4 = input("" )
  if resposta4 == 'd':
    print('você acertou')
    pontos = pontos + 20
    print(jogador1 + ": " +  str(pontos) + "pontos")
    
    
  else:
      
      print('você errou')
      print(jogador1 + ": " + str(pontos) + "pontos")
      print("Game Over")
      continuar = False
    
    

def medio():
  if dificuldade == '2':
    
    print(pergunta2)
    resposta2 = input("" )
    print(jogador1 + " 50 pontos")
  if resposta2 == 'd':
    print('você acertou')
    pontos = 50
    print(jogador1 + ": " +  str(pontos) + "pontos")
    
    
    
  else:
      
      print('você errou')
      print(jogador1 + ": " + str(pontos) + "pontos")
      print("Game Over")
      continuar = False

  print(pergunta5)
  resposta5 = input("" )
  if resposta5 == 'a':
    print('você acertou')
    pontos = pontos + 50
    print(jogador1 + ": " +  str(pontos) + "pontos")
    
    
  else:
      
      print('você errou')
      print(jogador1 + ": " + str(pontos) + "pontos")
      print("Game Over")
      continuar = False

    
    


def dificil():
  if dificuldade == '3':
    
    print(pergunta3)
    resposta3 = input("" )
    
  if resposta3 == 'd':
    print('você acertou')
    pontos = 70
    print(jogador1 + ": " + str(pontos) + "pontos")
    
    
  else:
      
      print('você errou')
      print(jogador1 + ": " + str(pontos) + "pontos")
      print("Game Over")
      continuar = False
    
      


  print(pergunta6)
  resposta6 = input("" )
  if resposta6 == 'a':
    print('você acertou')
    pontos = pontos + 50
    print(jogador1 + ": " +  str(pontos) + "pontos")
    
    
  else:
      
      print('você errou')
      print(jogador1 + ": " + str(pontos) + "pontos")
      print("Game Over")
      continuar = False
  
continuar = True

while continuar :


  pontos = 0 
  
  if dificuldade == '1':
    facil()
  elif dificuldade == '2':
    medio()
  else:
    dificil()


  jogador1 = input("Insira o nome jogador 1: ")

  dificuldade = input("Insira a dificuldade: \n 1 - Fácil 2 - Normal 3 - Difícil \n")



  




  

