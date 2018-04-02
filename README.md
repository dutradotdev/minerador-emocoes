# minerador_emocoes

<h1>Mineração de texto</h1>
<p>Visando a ideia de customer success dentro da startup, decidi que o meu projeto será com enfâse na análise mais precisa e detalhada do customer success.</p>
<p>Este projeto é uma solução com inteligência artificial para analisar o sentimento do cliente em um texto formatado (JSON, XML) ou um texto livre (Post do facebook, tweet, etc). </p>
<p>Técnicas de classificação:</p>

<p><b>Classificação:</b></p>
<p>E-mail:
Entrada(post, tweet) -> Algoritmo classficador -> Spam, Normal 
</p>

<p>Notícia:
"Fred passa por cirurgia no joelho direito e tem alta prevista para esta quinta-feira" -> Algoritmo classificador multirrótulo -> Esporte, Cone, Lesão
</p>

<p><b>Agrupamento (Clustering):</b></p>
<p>Agrupamento de pratos, por exemplo. Um funcionário caixa da Sapore sempre insere no app o prato que o cliente comeu na hora do pagamento. O prato é "arroz com feijão" mas o funcionário coloca "arrz e feij" ou "arros e fejao". Conseguimos detectar e agrupar todo mundo como "Arroz com Feijão".</p>
<p> Detecção de plágio </p>

<p><b>Extração de informação:</b></p>
<p>Em nosso cenário, eu recebo um comentário do facebook e consigo extrair: Nome, Sobrenome, Data, Hora, Opinião, Prato em questão, restaurante, Sentimento identificado e etc..</p>

<p>Utilização de ontologias, representando conceitos e relacionamentos em um domínio<b>(section2, lecture3)</b></p>

<p><b>Associações:</b></p>
<p>Correlação entre palavras (Associações):</p>

<p>É basicamente identificar padrões -regras de associações- em textos:</p>
=======
<p>É basicamente identificar padrões em textos:</p>
<p>"60% dos textos que contém a palavra <b>Internacional</b> também contém a palavra <b>Grêmio</b>.
3% de todos os textos contém ambas as palavras.
Case baseado nisso: O walmart identificou que quando eram vendido fraudas também
 eram vendido cerveja. Aí eles colocaram uma seção de cerveja próxima de fraudas
  e maximizaram a venda desses produtos.
</p>

<p>A presença do termo <b>Pelé</b> aumenta em 5 vezes a chance de ocorrência dos termos <b>Copa</b> e <b>1970</b></p>
<b>Regra deInterpratação sintica e semântica das frases associação: Pelé => Copa e 1970</b>
<p>A polícia usa esse tipo de algoritmo para varrer redes sociais e identificar se terá briga em jogos de futebol</p>

<p><b>Correspondências semânticas</b></p>
<p>Migração de base de dados(sec 2 aula 4)</p>
<p>matcher para consulta de dados no banco (Monta um select automático com base no que o usuário digitou)</p>

<p><b>Recuperar informação:</b></p>
<p>Indexação API Lucene(Java)(sec 2 aula 4)</p>

<p><b>Resumo de documentos:(sec 2 aula 4)</b></p>

<p><b>Abordagem estatística</b></p>
<p>Frequência de termos, ignorando informações semânticas</p>

<p><b>Processamento de lingaugem natural</b></p>
<p>Interpratação sintica e semântica das frases</p>
<p>Fazer o computador entender a frase</p>


<h1>Mineração de emoção</h1>
<p>Classificação:
texto -> algoritmo -> alegria, tristeza, medo
</p>

<p>Monitoramento de sentimento das pessoas em relação a marcas, entidades, figuras sociais, etc</p>

<p>Gestão de crises (% de alegria, tristeza em comentários ou sei lápara tomada de decisões estratégicas)</p>

<p>Entender o que o consumidor está pensando</p>

<p><b>Classificação por polaridade</b></p>

texto -> Algoritmo de machine learning -> classificação em positivo, neutro ou negativo

<p><b>Classificação por Emoção</b></p>
<p>Surpresa, alegria, tristeza, medo, nojo e raiva</p>

<h1>Classificação:</h1>
<p>Com base nos atributos previsores eu crio uma classe. </p>
<p>Esses atributos previsores são atributos de uma base de dados histórica</p>
<p>Aprendizado supervisionado de máquina. Ele analisa todos os atributos previsores da pessoa e com base nisso, define como a pessoa foi categorizada.</p>

<p>Eu coloco uma base histórica com muitos registros e gero uma classe para a informação que eu quero(sec2 ep6) e, para prever o movimento dos próximos clientes, eu submeto as informações dos clientes que eu quero prever em um algoritmo de aprendizado de máquina com base nessa base histórica que foi processada.</p>

<p>Cada registro pertence a uma classe e possui um conjunto de atributos previsores</p>
<p>Objetiva-se descobrir um relacionamento entre os atributos previsores e o atributo meta(classe)</p>

<p>O valor do atributo meta é conhecido (aprendizagem supervisionada)</p>

<h1>Representação da classificação(método indutivo)(img sec2ep78)</h1>

<h1>Classificação de textos</h1>
<p>Os atributos previsores na classificação de textos são as próprias palavras</p>
<p>É feito um pivoteamente de frase para coluna. Cada palavra da frase vira uma coluna. Stop-words são eliminadas e são apenas palavras únicas permitidas. Logo após isso, para cada coluna eu coloco uma flag booleana para identificar se a palavra está na frase daquele registro </p>
=======

<h1>Como funciona:</h1>
<p>Temos uma base de frases e uma coluna com o sentimento que ela representa.</p>
<p>Removemos stop-words (o, a, agora, agora, algum, alguma, aquele, aqueles, de, deu, do, e) pois diminui o processamento e 
deixa a tabela menor.</p>
<p>(Steeming) Extraímos os radicais das palavras para reduzir a dimensionalidade dos dados. A raiz da palavra é um elemento originário e irredutível em que se encontra a significação das palavras.</p>
<p>Desvantagens de usar stemming: Palavras com sentido opostos possuem o mesmo radical: Novamente e novo, por exemplo.</p>
<p>A tabela final é feita apenas com radicais únicos de palavras. Não posso ter cabeçalhos iguais. </p>