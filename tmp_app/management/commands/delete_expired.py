import os
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from tmp_app.models import StorageModel


class Command(BaseCommand):
    help = 'Delete the expired database entry and file'

    def handle(self, *args, **options):
        try:
            expired_objects = StorageModel.objects.filter(expires_on__lte=timezone.now())
            if expired_objects:
                for expired in expired_objects:
                    os.remove(expired.file_path)
                expired_objects.delete()
                self.stdout.write(self.style.SUCCESS('Files successfully deleted'))
            else:
                self.stdout.write(self.style.WARNING('Nothing deleted'))
        except StorageModel.DoesNotExist:
            raise CommandError('Model doesnt exist')
