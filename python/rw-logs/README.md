# Documentação

## Contexto

Este script foi projetado para ser executado em um ambiente Python 3.6 ou superior. Ele gera logs para um arquivo especificado, com cada mensagem de log incluindo o ID do processo que a gerou.

### Executando o script no Windows Subsystem for Linux (WSL)

Para executar o script no WSL, primeiro navegue até o diretório que contém o script usando o comando `cd`. Por exemplo:

```bash
cd /caminho/para/o/diretorio
```

Em seguida, você pode iniciar duas instâncias do script em paralelo usando o seguinte comando:

```bash
python3 src/write_logs.py & python3 src/write_logs.py &
```

Este comando inicia dois processos em segundo plano que executam o script.

## Configuração
O script usa as seguintes variáveis de ambiente para configuração:

`LOG_DIR`: O diretório onde o arquivo de log será criado. Se não for especificado, o script criará o arquivo de log no diretório atual.  
`SCRIPT_DURATION`: A duração do script em segundos. Se não for especificado, o script será executado por 60 segundos.  

Você pode definir essas variáveis de ambiente antes de executar o script. Por exemplo, no WSL, você pode fazer o seguinte:

```bash
export LOG_DIR=/caminho/para/o/diretorio/de/logs
export SCRIPT_DURATION=120
python script.py & python script.py &
```

Estes comandos definem o diretório de logs e a duração do script, e então iniciam duas instâncias do script em paralelo.

## Lendo o arquivo de log
Para ler o arquivo de log enquanto o script está sendo executado, você pode usar o comando tail. Este comando exibe as últimas linhas de um arquivo e, com a opção -f, você pode acompanhar as alterações no arquivo em tempo real.

### No Windows Subsystem for Linux (WSL)
No WSL, você pode usar o comando tail diretamente. Para acompanhar as alterações no arquivo de log em tempo real, use o seguinte comando:

```bash
cd /cloud-labs/python/rw-logs
tail -f /logs/app.log
```
Este comando exibirá as últimas linhas do arquivo de log e atualizará a saída sempre que novas linhas forem adicionadas ao arquivo.

## Referencia

### Como dois scripts podem gerar logs no mesmo arquivo em paralelo?
Dois scripts podem gerar logs no mesmo arquivo em paralelo usando a biblioteca logging do Python, que é segura para threads. No entanto, se os scripts estiverem em processos separados, você pode encontrar problemas de concorrência ao escrever no arquivo de log.

Para resolver isso, você pode usar um logging.handlers.QueueHandler em combinação com um logging.handlers.QueueListener. Isso permite que vários processos gerem logs para a mesma fila, e um único processo consuma a fila e escreva os logs no arquivo.

