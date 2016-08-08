# NORS Project - The Server #

## Preparing Environment ##

### Building Native Environment ###

$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ cd orders/
(venv) $ ./run.py
(venv) $ deactivate

### Building a Container ###

You will need docker installed. For Ubuntu 14.04:

$ sudo apt-get update && sudo apt-get install docker.io

Build the container:

$ cd /path_to_nors/server
$ docker build --rm -t nors .

Run the container:

$ docker run -ti -P --rm nors
