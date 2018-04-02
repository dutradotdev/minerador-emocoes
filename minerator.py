# -*- coding: utf-8 -*-
import nltk

nltk.download('rslp')
#necessário pré-processamento das frases porque quando usamos web-crawlers da internet as frases vem cheia de tag html, acentuação
#e etc..

#remoção de stop-words porque diminui o processamento de dados e elas não caracterizam nada no texto

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

#o nltk tem uma lista de stopwords própria tbm
#stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

def removeStopWords(texto):
        frases = []

        #para cada palavra e emocao
        for(palavras, emocao) in texto:

                #eu splito palavra por palavra e coloco no semstop só se não conter nas stopwords
                semstop = [p for p in palavras.split() if p not in stopwords]
                frases.append((semstop, emocao))
        return frases

print(removeStopWords(base))

def aplicaStemmer(texto):
        stemmer = nltk.stem.RSLPStemmer()
        frasesSteeming = []
        for(frases, emocao) in texto:
                comStemming = [str(stemmer.stem(p)) for p in frases.split() if p not in stopwords]
                frasesSteeming.append((comStemming, emocao))
        return frasesSteeming

frasesComStemmer = aplicaStemmer(base)
print(frasesComStemmer)

#coloco todas as palavras em um vetor, sem colocar as emoções
def buscaPalavras(frases):
        todasPalavras = []
        for(palavras, emocao) in frases:
                todasPalavras.extend(palavras)
        return todasPalavras

palavras = buscaPalavras(frasesComStemmer)
print(palavras)

def buscaFrequencia(palavras):
        palavras = nltk.FreqDist(palavras)
        return palavras

frequencia = buscaFrequencia(palavras)
#apenas as 50 primeiras palavras
print(frequencia.most_common(50))

def buscaPalavrasUnicas(frequencia):
        #pego somente a chave das frequências pq já é um valor único
        freq = frequencia.keys()
        return freq

palavrasUnicas = buscaPalavrasUnicas(frequencia)
#essa vão ser as palavras do cabeçalho da base de dados
print(palavrasUnicas)

#passo uma frase apenas com radicais e vejo quais palavras da frase que eu passei existem
#na nossa base de dados
def extratorPalavras(documento):
        doc = set(documento)
        caracteristicas = {}
        for palavras in palavrasUnicas:
                caracteristicas['%s' % palavras] = (palavras in doc)
        return caracteristicas

caracteristicasFrase = extratorPalavras(['am', 'nov', 'dia'])
print(caracteristicasFrase)


#esse apply_features ele faz todo o preenchimento da base de dados com true ou false.
#Eu passo uma função extratora que marca se tem ou não tem em toda a base de dados
#e depois passo a base de dados completa só que com radicais
#e aí ele compara todas as palavras da primeira frase com todas as palavras da base
#e marca se a palavra é usada na primeira frase ou não
#essa é a base final, tratada e sem repetições que eu jogo nos algoritmos.
base_completa = nltk.classify.apply_features(extratorPalavras, frasesComStemmer)
print(base_completa)
