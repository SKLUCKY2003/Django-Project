Django signals are used to trigger actions automatically when certain events occur, such as saving a model. In this project, signals were used to study their behavior by adding a delay and observing the output. It was found that Django signals execute synchronously, meaning they run immediately and delay the response until completion. It was also observed that signals run in the same thread as the caller and share the same database transaction, as any rollback affects both the main operation and the signal.

Project Setup Steps:
1. Created a Django project using:

django-admin startproject myproject

2. Navigated into the project folder:
   
cd myproject

4. Created an app:
   
python manage.py startapp myapp

6. Applied migrations:
   
python manage.py makemigrations

python manage.py migrate

8. Ran the development server:
   
python manage.py runserver

Results

<img width="652" height="329" alt="image" src="https://github.com/user-attachments/assets/869e1a1b-e6b7-4c07-bf74-fe8eb555ed11" />

<img width="794" height="404" alt="image" src="https://github.com/user-attachments/assets/8bb33691-c671-4123-999c-49c9fbea28af" />

<img width="804" height="643" alt="image" src="https://github.com/user-attachments/assets/f6499972-fceb-4e99-abe2-f79f8b822fdc" />

<img width="804" height="369" alt="image" src="https://github.com/user-attachments/assets/9979b2b8-5ff6-4542-a8e8-616c04778d34" />










