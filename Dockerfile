FROM python:3.9-alpine3.18

RUN wget https://releases.hashicorp.com/terraform/1.7.3/terraform_1.7.3_linux_amd64.zip
RUN unzip terraform_1.7.3_linux_amd64.zip
RUN mv terraform /usr/bin/terraform

RUN apk add --no-cache build-base libffi-dev python3-dev openssl-dev

RUN pip install 'ansible[azure]'

RUN ansible-galaxy role install geerlingguy.docker

RUN apk update && apk add openssh-client

COPY . /app

WORKDIR /app

RUN tar -czvf ./inception.tar.gz ./inception

CMD ["python3", "src/main.py"]