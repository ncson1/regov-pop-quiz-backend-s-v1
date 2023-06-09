# quiz:
`https://github.com/regov-enterprise/pop-quiz-backend-s-v1`

# Use case:
![the picture](./use-case.png)


# Database design:

![the picture](./database-design.png)

# API Flow:

### Student 
```bash
view list course -> /courses GET
enroll course if avaiable -> /courses/enroll POST
drop course enroll if they are in that course, then capa auto update -> /courses/{course_id}/enroll/{enroll_id} PUT
```

### Administrator
```bash
create course + set max capa -> /courses POST
view list course + number of student inside -> /courses GET
view course detail + view student list inside -> /courses/{id} GET
view list drops -> /drops/ GET
```


# Setup:

First of all, you need to run this command to create environment for this project

```bash
`cd project_name`
`python3 -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`
```

If you don't have db yet, please follow this instruction:

```bash
`sudo -i -u postgres psql`
`CREATE DATABASE regov_quiz_v1;`
`CREATE USER fudo4 WITH PASSWORD 'admin123';`
`GRANT ALL PRIVILEGES ON DATABASE regov_quiz_v1 TO fudo4;`
```

Then you need to config db info by:
In tutorial/settings.py file, find `DATABASES` variable and setting postgresdb based on it

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'regov_quiz_v1',
        'USER': 'fudo4',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

After that, run this command to migrate database

`python3 manage.py migrate`

Now, you need to create a new admin:

`python3 manage.py createdefaultadmin`

Run server:

`python3 manage.py runserver`

After finished, you can go to home page `127.0.0.1:8000` to try login

Now, you are good to go

# Additional Info that you might want to know

For framework, i'm using django rest framework

For database, i'm using postgres

For authenticate, i'm using jwt of "djoser"

You can try to create a new student by running API `127.0.0.1:8000/auth/users/` or `Register User` in postman collection

Admin account and Student account will have difference permission on each API.

I've post my postman collection in this repo, you can check in `Regov Quiz.postman_collection.json`

I'm resolve about handle concurrent requests from multiple users by using transaction.
