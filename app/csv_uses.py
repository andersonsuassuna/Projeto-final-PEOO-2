import sys
import csv
from .classes import *

def gerar_lista():
   csvarquivo=[]
   with open("usuarios.csv", encoding='utf-8') as csvfile:
      leitor_csv = csv.reader(csvfile)
      for i in leitor_csv:
         csvarquivo.append(i)
   return csvarquivo # gerar cópia do arquivo csv em lista

def escrever_csv(texto): # append no csv
   with open("usuarios.csv", 'a', newline='') as csvfile:
      file_writer = csv.writer(csvfile,delimiter=',')
      file_writer.writerow(texto)

def substituir_csv(texto):
   with open("user.csv","w",newline="") as csvfile:
      file_writer=csv.writer(csvfile,delimiter=",")
      file_writer.writerow(texto)