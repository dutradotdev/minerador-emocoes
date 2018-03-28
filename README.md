# minerador_emocoes

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
<p>É basicamente identificar padrões em textos:</p>
<p>"60% dos textos que contém a palavra <b>Internacional</b> também contém a palavra <b>Grêmio</b>.
3% de todos os textos contém ambas as palavras.
Case baseado nisso: O walmart identificou que quando eram vendido fraudas também
 eram vendido cerveja. Aí eles colocaram uma seção de cerveja próxima de fraudas
  e maximizaram a venda desses produtos.
</p>

<p>A presença do termo <b>Pelé</b></p>
