#!/usr/bin/env bash
 nohup ~/Env/py3env/bin/gunicorn -b 0.0.0.0:9090 --workers=2 IncMiGe.wsgi:application &
