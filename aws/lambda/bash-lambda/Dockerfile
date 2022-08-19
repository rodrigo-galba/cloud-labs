# Define function directory
ARG FUNCTION_DIR="/function"

# https://hub.docker.com/layers/python/library/python/buster/images/sha256-3b23675ae178f887643aae1d771d1c550982b23995ea0c866e588fd36c961486?context=explore
ARG RUNTIME_VERSION="buster" 

# Stage 1 - bundle base image + runtime
FROM python${RUNTIME_VERSION}:buster as python-buster

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

# Stage 2 - build function and dependencies
FROM python-buster as build-image

ARG FUNCTION_DIR

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

WORKDIR ${FUNCTION_DIR}
COPY app.py .
COPY task.sh .

# Install the runtime interface client
RUN pip install \
        --target ${FUNCTION_DIR} \
        awslambdaric


COPY requirements.txt .
RUN  pip3 install -r requirements.txt --target .

FROM python:${RUNTIME_VERSION}

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the build image dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
