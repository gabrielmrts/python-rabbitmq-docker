# Rabbit MQ implementado com Python

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/gabrielmrts/python-rabbitmq-docker?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/gabrielmrts/python-rabbitmq-docker?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/gabrielmrts/python-rabbitmq-docker?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/gabrielmrts/python-rabbitmq-docker?style=for-the-badge)

> A ideia desse projeto é exemplificar como fazer a implementação do RabbitMQ com Python e Docker

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Ter instalada a versão mais recente do `Docker & Docker compose`

## 🚀 Instalando esse projeto

Para instalar o projeto, siga estas etapas:

```
docker-compose up -d --build (para buildar e iniciar o RabbitMQ)
```

## ☕ Usando o projeto

Para usar o projeto, siga estas etapas:

```
Primeiro: execute o receiver.py (python3 receiver.py) para iniciar um canal.
Segundo: execute o publisher.py (python3 publisher.py) para públicar no canal que o receiver.py está usando
```

## 📫 Contribuindo para este projeto
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin python-rabbitmq-docker / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
