# MindBowser_Assignment
requirements: Pycharm/spider IDE
              POSTGRES Database
              PG Admin (POSTGRES DAtabase Interface)
              
go to assignment folder and run command in pycharm terminal:
    python manage.py runserver
    
for existing manager login from frontend:
username: mindbowser
password:12345


for manager login backend (Admin Panel)

goto http://127.0.0.1:8000/admin
this will open django admin panel.log in using following credentials

userrname:Mindbowser
password:12345
              
new admin can be created usin python manage.py createsuperuser in pycharm terminal

employee can be added by both: 1 frontend: employee can register himself
                               2 backend: manager can add employee using admin panel
                               
employee list is fetched from the database and and displayed on the employee page.                               
