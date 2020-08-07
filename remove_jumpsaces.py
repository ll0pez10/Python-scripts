# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:27:25 2020

@author: luan9

Objetivo: Remover os caracteres de quebra de linha de qualquer texto em
ambiente Windows.
"""

from selenium import webdriver
import requests, bs4

driver = webdriver.Chrome('C:/Program Files/Google/chromedriver')
         
for elem in range(0,35):
    #endereço do site quantum leaps
    res = requests.get("https://www.state-machine.com/quickstart/lesson%s.txt" %(elem))                    
    res.raise_for_status()
    
    playFile = open("textoSemPulo_"+ str(elem) +".txt", "wb")
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile = open("textoSemPulo_"+ str(elem) +".txt", "r")
    
    lista_arquivo = playFile.readlines()
    texto = ''.join(lista_arquivo)
    textoSemPulo = texto.replace("\n", '')
    with open("textoSemPulo_"+ str(elem) +".txt", "w") as t:
        t.write(textoSemPulo)
    
playFile.close()
