Django signals are used to trigger actions automatically when certain events occur, such as saving a model. In this project, signals were used to study their behavior by adding a delay and observing the output. It was found that Django signals execute synchronously, meaning they run immediately and delay the response until completion. It was also observed that signals run in the same thread as the caller and share the same database transaction, as any rollback affects both the main operation and the signal.
Project Setup Steps:
1. Created a Django project using:
django-admin startproject myproject
2. Navigated into the project folder:
cd myproject
3. Created an app:
python manage.py startapp myapp

4. Applied migrations:
python manage.py makemigrations
python manage.py migrate
5. Ran the development server:
python manage.py runserver
