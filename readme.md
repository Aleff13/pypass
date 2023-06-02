# PyPass

O PyPass é um sistema para armazenar senhas de forma segura em sua máquina local.Ele consiste basicamente em dois bancos de dados, um com seu usuário de acesso e outro com suas senhas.

O banco de usuários serve para realizar login e garantir que você tenha permissão de acessar o banco de dados com as senhas. O sistema de login funciona com base em um Hash.

O banco de senhas salva as senhas criptografadas utilizando rsa, ou seja você apenas conseguirá salvar senhas e recuperá-las se suas chaves forem compatíveis, por isso é esperado que as guarde com segurança.

## Intalação e uso
Assumindo que você possua o python já instalado.

1. Clone o projeto
2. Acesse a pasta gerada `pypass`
3. Instale o `rsa` com `pip install rsa`
4. Rode o arquivo `pypass.py`, ex.: `$ /bin/python3 ~/pypass/pypass.py`

X. Caso algum erro ocorra, verique se você possui todas as dependências instaladas.

## Forma de utilizar 

Rodar o arquivo pypass.py

Na primeira utilização você deverá inserir um nome de usuário e na sequencia uma senha, que serão utilizadas para o seu login nos próximos acessos.

Após isso, ele irá gerar uma `publicKey.pem` e uma `privateKey.pem`. (guarde elas com segurança elas são sua única forma de recuperar as senhas)

Após realizar o login, irá aparecer uma `lista de opções`
1. Criar nova senha
2. Buscar senha
3. Mostrar todas as senhas
4. sair

## Recomendações de uso
1. Guardar as chaves em um armazenamento externo e importa-las apenas quando for utilizar;
2. Criar um backup em outro armazenamento com suas chaves e seu banco de senhas `passwords.db`

## Fluxo básico

`Login` -> try -> `Acesso no banco users.db` -> try-> `Escolher opção` -> try -> `Carregar chaves` -> try -> `Realizar operação no banco passwords.db`

## Criando um comando personalizado(alias) com bash para iniciar o serviço

1. Acesse seu diretório `~`. ex.: `cd ~`
2. Abra seu arquivo `.bashrc`, ex.: `nano .bashrc`
3. Insira um novo alias, ex.: `alias initDB = '/bin/python3 ~/pypass/pypass.py'`
4. Salve o arquivo e reinicie seu terminal

# Testes unitarios

`python3 -m unittest discover -s tests -p '*_test.py'` 