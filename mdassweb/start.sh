#!/usr/bin/env bash
 nohup ~/Env/py3env/bin/gunicorn -b 0.0.0.0:9000 --workers=2 mdassweb.wsgi:application &
