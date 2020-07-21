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
