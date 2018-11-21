## 3DEMBenchmark Portal

> http://3dembenchmark.i2pc.es

## Set up

### Dependencies

```
$ cd 3dembenchmark
$ virtualenv --python /usr/bin/python2 env
$ env/bin/pip install -r requirements.txt
```

## Run

## Development server

```
$ env/bin/python manage.py runserver
```

## Production server (Apache)

```
<VirtualHost *:80>
  ServerName 3dembenchmark.i2pc.es
  Alias /static /home/ubuntu/3dembenchmark/staticfiles

  <Directory /home/ubuntu/3dembenchmark/staticfiles>
    Require all granted
  </Directory>

  <Directory /home/ubuntu/3dembenchmark/main>
    <Files wsgi.py>
      Require all granted
    </Files>
  </Directory>

  WSGIDaemonProcess 3dembenchmark python-home=/home/ubuntu/3dembenchmark/env python-path=/home/ubuntu/3dembenchmark
  WSGIProcessGroup 3dembenchmark
  WSGIScriptAlias / /home/ubuntu/3dembenchmark/main/wsgi.py
</VirtualHost>
```

## Admin interface (requires password)

> http://3dembenchmark.i2pc.es/admin/
