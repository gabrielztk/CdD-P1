import pandas as pd
import numpy as np
import math as math
from scipy import stats
import matplotlib.pyplot as plt

# copiado de https://pastebin.com/0KcDyqKq
def reta(dados_x, dados_y, label_x, label_y):    
    a = dados_y.cov(dados_x) / dados_x.var()
    b = dados_y.mean() - a*dados_x.mean()
 
    print("Taxa de correlaçâo:", '%06.4f' % (dados_x.corr(dados_y)))
    
 
    plt.figure(figsize=(8, 6))
    plt.scatter(dados_x, dados_y, c='red', alpha=0.8)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
 
    plt.plot((dados_x.min(), dados_x.max()), (a*dados_x.min()+b, a*dados_x.max()+b), color='blue')
 
    plt.tight_layout()
    plt.legend()
    plt.show()
    
def box(dados):
    print("A mediana desta seleção de dados é: {0}%".format('%06.4f' % dados.median()))
    print("A média desta seleção de dados é: {0}%".format('%06.4f' % dados.mean()))
    dados.plot.box()

#baseado em https://pastebin.com/0KcDyqKq    
def tudo(anoI, anoF, nomeX, nomeY, data_set, label_x, label_y):
    lista = np.arange(anoI, anoF+1)
    plt.figure(figsize=(16, 12))
    for d in lista:

        dados_x = data_set[nomeX + str(d)]
        dados_y = data_set[nomeY + str(d)]
        
        a = dados_y.cov(dados_x) / dados_x.var()
        b = dados_y.mean() - a*dados_x.mean()
        
        print("Taxa de correlaçâo em {0}:".format(d), '%06.4f' % (dados_x.corr(dados_y)))
        print("Coeficiente angular da reta em {0}:".format(d), '%06.4f' % (a))
        print(" ")
        
        plt.scatter(dados_x, dados_y, alpha=0.8)
        plt.plot((dados_x.min(), dados_x.max()), (a*dados_x.min()+b, a*dados_x.max()+b))
    
    plt.tight_layout()
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.legend()
    plt.grid()
    plt.show()

 
def corre(anoI, anoF, nomeX, nomeY, data_set):
    lista = np.arange(anoI, anoF+1)
    for d in lista:

        dados_x = data_set[nomeX + str(d)]
        dados_y = data_set[nomeY + str(d)]
        
        print("Taxa de correlaçâo em {0}:".format(d), '%06.4f' % (dados_x.corr(dados_y)))
        print(" ")
        
#baseado em https://pastebin.com/0KcDyqKq       
def vez(anoI, anoF, nomeX, nomeY, data_set, label_x, label_y):
    lista = np.arange(anoI, anoF+1)
    for d in lista:
        
        dados_x = data_set[nomeX + str(d)]
        dados_y = data_set[nomeY + str(d)]
       
        a = dados_y.cov(dados_x) / dados_x.var()
        b = dados_y.mean() - a*dados_x.mean()
        
        print("Taxa de correlaçâo em {0}:".format(d), '%06.4f' % (dados_x.corr(dados_y)))
        print("Coeficiente angular da reta em {0}:".format(d), '%06.4f' % (a))
        print(" ")
    
        plt.scatter(dados_x, dados_y, alpha=0.8)
        plt.plot((dados_x.min(), dados_x.max()), (a*dados_x.min()+b, a*dados_x.max()+b))
    
        plt.tight_layout()
        plt.xlabel(label_x)
        plt.ylabel(label_y)
        plt.legend()
        plt.grid()
        plt.show()