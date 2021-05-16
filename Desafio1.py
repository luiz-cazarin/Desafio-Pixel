#!/usr/bin/env python
# coding: utf-8

# In[53]:


# Desafio pixel syngenta digital
# Desenvolvimento usando jupyter
# Utilizando python e as biblioteca NumPy e matplotlib
import numpy as np
import matplotlib.pyplot as plt


# In[54]:


# Atribuímos a imagem a uma variável usando o método plt.imread( )
# Passando o arquivo da imagem como parâmetro
img = plt.imread('Syngenta.bmp')


# In[55]:


# Verificamos o tipo do arquivo
type(img)
# Sabendo que é um objeto de array n-dimensional homogêneo


# In[56]:


# Verificamos os dados do arquivo
img.shape


# In[57]:


# Atribuímos o arquivo a uma variável
# img[linha, coluna, camada]
a = img[:,:,:]


# In[58]:


# Usamos a função unique para pegar apenas os valores únicos
np.unique(a)


# In[59]:


# Descobrimos que existe 4 valores (4 camadas)
# Sabemos que as cores são representadas em uma escala de 0 a 255
# Sendo 0 = preto e 255 = branco em decimal
# Ao analisarmos a imagem em um editor
# Descobrimos que a cor do pixel verde contém os seguintes valores #60c000 que são representados em hexadecimal
# Podemos representar em #RGB sendo 60 o valor do Red, c0 o valor do Green e 00 o valor do Blue
# convertendo os valores retornados da última função [ 0, 96, 192, 255] em hexadecimal
# Sabemos que os valores são iguais a 96 = 60, e 192 = c0, ou seja, a combinação dessas cores forma o pixel verde (#60c000)


# In[60]:


# Pegando a soma dos valores unicos [  0,  96, 192, 255]
np.unique(a, return_counts=True)
print(np.unique(a, return_counts=True))


# In[61]:


# Ao somar os valores dos pixels, retornamos [376006,    298,    298, 127398]
# sabendo que o segundo e o terceiro valor são responsáveis pela cor verde
# descobrimos que a existem 298 pixels verdes

