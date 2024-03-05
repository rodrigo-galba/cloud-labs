# Ngrok

## Instalation

**Linux**
Install ngrok via Apt with the following command:
```
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```
Run the following command to add your authtoken to the default ngrok.yml configuration file.
```
ngrok config add-authtoken <token>
```

### Deploy yout app online

**Ephemeral domain**
Put your app online at ephemeral domain Forwarding to your upstream service. For example, if it is listening on port http://localhost:8080, run: 
```
ngrok http http://localhost:8080
```

Sample app with Nginx
```
$ docker run -it --rm -d -p 8080:80 --name web nginx
```

### Expose ssh access

```
ngrok tcp 22
```
```
ngrok http 46461 \
  --basic-auth "rogal:s3cr3t"
```
To access it:
```
ssh user@ngrok-ip -p randon_port

- https://ngrok.com/docs/agent/ssh-reverse-tunnel-agent/#overview
