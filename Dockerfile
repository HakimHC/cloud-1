FROM python:latest


RUN apt-get update && apt-get install -y gnupg software-properties-common

RUN   wget -O- https://apt.releases.hashicorp.com/gpg | \
      gpg --dearmor | \
      tee /usr/share/keyrings/hashicorp-archive-keyring.gpg

RUN  echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
      tee /etc/apt/sources.list.d/hashicorp.list

RUN  apt update

RUN  apt-get install -y terraform

RUN pip install 'ansible[azure]'

RUN ansible-galaxy role install geerlingguy.docker

COPY . /app

WORKDIR /app

RUN tar -czvf ./inception.tar.gz ./inception

CMD ["python3", "src/main.py"]