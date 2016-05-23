#!/usr/bin/env python3

import connexion

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'NORS project rest API documentation.\n\nLearn about NORS on [Github](http://www.github.com/dmazzer/nors).\n\nFor this sample, you can use the api key `special-key` to test the authorization filters\n'})
    app.run(port=8080, debug=True)
