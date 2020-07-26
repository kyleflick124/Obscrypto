# Obscrypto
Um repositório para guardar os passos e ideias que tive para fazer o programa Obscrypto, que usa de um grande processo de criptografia para criar senhas de alta segurança.
Projeto desenvolvido para o primeiro semestre de 2020 (2020/1) do HackoonSpace.

## Conceito do Projeto:
O Projeto foi desenvolvido mais como uma introdução para mim mesmo ao mundo da criptografia e segurança. Embora fazer uma senha pessoal pareça ser algo extremamente seguro e pessoal, existem diversos softwares, maliciosos ou não, que conseguem obter quaisquer senhas em questão de horas. Sabendo disso, uma solução fácil porém nada agradável a um usuário da internet seria fazer uma senha com cada vez mais e mais caracteres "aleatórios". Pelos conceitos básicos da matemática aplicados em combinações, aumentar apenas um caractere em uma senha já aumenta consideravelmente o número de possíveis senhas, como observado a seguir:

![Imagem](https://github.com/kyleflick124/Obscrypto/blob/master/combina%C3%A7%C3%B5es.png)

Como pode ser visto, existem enormes possibilidades de senhas apenas com números e letras minúsculas, e caso fosse usado um número infinito de caracteres, quem sabe infinitas possibilidades existiriam?

No entanto, você poderia estar se perguntando: Como então tantas pessoas são hackeadas em tantos sites que se dizem seguros, se existem tantas possibilidades de senha assim?

A resposta para isso está no jeito que criamos senhas: Não fazemos senhas com caracteres aleatórios pois precisamos lembrar da senha para usá-la em algum lugar. Por exemplo, é bem mais fácil lembrar da senha iloveyou ou nicole123 do que 1ft3kr5t648ref5 ou qualquer outra senha desse tipo. Assim, os softwares de força bruta (tentar descobrir as senhas por tentativa e erro em massa) costumam usar wordlists como a rockyou.txt pois possuem senhas comuns, usadas por muitas pessoas por serem fáceis de serem lembradas ou conterem uma palavra existente em algum idioma.

Pensando nisso, meu projeto de criptografia obscura busca mostrar um "novo" caminho de tornar as senhas cada vez mais seguras: A partir do fornecimento de uma palavra ou de uma senha comum usada por alguma pessoa, criptografar as senhas de uma forma que façam uma cadeia consideravelmente grande de caracteres "aleatórios" gerado a partir dessa palavra, usando diferentes métodos de criptografia para tal.

## Pré-requisitos e recursos utilizados:

A programação foi feita 100% em python, tudo que é necessário é ter uma versão do python 3, recomendo que seja a mais recente.
A interface do programa foi construída dentro do código, com a importação de uma biblioteca já existente no python chamada Tkinter, os usos e implementações podem ser conferidos [aqui](http://effbot.org/tkinterbook/).

## Passo a passo:

1.Estudei um pouco como funcionava a biblioteca do Tkinter e como eu poderia usar para deixar meu programa simples e agradável

2.Estudei alguns tipos de criptografia que geram números não importando a senha inserida, para que qualquer senha possa ser usada mesmo levando em conta caracteres especiais, gerando como se fosse um padrão/base para não dar conflito com os diferentes tipos de criptografia.

3.Implementei esses tipos em uma sequência que gerasse uma longa cadeia de caracteres bem encriptados, parecendo como "aleatórios"

4.Depois, adaptei tudo para as funcionalidades do Tkinter, como um botão chamar uma função, exibir as caixas de texto, etc.

## Instalação:

Após instalar o python, usando o GitHub pelo seu browser, clique no botão verde "Code" e em "Download ZIP". Após a conclusão do download, extraia a pasta para a sua área de trabalho.

## Execução:

Existem 2 modos mais fáceis de executar o programa:

1. O jeito mais fácil é clicando duplamente no programa Obscrypto.py, na pasta dos arquivos. 

![imagem](https://github.com/kyleflick124/Obscrypto/blob/master/pasta.png)

Normalmente, o programa deveria ser executado do segundo modo, mas uma propriedade do Tkinter faz o programa continuar rodando até que seja fechado, então o primeiro modo também é válido.

2. Abrindo seu terminal de comando, mude o caminho até chegar na área de trabalho, depois para a pasta do arquivo, e digite Obscrypto.py, apertando Enter em seguida:

![imagem](https://github.com/kyleflick124/Obscrypto/blob/master/caminho.png)

Isso abrirá automaticamente o programa, siga as instruções exibidas na interface dele para usá-lo.

## Bugs/problemas conhecidos:

Por enquanto não há nenhum bug visual ou de sintaxe no programa que eu tenha percebido, mas qualquer problema com o programa basta mandar uma mensagem por email ou pelo discord/whatsapp do [HackoonSpace](https://hackoonspace.com) caso faça parte.

## Autores:
* Fernando Favareto Abromovick ([kyleflick124](https://github.com/kyleflick124))

## Demais anotações e referências:

* Uma boa parte do programa está comentado, o que ajuda as pessoas a entenderem como cada parte funciona sem precisar de explicação.

* Os métodos de criptografia usados para converter a senha foram, nesta ordem, ascii, octal e base64.

* Um dos vídeos que mais me ajudou a entender como funciona o Tkinter foi [esse](https://youtu.be/JrWHyqonGj8), disponível em inglês, feito por Robert Jomar Malate e pelo curso de Harvard CS50, que inclusive recomendo muito [o canal deles](https://www.youtube.com/channel/UCcabW7890RKJzL968QWEykA) para quem quer aprender programação de maneira interativa, o conteúdo é todo em inglês mas a maioria das coisas possuem legenda em português.

## Imagens e Screenshots do programa:

Menu Principal:

![imagem](https://github.com/kyleflick124/Obscrypto/blob/master/menuprincipal.png)

Programa rodando:

![imagem](https://github.com/kyleflick124/Obscrypto/blob/master/programa.png)

