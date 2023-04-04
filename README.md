# CadastroDeAlunos


REQUISITOS:
O programa deve oferecer as opções de INSERIR para cadastrar (gravar em arquivo) as
informações dos alunos e EXIBIR para apresentar em tela (após ler do arquivo) todas as
informações de todos os alunos cadastrados. REMOVER um determinado aluno. No caso,
solicitando ao usuário o número de matrícula ou o nome do aluno. Se houver um registro do
aluno no arquivo que corresponda ao dado solicitado, o registro (todas as informações do
aluno) deverá ser apagado do arquivo, mantendo todos os outros registros. Por fim, o
programa deve apresentar uma opção de SAIR para que a execução do programa seja
finalizada.
As informações que o programa deve solicitar para que o usuário digite para cada aluno são:
Nome, Rua, Número, Bairro, Cidade, UF, Telefone, e-mail. Existe mais uma informação que é o
Número de Matrícula, porém o sistema deve gerar este número em sequência a partir do
último existente, de forma automática. Decida qual tipo de variável utilizar para cada dado.
Utilize a ideia de modularização (crie funções). Use os dicionários (dict), vetores (list). Grave
todas as informações em arquivo (pandas dataframe). Crie um menu com as opções que o
usuário pode escolher :
1- INSERIR
2- EXIBIR
3- REMOVER
4- SAIR
Este menu deve ficar dentro de um loop, que termina somente se o usuário seleciona a opção
de “SAIR”. Exemplo: Se o usuário digitar 1, o script deve chamar uma função de inserir os
dados, que permite que o usuário digite as informações. Depois que o usuário informou os
dados e a função inserir finalizou a execução, o script irá apresentar o menu novamente para
que o usuário possa escolher uma nova opção. Toda vez o que programa for executado, ele
deve ler as informações dos alunos que já foram salvas anteriormente. Isto é, se o usuário
cadastrou um aluno por dia, o programa sempre inicia com os alunos já cadastrados. O
registro só é apagado se o usuário escolher a opção de remover.
