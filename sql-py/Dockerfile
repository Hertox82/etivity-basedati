FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/bash"]