# This file is part of NORS project.
# http://github.com/dmazzer/nors

FROM ubuntu:14.04

MAINTAINER Daniel Mazzer "dmazzer@gmail.com"

# EXPOSE 27017
EXPOSE 9270

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8


# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

RUN apt-get update && \
	apt-get install -y \
	git \
  mongodb-org \
	python3 \
	python3-pip && \
	apt-get clean


# Update apt-get sources AND install MongoDB
# RUN apt-get update && apt-get install -y mongodb-org
# RUN apt-get update && apt-get install -y mongodb-org=3.0.1 mongodb-org-server=3.0.1 mongodb-org-shell=3.0.1 mongodb-org-mongos=3.0.1 mongodb-org-tools=3.0.1

#RUN pip install virtualenv

# Make ssh dir
RUN mkdir /root/.ssh/

# Create the MongoDB data directory
VOLUME /data/db
# RUN mkdir -p /data/db
RUN chown mongodb:mongodb /data -R

# MongoDB related environment defines
ENV AUTH yes
ENV STORAGE_ENGINE wiredTiger
ENV JOURNALING yes

COPY run.sh /run.sh
COPY set_mongodb_password.sh /set_mongodb_password.sh

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/nors && \
    echo "nors:x:${uid}:${gid}:nors,,,:/home/nors:/bin/bash" >> /etc/passwd && \
    echo "nors:x:${uid}:" >> /etc/group && \
    echo "nors ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/nors && \
    chmod 0440 /etc/sudoers.d/nors && \
    chown ${uid}:${gid} -R /home/nors

USER nors
ENV HOME /home/nors

# Clone the conf files into the docker container
RUN git clone https://github.com/dmazzer/nors.git $HOME/app/nors
WORKDIR $HOME/app/nors
RUN git checkout develop

WORKDIR $HOME/app/nors/server
RUN sudo pip3 install -r requirements.txt

CMD /run.sh && git pull origin develop && ./nors_srv.py -c nors.conf
#ENTRYPOINT ["/usr/bin/mongod"]
