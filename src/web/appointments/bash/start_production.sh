echo "=> Starting webserver..."
gunicorn --bind 0.0.0.0:5001 -w 8 src.wsgi:application 