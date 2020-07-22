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

Abrindo seu terminal de comando, mude o caminho até chegar na área de trabalho, depois para a pasta do arquivo, e digite Obscrypto.py, apertando Enter em seguida:

![imagem](https://github.com/kyleflick124/Obscrypto/blob/master/caminho.png)
