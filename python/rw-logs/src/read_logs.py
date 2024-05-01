import os
import re

# Obter o diretório de logs da variável de ambiente
log_dir = os.getenv('LOG_DIR')


# Nome do arquivo de log
log_file = os.path.join(log_dir, 'app.log')

# Open the log file
with open(log_file, 'r') as file:
    # Read the contents of the file
    log_contents = file.read()

# Define the regex pattern to match the log entries
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) - (.*)'

# Find all matches in the log contents
matches = re.findall(pattern, log_contents)

# Iterate over the matches and print the separated log components
for match in matches:
    asctime = match[0]
    levelname = match[1]
    message = match[2]
    print(f"Asctime: {asctime}, Levelname: {levelname}, Message: {message}")
