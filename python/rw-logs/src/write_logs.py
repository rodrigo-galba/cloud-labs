import os
import logging
import time

# Obter o diretório de logs e a duração do script das variáveis de ambiente
log_dir = os.getenv('LOG_DIR')
script_duration = int(os.getenv('SCRIPT_DURATION', 60))  # Valor padrão é 60 segundos

# Criar o diretório de logs se ele não existir
os.makedirs(log_dir, exist_ok=True)

# Configurar o logging para incluir um timestamp
logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Registrar o tempo de início
start_time = time.time()

# Gerar logs pela duração especificada
while time.time() - start_time < script_duration:
    logging.info('Gerando logs...')
    time.sleep(1)  # Pausar por 1 segundo entre cada log

logging.info('Finalizando o script...')
