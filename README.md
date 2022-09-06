# Temporary File Storage

A simple file hosting system built with Django. It can temporarily storage your files upto 60 mins.

## How to run the project
1. Clone this repository.
2. Navigate to the main project directory and install the python dependencies with `pip install -r requirements.txt`
3. Run `python manage.py runserver` to start the development server and browse to `http://127.0.0.1:8000` and upload a file.
4. Use `cron -e` on your terminal to edit the cron file and paste `*/60 * * * * /home/c1ph3rr/Desktop/temporary-storage/temporary-file-storage-django/cron.sh` (Use `cron -l` to check if the cron is running).



### Todo
- [ ] Api
