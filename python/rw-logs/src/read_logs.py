import os

# Obter o diretório de logs da variável de ambiente
log_dir = os.getenv('LOG_DIR')

# Nome do arquivo de log
log_file = os.path.join(log_dir, 'app.log')

# Abrir o arquivo de log e imprimir seu conteúdo
with open(log_file, 'r') as f:
    print(f.read())