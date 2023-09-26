## 1 Install required libraries
```bash
 pip install -r requirements.txt
```
## 2 Connect existing database
Replace these lines in settings with desired database
```python
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'OrdersAPI', 
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```
## 3 Make migrations and migrate database
```bash
python manage.py makemigrations
python manage.py migrate
```
## 4 run server
```bash
python manage.py runserver
```