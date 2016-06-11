#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'production'))
    with app.app_context():
        # create a development user
        if User.objects.first() is None:
            u = User(username = 'admin')
            u.set_password('admin')
            u.save()
    app.debug = True
    app.run()
