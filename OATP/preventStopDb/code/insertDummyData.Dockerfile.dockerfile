FROM python:3.10.1

RUN apt-get update -y
RUN apt-get -y install cron

WORKDIR cd/etc/apt
RUN echo "deb http://archive.ubuntu.com/ubuntu bionic main restricted universe multiverse" >> sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu bionic-security main restricted universe multiverse" >> sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu bionic-updates main restricted universe multiverse" >> sources.list

COPY pip-requirements.txt ./
RUN pip install --no-cache-dir -r pip-requirements.txt

RUN mkdir -p /opt/oracle
WORKDIR /opt/oracle
COPY instantclient ./instantclient
RUN chmod -R 777 ./instantclient
RUN apt-get install libaio1
RUN sh -c "echo /opt/oracle/instantclient/instantclient_21_8 > /etc/ld.so.conf.d/oracle-instantclient.conf"
RUN ldconfig
RUN export LD_LIBRARY_PATH=/opt/oracle/instantclient/instantclient_21_8:$LD_LIBRARY_PATH

WORKDIR /usr/src/app
RUN chmod -R 777 /usr/src/app
COPY instantclient ./instantclient

COPY insertDummyData_linux.py .
RUN python insertDummyData_linux.py 3600