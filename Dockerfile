FROM alpine:3.4

RUN apk update && apk add python py-pip

ADD . /deployer
RUN pip install -e /deployer
