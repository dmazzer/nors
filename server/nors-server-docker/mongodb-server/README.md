# NORS Project - MongoDB Server Container #

## Preparing Environment ##

Install Docker as instructed [here](https://docs.docker.com/engine/installation/linux/ubuntulinux/)

For Ubuntu 14.04:

```
$ sudo apt-get update
$ sudo apt-get install apt-transport-https ca-certificates
$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
```

Insert the above line in file `/etc/apt/sources.list.d/docker.list`:

```
deb https://apt.dockerproject.org/repo ubuntu-trusty main
```

Then:

```
$ sudo apt-get update
$ sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
$ sudo apt-get install docker-engine
$ sudo service docker start
```

### Building a Container ###

Build the container:

```
$ cd /path_to_nors/mongodb-server
$ docker build --rm -t nors-mongodb .
```

Run the container:

This command will start the mongodb server mapping the container port 27017 to host port 47017

```
$ docker run -d -ti --name=nors-mongodb --rm -p 47017:27017 nors-mongodb
```

Access mongodb-server to test the container:

```
$ mongo localhost:47017
```

