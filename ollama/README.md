# Ollama - LLMs for all

## Running Ollama on your own server

```
curl https://ollama.ai/install.sh | sh

ollama pull llama3

service ollama stop

nohup env OLLAMA_HOST=0.0.0.0:11434 ollama serve

docker run -d -p 3000:8080 --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main

```

## Open WebUI

To run the WebUI:
```
docker run -d  --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Now, go to the http://ip:8080

Referencias

- https://github.com/open-webui/open-webui
- https://dev.to/ajeetraina/the-ollama-docker-compose-setup-with-webui-and-remote-access-via-cloudflare-1ion#:~:text=You%20can%20access%20the%20web%20interface%20at%20http%3A%2F%2Flocalhost%3A8080,to%20access%20the%20web%20interface%20remotely%20through%20Cloudflare.
- https://thoughtbot.com/blog/how-to-use-open-source-LLM-model-locally