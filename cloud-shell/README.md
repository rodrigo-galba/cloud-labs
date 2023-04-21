docker build . -t cloud-shell
docker run -v ${PWD}:/data -it cloud-shell
