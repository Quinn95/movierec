# what2watch

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
pip install -r requirements.txt
./manage.py migrate
./manage.py makemigrations movierec
./manage.py migrate
./manage.py loaddata sites
./manage.py runserver
```
