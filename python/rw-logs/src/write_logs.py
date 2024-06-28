import os
import logging
import logging.handlers
import queue
import time

# Obter o diretório de logs e a duração do script das variáveis de ambiente
log_dir = os.getenv('LOG_DIR')
script_duration = int(os.getenv('SCRIPT_DURATION', 60))  # Valor padrão é 60 segundos

# Criar o diretório de logs se ele não existir
os.makedirs(log_dir, exist_ok=True)

# Criar uma fila para os logs
log_queue = queue.Queue(-1)

# Criar um handler de fila para a fila
queue_handler = logging.handlers.QueueHandler(log_queue)

# Configurar o logging para incluir um timestamp e usar o handler de fila
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[queue_handler]
)

# Criar um handler de arquivo para o arquivo de log
file_handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))

# Criar um listener de fila para o handler de arquivo
queue_listener = logging.handlers.QueueListener(log_queue, file_handler)

# Iniciar o listener de fila
queue_listener.start()

# Registrar o tempo de início
start_time = time.time()

# Gerar logs pela duração especificada
while time.time() - start_time < script_duration:
    logging.info('Gerando logs... Process ID: %s' % os.getpid())  # Incluir o ID do processo na mensagem de log
    time.sleep(1)  # Pausar por 1 segundo entre cada log

logging.info('Finalizando o script... Process ID: %s' % os.getpid())

# Parar o listener de fila
queue_listener.stop()
