# ChallengeX

## Tutorial
<p> Após clonar o repositório, abra um terminal e configure suas credenciais da AWS.<br>
Em seguida execute os seguintes comandos para instalar algumas dependências do projeto.</p>

``` console
$ npm install -g serverless
$ npm i
$ serverless plugin install -n serverless-vpc-discovery
```
<p>Para subir o ambinte <strong>serveless</strong> para AWS:</p>

``` console
$ sls deploy
```
<p> Para testar a solução você deve acessar a AWS no serviço API Gateway, no menu lateral selecione
<strong>Resources</strong>.<br>Expanda até encontrar a rota POST, em seguinta escolha o metodo Test, adicione payload ao Request Body e clique em Test.</p>


## Arquitetura
![alt text](img/architecture.png)