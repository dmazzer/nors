# This file is part of NORS project.
# http://github.com/dmazzer/nors

FROM ubuntu:14.04

MAINTAINER Daniel Mazzer "dmazzer@gmail.com"

EXPOSE 9270

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update && \
	apt-get install -y \
	git \
	python3 \
	python3-pip && \
	apt-get clean

#RUN pip install virtualenv

# Make ssh dir
RUN mkdir /root/.ssh/

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

CMD ./nors_srv.py -c nors.conf
