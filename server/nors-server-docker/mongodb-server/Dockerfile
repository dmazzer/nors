# This file is part of NORS project.
# http://github.com/dmazzer/nors

FROM ubuntu:14.04

MAINTAINER Daniel Mazzer "dmazzer@gmail.com"

EXPOSE 27017
EXPOSE 28017

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8


# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

RUN apt-get update && \
	apt-get install -y \
	mongodb-org && \
	apt-get clean


# Create the MongoDB data directory
VOLUME /data/db

#RUN chown mongodb:mongodb /data -R

# MongoDB related environment defines
ENV AUTH yes
ENV STORAGE_ENGINE wiredTiger
ENV JOURNALING yes

COPY run.sh /run.sh
COPY set_mongodb_password.sh /set_mongodb_password.sh

WORKDIR /data

ENTRYPOINT ["/usr/bin/mongod"]
