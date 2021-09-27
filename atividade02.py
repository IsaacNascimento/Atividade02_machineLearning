!pip install plotly --upgrade #Baixa bibliotecas e funcionalidades, na qual não estão no ambiente colab. Plot para usar gráficos

%reset -f  #Apagar as váriaveis do Phy para não herdar váriaveis anteriores

import pandas as pd  #importar a biblioteca pandas como "pd", cuida de valores incosistentes

import numpy as np #importar a biblioteca numpy as "np", para tramento de números

import seaborn as sns #auxilio de gráficos

import matplotlib.pyplot as plt #Desenhar gráficos

import plotly.express as px #Auxilio na plotagem de gráficos

np.set_printoptions(threshold=np.inf) #Biblioteca que Determina a forma como os flots e outros objetos serão exibidos 

base_nursery = pd.read_csv("nursery.csv") #Lê o arquivo nursery.csv e armazena numa váriavel

print(base_nursery) #imprime a váriavel 

from sklearn.preprocessing import OneHotEncoder # Bibliotecas respnsáveis por passar informações categoricas para números;
from sklearn.compose import ColumnTransformer
