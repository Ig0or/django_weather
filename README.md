# Django Weather
Projeto de estudo feito em Python utilizando o Framework Django e a API de clima do OpenWeather.

![](https://github.com/Ig0or/django_weather/blob/main/app/static/app/img/img.png)

## Rodando a Aplicação
Baixe o repositório e crie um novo ambiente virtual -> `virtualenv venv`

Ative o ambiente virtual -> `.\venv\Scripts\activate`

Instale as dependencias necessárias -> `pip install -r requirements.txt`

Para utilizar a API de clima é necessário uma key de acesso, para isso crie uma conta em https://openweathermap.org/api e a key será enviada por e-mail.

Dentro da pasta `app` crie um arquivo chamado `key.py` com sua key de acesso -> `key = 'sua key'`

Agora é só rodar o servidor -> `python.exe .\manage.py runserver`

## Observações
A API usa a lingua inglesa, portanto para realizar alguma pesquisa o nome das cidades devem estar nesse mesmo formato.

As consultas ficam salvas apenas no servidor, após encerrar o servidor as informaçõoes serão perdidas.
