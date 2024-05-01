# Configuração do Projeto de Logging

Este projeto é um script Python simples que gera logs em um diretório especificado por uma variável de ambiente. O script é executado dentro de um contêiner Docker.

## Pré-requisitos

- Docker
- Docker Compose

## Configuração

1. **Clone o repositório**

   Primeiro, clone o repositório para sua máquina local usando git.

   ```bash
   git clone <url_do_repositorio>

2. **Crie o diretório de logs**

   Crie um diretório na sua máquina local onde os logs serão armazenados. Por exemplo:

   ```bash
   mkdir logs
   
3. **Construa e execute o contêiner Docker**

   Navegue até o diretório do projeto e use Docker Compose para construir e executar o contêiner.

   ```bash
   cd <diretorio_do_projeto>
   docker-compose up


O script Python será executado e os logs serão escritos no diretório que você criou.

## Variáveis de Ambiente

Este projeto usa a seguinte variável de ambiente:

- `LOG_DIR` - O diretório onde os logs serão escritos. Este diretório deve ser um volume montado no contêiner Docker.

## Logs

Os logs são escritos no arquivo `app.log` no diretório especificado pela variável de ambiente `LOG_DIR`. O script gera logs de nível INFO, WARNING e ERROR.