import sys
import csv
from .classes import *

filename = 'usuarios.csv'

def gerar_lista():
   csvarquivo=[]
   with open("usuarios.csv", encoding='utf-8') as csvfile:
      leitor_csv = csv.reader(csvfile)
      for i in leitor_csv:
         csvarquivo.append(i)
   return csvarquivo

def escrever_csv(texto):
   lista=gerar_lista()
   lista.append(texto)
   with open("usuarios.csv", 'w', newline='\n') as csvfile:
      file_writer = csv.writer(csvfile,delimiter=',')
      for i in range(len(lista)):
         file_writer.writerows(lista)

def sobescrever_csv():
   with open("usuarios.csv", 'w', newline='\n') as csvfile:
      file_writer = csv.writer(csvfile,delimiter=',')
      file_writer.writerows([gerar_lista()])

adm=Usuario("84998274748","Anderson","andersonssgf7@gmail.com","Andinhossgf1*","Rua 13 de Maio, 130")