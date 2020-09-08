from django.core.management.base import BaseCommand, CommandError
from jsonread.models import DataRead as DR

class Command(BaseCommand):
    help = 'Gets the Data of the ID given'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs='*', type=int)

    def handle(self, *args, **options):
        self.stdout.write("Running the commands from command line")
        for i in options['id']:
            h = DR.objects.get(dr_id=str(i))
            self.stdout.write(self.style.SUCCESS('First name : %s' % h.dr_fname))
            self.stdout.write(self.style.SUCCESS('Last name : %s' % h.dr_lname))
