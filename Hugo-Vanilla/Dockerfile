FROM buildpack-deps:bullseye-scm

ARG WORK_DIR=/home/devkit/
ARG GO_VERSION=1.18.1
ARG HUGO_VERSION=0.98.0

ENV GOLANG_VERSION ${GO_VERSION}
ENV PATH /go/bin:/usr/local:/usr/local/go/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends g++ gcc libc6-dev  make pkg-config
RUN mkdir -p "${WORK_DIR}workhome" && cd ${WORK_DIR} && chmod -R 777 "${WORK_DIR}"
RUN wget -O go.tar.gz "https://dl.google.com/go/go${GO_VERSION}.linux-arm64.tar.gz" \
	&& wget -O hugo.tar.gz "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz"
RUN tar -xzf go.tar.gz -C /usr/local && tar -zxf hugo.tar.gz -C /usr/local
RUN rm -rf "/var/lib/apt/lists/*" "hugo.tar.gz" "go.tar.gz"
RUN go version && hugo version

VOLUME ${WORK_DIR}
WORKDIR ${WORK_DIR}workhome