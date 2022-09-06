#!/bin/bash
echo "cron running"
cd /home/c1ph3rr/Desktop/temporary-storage/
source env/bin/activate
cd temporary-file-storage-django/
python manage.py delete_expired