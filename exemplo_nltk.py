# -*- coding: utf-8 -*-
import nltk
#nltk.download('words')
#nltk.download('maxent_ne_chunker')

texto = 'Mr. Lucas isso e um teste. Mr. Lucas teste 2'
frases = nltk.tokenize.sent_tokenize(texto) #separo as frases
tokens = nltk.word_tokenize(texto) #separa palavra por palavra da frases em tokens
classes = nltk.pos_tag(tokens) #classifica se é sujeito, etc
entidades = nltk.chunk.ne_chunk(classes) #identificação das entidades(pessoas, organizações, etc)
print('Frases: ', frases)
print('Tokens: ', tokens)
print('Classes: ', classes)
print('Entidades: ', entidades)