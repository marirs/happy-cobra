# Happy Cobra

Happy Cobra is a basic skeleton for Login & Registration system using the Flask-Security. The features in this skeleton include:

1) Home page 
    - Register a user
    - Login a user
    - Forgot Password
    - Reconfirm User

2) Register: New Users registration
    - Email
    - First Name
    - Last Name
    - Password  
 After Registration process is done, a confirmation email is sent to the users email id to confirm.  
    - Confirmation Link will be valid for only 1 day (configurable)

3) Login: Login a user
    - Email (as userid)
    - Pass
    - Track User details after login (browser, ip, geolocation, etc)

4) Password Recovery:  
    Password reset and recovery, when a user forgets his or her password.  
    - Reset Password link expires within 1 day (configurable)

5) Logout:
    - Logout when user clicks Logout

Since this is a skeleton, it can be included in any bigger projects.

---

### Requirements
1. Python 2.7
2. PIP Requirements
3. PostgreSQL/MySQL/SQLite (depending on your environment)
4. A working SMTP Mail Server (Sendgrid, or anything like.)

---
## *Deployment*

Deployment steps

#### Setting up the virtual environment
If you are using python 3.x
```bash
mkvirtualenv --python=`which python3` venv_name
cd /path/to/happycobra/
setvirtualenvproject
```
If you are using python 2.7
```bash
mkvirtualenv --python=`which python` venv_name
cd /path/to/happycobra/
setvirtualenvproject
```

#### Installing the pip requirements
```bash
pip install -r requirements
```

#### Environment
* Unix/OSx
```bash
export FLASK_APP=app/__init__.py
export WORKING_ENVIRONMENT='production'
export FLASK_DEBUG=0
```
* Windows
```bash
set FLASK_APP=app/__init__.py
set WORKING_ENVIRONMENT='production'
set FLASK_DEBUG=0
```

if it's development then use `WORKING_ENVIRONMENT='development'`

#### Setting up PostgresSQL
```bash
psql

CREATE DATABASE adbname ENCODING 'UTF-8';
CREATE USER appuser WITH PASSWORD 'AC0mp13XPa55w0rd';
GRANT ALL PRIVILEGES ON DATABASE adbname to appuser;
```
---

###### *Available Flask commands*
```bash
flask --help

Commands:
  create_roles  Create default roles
  create_super  Create superuser
  db            Perform database migrations.
  roles         Role commands.
  routes        Show the routes for the app.
  run           Runs a development server.
  shell         Runs a shell in the app context.
  users         User commands.
```
---
#### DB Init & Migrations
```bash
flask db init
flask db migrate
flask db upgrade
```

#### Creating the super user
```bash
flask create_super FirstName LastName Email@Adddress
```

#### Creating a new user
```bash
flask users create UserEmail --password PWD --active
```

#### Creating default Roles
```bash
flask create_roles
```

#### Creating New Roles
```bash
flask roles create RoleName -d "Role Description"
```

#### Adding Role to a User
```bash
flask roles add USER ROLE
```
---
## *Running the app*
```bash
flask run
```

## *Accessing the app*
```bash
http://localhost:5000
```

---
Licensing:  
- MIT License

Credits:
- bootstrap
- ShardsAdmin by Design Revision
