# CARREGANDO BIBLIOTECAS
import pandas as pd
import unidecode
import re

# REMOVE CARACTER
def RemoveCaracter(string):
    texto = unidecode.unidecode(string)                               # REMOVE ACENTOS
    texto = re.sub(r"[@#$%&*^~-´'²³\\//|<>:;,.!?'0-9]", " ", texto)
    texto = texto.replace('_','')
    texto = texto.replace('"','')
    texto = texto.replace('`','')
    texto = texto.replace('[','')
    texto = texto.replace(']','')
    texto = texto.replace('{','')
    texto = texto.replace('}','')
    texto = texto.replace('(','')
    texto = texto.replace(')','')
    texto = texto.replace('+','')
    texto = texto.replace('-','')
    texto = texto.replace('=','')
    texto = texto.lower()   
    
    return texto

# REMOVE ESPAÇO - USADA SOMENTE NO CARREGAMENTO DE ARQUIVOS. NÃO TEVE APLICAÇÃO NO TRABALHO.
def RemoveEspaco(item):
    remove_espaco = item.strip() 
    return remove_espaco


# CARREGAMENTO DE ARQUIVOS
ortografia = pd.read_csv('correcao_ortografica.csv', header = None, index_col = 0, squeeze = True).to_dict()
digitacao = pd.read_csv('correcao_digitacao.csv', header = None, index_col = 0, squeeze = True).to_dict()
digrafos_vogais = open("digrafos_vogais_identicas.txt", encoding = 'UTF-8')
digrafos_vogais = list(map(RemoveEspaco, digrafos_vogais))

# FUNÇÃO ORTOGRÁFICA
def Correcao1(texto, correcao = ortografia):     
    lista_palavras = texto.split(" ") 
    lista_palavras = [item.strip() for item in lista_palavras if item.strip() != ''] 
    lista_corrigida = []
    
    for palavra in lista_palavras:
        if (palavra in correcao):
            palavra_correta = correcao.get(palavra)
            
            lista_corrigida.append(palavra_correta)
        else:
            lista_corrigida.append(palavra)
            continue
    
    texto_final = ' '.join(lista_corrigida) 
    texto_final = RemoveCaracter(texto_final)

    return texto_final

# SUBSTITUÍ ERROS DE DIGITAÇÃO
def Correcao2(texto, correcao = digitacao):     
    lista_palavras = texto.split(" ") 
    lista_palavras = [item.strip() for item in lista_palavras if item.strip() != ''] 
    lista_corrigida = []
    
    for palavra in lista_palavras:
        if (palavra in correcao):
            palavra_correta = correcao.get(palavra)
            
            lista_corrigida.append(palavra_correta)
        else:
            lista_corrigida.append(palavra)
            continue
    
    texto_final = ' '.join(lista_corrigida) 
    texto_final = RemoveCaracter(texto_final)

    return texto_final

# REMOÇÃO DE LETRAS REPETIDAS
def RemoveLetras(texto, lista = digrafos_vogais):
    lista_palavras =  texto.split(" ")  
    novo_texto = []
    vogais = ['a','e','i','o','u']
    consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    
    for palavra in  lista_palavras:
        palavra_separada = list(palavra)
        
        if (palavra in lista):
            novo_texto.append(palavra)
            
        elif (len(set(palavra_separada).intersection(consoantes)) > 0 and len(set(palavra_separada).intersection(vogais)) > 0 and palavra_separada not in lista):
            nova_palavra = []
            letra_inicial = palavra_separada[0]
            nova_palavra.append(letra_inicial)

            for i in range(1, len(palavra_separada)):
                    letra = palavra_separada[i]
                    
                    if (letra != palavra_separada[i-1]):
                        nova_palavra.append(letra) 
                    else:
                        continue 
            nova_palavra = "".join(nova_palavra)
            novo_texto.append(nova_palavra)
                    
        else:
            continue
            
    novo_texto = " ".join(novo_texto)
    return novo_texto

# STOPWORDS
stopwords = open("stopwords.txt", encoding = 'UTF-8')
stopwords = list(map(RemoveCaracter, stopwords))      
stopwords = list(map(RemoveEspaco, stopwords)) 

def RemoveStopwords(texto, stopwords = stopwords):     
    lista_palavras = texto.split(" ")                                                         
    remove_stopwords = [palavras for palavras in lista_palavras if palavras not in stopwords] 
    lista_palavras = [item.strip() for item in remove_stopwords if item.strip() != '']        
    texto_final = ' '.join(lista_palavras)                                                    
    return texto_final


# LEMATIZAÇÃO
arquivo_lema = open("lematizacao_portugues.txt", encoding = 'UTF-8')

dicionario_lema = {}

for linha in arquivo_lema:
    palavras = linha.split()
    dicionario_lema[RemoveCaracter(palavras[1])] = RemoveCaracter(palavras[0])

def Lematizacao(texto):
    lista_palavras = texto.split(" ") 
    lista_palavras = [item.strip() for item in lista_palavras if item.strip() != ''] 
    lista_lema = []

    
    for palavra in lista_palavras:
        if palavra in dicionario_lema.keys():
            palavra_lema = dicionario_lema.get(palavra)
            lista_lema.append(palavra_lema)
            
        else:
            lista_lema.append(palavra)
            
    texto_lema = ' '.join(lista_lema) 
    return texto_lema