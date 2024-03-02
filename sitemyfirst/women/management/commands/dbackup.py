from django.core.management import BaseCommand
from django.core.management import call_command
from datetime import datetime

class Command(BaseCommand):
    """
    Команда для создания резервной копии базы данных
    """
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database dump...')
        call_command(
            'dumpdatautf8',
            '--natural-foreign',
            '--natural-primary',
            '--exclude=contenttypes',
            '--exclude=admin.logentry',
            '--indent=4',
            f'--output=database-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json'
        )
        self.stdout.write(self.style.SUCCESS('Database successfully backed up'))