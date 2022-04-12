# ChallengeX - DESAFIO SOFTWARE ENGINEERING

## Tutorial
<p> Após clonar o repositorio, abra um terminal e <br>
configure suas credenciais da AWS.</p>
<p>Em seguinda excecute os seguintes comandos para<br>
algumas instalar dependencias do projeto.</p>

``` console
$ npm install -g serverless
$ npm i
$ serverless plugin install -n serverless-vpc-discovery
```
<p>Para subir o ambinte serveless para aws</p>

``` console
$ sls deploy
```
<p> Para testar a solução você deve acessar a AWS<br>
Ir no serviço API Gateway, no menu lateral selecione<br>
<strong>Resources</strong>. Expanda até encontrar a<br>
rota POST, em seguinta escolha o metodo Test, adicione<br>
payload ao Request Body e clique em Test.</p>
