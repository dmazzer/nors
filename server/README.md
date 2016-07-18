# NORS Project - The Server #

# Building Python virtual environment #

$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ cd orders/
(venv) $ ./run.py
(venv) $ deactivate

# Building docker container #

On server project folder:

$ docker build --rm -t nors .
$ docker run -ti --rm nors



