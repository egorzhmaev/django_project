from django.db import connection
import os

def db_new():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitemyfirst.settings')
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE auth_permission, django_content_type CASCADE")

db_new()