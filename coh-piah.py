import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    print()
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        print()
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma = 0
    for assinatura in as_a:
        soma = soma + (abs(as_a[i] - as_b[i]))
        i = i + 1
    return soma / 6
    

def calcula_assinatura(texto):
    '''Funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = []
    lista_palavras = []
    somaSentenca = 0
    for sentenca in lista_sentencas:
        somaSentenca = somaSentenca + len(sentenca)
        lista_frases.extend(separa_frases(sentenca))

    somaFrase = 0        
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))
        somaFrase = somaFrase + len(frase)
    
    qdeCaracter = 0
    for palavra in lista_palavras:
        qdeCaracter = qdeCaracter + len(palavra)

    palavrasDiferentes = n_palavras_diferentes(lista_palavras)
    palavrasUnicas = n_palavras_unicas(lista_palavras) 
    
    wal = qdeCaracter / len(lista_palavras)  # wal - Tamanho médio de palavra
    ttr = palavrasDiferentes / len(lista_palavras) # ttr - Relação Type-Token
    hlr = palavrasUnicas / len(lista_palavras)  # hlr - Razão Hapax Legomana
    sal = somaSentenca / len(lista_sentencas) # sal - Tamanho médio de sentença
    sac = len(lista_frases) / len(lista_sentencas)  # sac - Complexidade média da sentença
    pal = somaFrase / len(lista_frases)  # pal - Tamanho medio de frase

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    resultado = []
    for tex in textos:
        ass_text = []
        ass_text = calcula_assinatura(tex)
        resultado.append(compara_assinatura(ass_text, ass_cp))
    
    valor_min = min(resultado)
    posicao = resultado.index(valor_min) + 1
  
    return posicao

assinatura_infectado = []
textos = []
assinatura_infectado = le_assinatura()
textos = le_textos()
resultado = avalia_textos(textos,assinatura_infectado)
print()
print('O autor do texto', resultado ,'está infectado com COH-PIAH')
