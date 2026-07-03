Para Marta, com todo o meu amor.

# Prefácio {.unnumbered}

> Eis um plano: se uma pessoa usar um recurso que você não entende, mate-a. É mais fácil que aprender algo novo, e em pouco tempo os únicos programadores sobreviventes usarão apenas um subconjunto minúsculo e fácil de entender de Python 0.9.6. (_piscadela marota_).[[1](../5-postfacio/footnote.md#L1)]
> — _Tim Peters (lendário colaborador do CPython e autor do Zen de Python)_.

"Python é uma linguagem fácil de aprender e poderosa." Essas são as primeiras palavras do [tutorial oficial de Python 3.10](https://docs.python.org/3.10/tutorial/). Isso é verdade, mas há uma pegadinha: como a linguagem é fácil de entender e de começar a usar, muitos programadores praticantes de Python se contentam apenas com uma fração de seus poderosos recursos.

Uma programadora experiente pode começar a escrever código Python útil em questão de horas. Conforme as primeiras horas produtivas se tornam semanas e meses, muitos desenvolvedores continuam escrevendo código Python com um forte sotaque das linguagens que aprenderam antes. Mesmo se Python for sua primeira linguagem, muitas vezes ela é apresentada nas universidades e em livros introdutórios evitando deliberadamente os recursos específicos da linguagem.

Como professor, ensinando Python para programadores experientes em outras linguagens, vejo outro problema: só sentimos falta daquilo que conhecemos. Vindo de outra linguagem, qualquer um é capaz de imaginar que Python suporta expressões regulares, e procurar esse tema na documentação. Mas se você nunca viu desempacotamento de tuplas ou descritores de atributos, talvez nunca procure por eles, e pode acabar não usando esses recursos, só por que são novos para você.

Este livro não é uma referência exaustiva de Python de A a Z. A ênfase está em recursos da linguagem característicos de Python ou incomuns em outras linguagens populares. Vamos nos concentrar principalmente nos aspectos centrais da linguagem e pacotes essenciais da biblioteca padrão. Apenas alguns exemplos mostram o uso de pacotes externos como FastAPI, httpx, e Curio.

### Para quem é esse livro

Escrevi este livro para programadores que já usam Python e desejem se tornar fluentes em Python 3 moderno. Testei os exemplos em Python 3.10 e a maioria também em Python 3.9 e 3.8. Os exemplos que exigem especificamente Python 3.10 estão indicados.

Caso não tenha certeza se conhece Python o suficiente para acompanhar o livro, revise o [tutorial oficial de Python](https://docs.python.org/pt-br/3/tutorial/). Tópicos tratados no tutorial não serão explicados aqui, exceto por alguns recursos mais novos.

### Para quem esse livro não é

Se está começando a estudar Python, poderá achar difícil acompanhar este livro. Mais ainda, se você o ler muito cedo em sua jornada pela linguagem, pode ficar com a impressão que todo script Python precisa se valer de métodos especiais e truques de metaprogramação. Abstração prematura é tão ruim quanto otimização prematura.

Para quem está aprendendo a programar, recomendo o livro [Pense em Python](https://penseallen.github.io/PensePython2e/) de Allen Downey, disponível na Web.

Se já sabe programar e está aprendendo Python, o [tutorial oficial de Python](https://docs.python.org/pt-br/3/tutorial/) foi traduzido pela comunidade Python brasileira.

### Como ler este livro

Recomendo que todos leiam o [Capítulo 1](../2-volume-1/1-parte-i-estruturas-de-dados/01-o-modelo-de-dados-em-python.md). Após a leitura do capítulo "O modelo de dados de Python", o público principal deste livro não terá problema em pular diretamente para qualquer outra parte, mas muitas vezes assumo que você leu os capítulos precedentes de cada parte específica. Pense nas partes [Parte I: Estruturas de dados](../2-volume-1/1-parte-i-estruturas-de-dados/01-o-modelo-de-dados-em-python.md) até a [Parte V: Metaprogramação](../4-volume-3/parte-v-metaprogramacao/22-atributos-dinamicos-e-propriedades.md) como cinco livros dentro do livro.

Tentei enfatizar o uso de classes e módulos que já existem antes de discutir como criar seus próprios. Por exemplo, na [Parte I: Estruturas de dados](../2-volume-1/1-parte-i-estruturas-de-dados/02-uma-colecao-de-sequencias.md), o [Capítulo 2](../2-volume-1/1-parte-i-estruturas-de-dados/02-uma-colecao-de-sequencias.md) trata dos tipos de sequências que estão prontas para serem usadas, incluindo algumas que não recebem muita atenção, como `collections.deque`. Criar sequências definidas pelo usuário só é discutido na [Parte III: Classes e Protocolos](../3-volume-2/1-parte-iii-classes-e-protocolos/12-metodos-especiais-para-sequencias.md), onde também vemos como usar as classes base abstratas (ABCs) de `collections.abc`. Criar suas próprias ABCs é discutido ainda mais tarde, na [Parte III: Classes e Protocolos](../3-volume-2/1-parte-iii-classes-e-protocolos/), pois acredito na importância de estar confortável usando uma ABC antes de escrever uma.

Essa abordagem tem algumas vantagens. Primeiro, saber o que está disponivel para uso imediato pode evitar que você reinvente a roda. Usamos as classes de coleções existentes com mais frequência que implementamos nossas próprias coleções, e podemos prestar mais atenção ao uso avançado de ferramentas prontas, adiando a discussão sobre a criação de novas ferramentas. Também é mais provável herdar de ABCs existentes que criar uma nova ABC do zero. E, finalmente, acredito ser mais fácil entender as abstrações após vê-las em ação.

A desvantagem dessa estratégia são as referências a pontos futuros espalhadas pelo livro. Espero que isso seja mais fácil de tolerar agora que você sabe porque escolhi esse caminho.

### Abordagem "mão na massa"

Frequentemente usaremos o console interativo de Python para explorar a linguagem e as bibliotecas. Acho isso importante para enfatizar o poder dessa ferramenta de aprendizagem, especialmente para quem teve mais experiência com linguagens estáticas compiladas, que não oferecem um REPL.[[2](../5-postfacio/footnote.md#L2)]

Um dos pacotes padrão de testagem de Python, o [`doctest`](https://docs.python.org/3/library/doctest.html), funciona simulando sessões de console e verificando se as expressões resultam nas resposta exibidas. Usei doctest para verificar a maior parte do código desse livro, incluindo as listagens do console. Não é necessário usar ou sequer saber da existência do `doctest` para acompanhar o texto: a principal característica dos _doctests_ é que eles imitam transcrições de sessões interativas no console de Python, assim qualquer pessoa pode reproduzir as demonstrações facilmente.

Algumas vezes vou explicar o que queremos realizar mostrando um _doctest_ antes do código que implementa a solução. Estabelecer precisamente o quê deve ser feito, antes de pensar sobre como fazer, ajuda a focalizar nosso esforço de codificação. Escrever os testes previamente é a base de desenvolvimento dirigido por testes (TDD, _test-driven development_), e também acho essa técnica útil para ensinar.

Também escrevi testes unitários para alguns dos exemplos maiores usando _pytest_ que acho mais fácil de usar e mais poderoso que o módulo _unittest_ da biblioteca padrão. Você vai descobrir que pode verificar a maior parte do código do livro digitando `python3 -m doctest example_script.py` ou `pytest` no console de seu sistema operacional. A configuração do _pytest.ini_, na raiz do [repositório do código de exemplo](https://github.com/fluentpython/example-code-2e), assegura que _doctests_ são coletados e executados pelo comando `pytest`.

### Ponto de vista: minha perspectiva pessoal

Venho usando, ensinando e debatendo Python desde 1998, e gosto de estudar e comparar linguagens de programação, seus projetos e a teoria por trás delas. Ao final de alguns capítulos acrescentei uma seção "Ponto de vista", apresentando minha perspectiva sobre Python e outras linguagens. Você pode pular essas partes, se não tiver interesse em tais discussões. Seu conteúdo é inteiramente opcional.

### Conteúdo na Web

Criei dois sites para este livro:

- [https://pythonfluente.com](https://pythonfluente.com)
  O texto integral em português traduzido por Paulo Candido de Oliveira Filho. É que você está lendo agora.

- [https://fluentpython.com](https://fluentpython.com)
  Contém textos em inglês complementando as duas edições do livro, além de um glossário. Tive que colocar esse conteúdo online para não ultrapassar o limite de 1.000 páginas.

O repositório de exemplos de código está no [GitHub](https://github.com/fluentpython/example-code-2e).

### Convenções usadas no livro

As seguintes convenções tipográficas são usadas neste livro:

- _Itálico_
  Indica novos termos, URLs, endereços de e-mail, nomes e extensões de arquivos[[3](../5-postfacio/footnote.md#L3)].

- `Espaçamento constante`
  Usado para listagens de programas, bem como dentro de parágrafos para indicar elementos programáticos tais como nomes de variáveis ou funções, bancos de dados, tipos de dados, variáveis do ambiente, instruções e palavras-chave.
  
  Observe que quando uma quebra de linha cai dentro de um termo de `espaçamento constante`, o hífen não é utilizado—​pois ele poderia ser erroneamente entendido como parte do termo.

- **`Espaçamento constante em negrito`**
  Mostra comandos ou outro texto que devem ser digitados literalmente pelo usuário.

- _`Espaçamento constante em itálico`_
  Mostra texto que deve ser substituído por valores fornecidos pelo usuário ou por valores determinados pelo contexto.

💡 - Esse elemento é uma dica ou sugestão.
ℹ️ - Este elemento é uma nota ou observação.
⚠️ - Este elemento é um aviso ou alerta.

### Usando os exemplos de código

Todos os scripts e a maior parte dos trechos de código que aparecem no livro estão disponíveis no repositório de código de Python Fluente, [no GitHub](https://github.com/fluentpython/example-code-2e).

Se você tiver uma questão técnica ou algum problema para usar o código, por favor mande um e-mail para [bookquestions@oreilly.com](bookquestions@oreilly.com).

Esse livro existe para ajudar você a fazer seu trabalho. Em geral, se o código exemplo está no livro, você pode usá-lo em seus programas e na sua documentação. Não é necessário nos contactar para pedir permissão, a menos que você queira reproduzir uma parte significativa do código. Por exemplo, escrever um programa usando vários pedaços de código deste livro não exige permissão. Vender ou distribuir exemplos de livros da O’Reilly exige permissão. Responder uma pergunta citando este livro e código exemplo daqui não exige permissão. Incorporar uma parte significativa do código exemplo do livro na documentação de seu produto exige permissão.

Gostamos, mas em geral não exigimos, atribuição da fonte. Isto normalmente inclui o título, o autor, a editora e o ISBN. Por exemplo, “_Python Fluente, 2ª ed._, de Luciano Ramalho. Copyright 2022 Luciano Ramalho, 978-1-492-05635-5.”

Se você achar que seu uso dos exemplo de código está fora daquilo previsto na lei ou das permissões dadas acima, por favor entre em contato com [permissions@oreilly.com](permissions@oreilly.com).

### O’Reilly Online Learning

> ℹ️ Por mais de 40 anos, [O’Reilly Media](https://www.oreilly.com/) tem oferecido treinamento, conhecimento e ideias sobre tecnologia e negócios, ajudando empresas serem bem sucedidas.

Nossa rede sem igual de especialistas e inovadores compartilha conhecimento e sabedoria através de livros, artigos e de nossa plataforma online de aprendizagem. A plataforma de aprendizagem online da O’Reilly oferece acesso sob demanda a treinamentos ao vivo, trilhas de aprendizagem profunda, ambientes interativos de programação e uma imensa coleção de textos e vídeos da O’Reilly e de mais de 200 outras editoras. Para mais informações, visite [http://oreilly.com](http://oreilly.com).

### Como entrar em contato

Por gentileza, envie comentários e perguntas sobre esse livro para o editor:

```
O’Reilly Media, Inc.
1005 Gravenstein Highway North
Sebastopol, CA 95472
800-998-9938 (in the United States or Canada)
707-829-0515 (international or local)
707-829-0104 (fax)
```

Há uma página online para o original em inglês deste livro, com erratas e informação adicional, que pode ser acessada aqui: [https://fpy.li/p-4](https://fpy.li/p-4).

Envie e-mail para [bookquestions@oreilly.com](bookquestions@oreilly.com), com comentários ou dúvidas técnicas sobre o livro.

Novidades e informações sobre nossos livros e cursos podem ser encontradas em [http://oreilly.com](http://oreilly.com).

### Agradecimentos

Eu não esperava que atualizar um livro de Python cinco anos depois fosse um empreendimento de tal magnitude. Mas foi. Marta Mello, minha amada esposa, sempre esteve ao meu lado quando precisei. Meu querido amigo Leonardo Rochael me ajudou desde os primeiros rascunhos até a revisão técnica final, incluindo consolidar e revisar as sugestões dos outros revisores técnicos, de leitores e de editores. Honestamente, não sei se teria conseguido sem seu apoio, Marta e Leo. Muito, muito grato!

Jürgen Gmach, Caleb Hattingh, Jess Males, Leonardo Rochael e Miroslav Šedivý formaram a fantástica equipe de revisores técnicos da segunda edição. Eles revisaram o livro inteiro. Bill Behrman, Bruce Eckel, Renato Oliveira e Rodrigo Bernardo Pimentel revisaram capítulos específicos. Suas inúmeras sugestões, vindas de diferentes perspectivas, tornaram o livro muito melhor.

Muitos leitores me enviaram correções ou fizeram outras contribuições durante o pré-lançamento, incluindo: Guilherme Alves, Christiano Anderson, Konstantin Baikov, K. Alex Birch, Michael Boesl, Lucas Brunialti, Sergio Cortez, Gino Crecco, Chukwuerika Dike, Juan Esteras, Federico Fissore, Will Frey, Tim Gates, Alexander Hagerman, Chen Hanxiao, Sam Hyeong, Simon Ilincev, Parag Kalra, Tim King, David Kwast, Tina Lapine, Wanpeng Li, Guto Maia, Scott Martindale, Mark Meyer, Andy McFarland, Chad McIntire, Diego Rabatone Oliveira, Francesco Piccoli, Meredith Rawls, Michael Robinson, Federico Tula Rovaletti, Tushar Sadhwani, Arthur Constantino Scardua, Randal L. Schwartz, Avichai Sefati, Guannan Shen, William Simpson, Vivek Vashist, Jerry Zhang, Paul Zuradzki e outros que pediram para não ter seus nomes mencionados, enviaram correções após a entrega da versão inicial ou foram omitidos porque eu não registrei seus nomes mil desculpas.

Durante minha pesquisa, aprendi sobre tipagem, concorrência, pattern matching e metaprogramação interagindo com Michael Albert, Pablo Aguilar, Kaleb Barrett, David Beazley, J. S. O. Bueno, Bruce Eckel, Martin Fowler, Ivan Levkivskyi, Alex Martelli, Peter Norvig, Sebastian Rittau, Guido van Rossum, Carol Willing e Jelle Zijlstra.

Os editores da O’Reilly Jeff Bleiel, Jill Leonard e Amelia Blevins fizeram sugestões que melhoraram o fluxo do texto em muitas partes. Jeff Bleiel e o editor de produção Danny Elfanbaum me apoiaram durante essa longa maratona.

As ideias e sugestões de cada um deles tornaram o livro melhor e mais preciso. Inevitavelmente, vão restar erros de minha própria criação no produto final. Me desculpo antecipadamente.

Por fim gostaria de estender meus sinceros agradecimento a meus colegas na Thoughtworks Brasil e especialmente a meu mentor, Alexey Bôas que apoiou este projeto de muitas formas até o fim.

Claro, todos os que me ajudaram a entender Python e a escrever a primeira edição merecem agora agradecimentos em dobro. Não haveria segunda edição sem o sucesso da primeira.

### Sobre esta tradução

_Python Fluente, 2ª Edição_ é uma tradução direta de _Fluent Python, Second Edition (O’Reilly, 2022)_. Não é uma obra derivada de _Python Fluente_ (Novatec, 2015).

A presente tradução foi autorizada pela O’Reilly Media para distribuição nos termos da licença [CC BY-NC-ND](fpy.li/4j). Os arquivos-fonte em formato _Asciidoc_ estão no repositório público [https://github.com/pythonfluente/pythonfluente2e](https://github.com/pythonfluente/pythonfluente2e).

Enquanto publicávamos a tradução ao longo de 2023, muitas correções foram enviadas por leitores como _issues_ (defeitos) ou _pull requests_ (correções) no [repositório](https://github.com/pythonfluente/pythonfluente2e). Agradeceço a todas as pessoas que colaboraram!

> ℹ️ Correções e sugestões de melhorias são bem vindas! Para contribuir, veja os _[issues](https://github.com/pythonfluente/pythonfluente2e/issues)_ no repositório [https://github.com/pythonfluente/pythonfluente2e](https://github.com/pythonfluente/pythonfluente2e).

Contamos com sua colaboração. 🙏

### Histórico das traduções

Escrevi a primeira e a segunda edições deste livro originalmente em inglês, para serem mais facilmente distribuídas no mercado internacional.

Cedi os direitos exclusivos para a O’Reilly Media, nos termos usuais de contratos com editoras famosas: elas ficam com a maior parte do lucro, o direito de publicar, e o direito de vender licenças para tradução em outros idiomas.

Até 2022, a primeira edição foi publicada nesses idiomas:

1. inglês,
2. português brasileiro,
3. chinês simplificado (China),
4. chinês tradicional (Taiwan),
5. japonês,
6. coreano,
7. russo,
8. francês,
9. polonês.

A ótima tradução PT-BR foi produzida e publicada no Brasil pela Editora Novatec em 2015, sob licença da O’Reilly.

Entre 2020 e 2022, atualizei e expandi bastante o livro para a segunda edição. Sou muito grato à liderança da [Thoughtworks Brasil](https://www.thoughtworks.com/pt-br) por terem me apoiado enquanto passei a maior parte de 2020 e 2021 pesquisando, escrevendo, e revisando esta edição.

Quando entreguei o manuscrito para a O’Reilly, negociei um adendo contratual para liberar a tradução da segunda edição em PT-BR com uma licença livre, como uma contribuição para comunidade Python lusófona.

A O’Reilly autorizou que essa tradução fosse publicada sob a licença CC BY-NC-ND: [Creative Commons — Atribuição-NãoComercial-SemDerivações 4.0 Internacional](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en). Com essa mudança contratual, a Editora Novatec não teve interesse em traduzir e publicar a segunda edição.

Felizmente encontrei meu querido amigo Paulo Candido de Oliveira Filho (PC). Fomos colegas do ensino fundamental ao médio, e depois trabalhamos juntos como programadores em diferentes momentos e empresas. Hoje ele presta serviços editoriais, inclusive faz traduções com a excelente qualidade desta aqui.

Contratei PC para traduzir. Estou fazendo a revisão técnica, gerando os arquivos HTML com [Asciidoctor](https://asciidoctor.org/) e publicando em [https://PythonFluente.com](https://pythonfluente.com/2/). Estamos trabalhando diretamente a partir do _Fluent Python, Second Edition_ da O’Reilly, sem aproveitar a tradução da primeira edição, cujo copyright pertence à Novatec.

O copyright desta tradução pertence a mim.

_Luciano Ramalho, São Paulo, 13 de março de 2023_