ARG base=20.04
FROM ubuntu:${base}

# Initialize build
ARG script_path=/tmp/devcont-scripts
RUN mkdir -p ${script_path}

ADD root/usr/bin/*devcont* /usr/bin/
SHELL ["/usr/bin/with-devcontenv", "bash", "-c"]

ARG ubuntu_archive_url
ADD scripts/set-archive.sh ${script_path}/set-archive.sh
RUN ${script_path}/set-archive.sh

# Install packages
ADD scripts/install-common.sh ${script_path}/install-common.sh
RUN ${script_path}/install-common.sh

ARG use_openssh_server=false
ADD scripts/install-openssh-server.sh ${script_path}/install-openssh-server.sh
RUN if [ "${use_openssh_server}" = true ]; then \
        ${script_path}/install-openssh-server.sh; \
    fi

ARG use_build_essential=false
ADD scripts/install-build-essential.sh ${script_path}/install-build-essential.sh
RUN if [ "${use_build_essential}" = true ]; then \
        ${script_path}/install-build-essential.sh; \
    fi

ADD root/ /
ENTRYPOINT ["sleep", "infinity"]
