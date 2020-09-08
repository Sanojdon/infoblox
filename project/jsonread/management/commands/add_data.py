from django.core.management.base import BaseCommand, CommandError
from jsonread.models import DataRead as DR
import json

class Command(BaseCommand):
    help = 'Gets the Data of the ID given'

    def add_arguments(self, parser):
        parser.add_argument('loc', nargs='*', type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading the JSON file'))
        for r in options['loc']:
            self.stdout.write("File uploaded is %s" % r)
            with open(r) as json_file:
                data = json.load(json_file)
                for i in data:
                    b = DR(dr_id=i["id"], dr_fname=i["first_name"], dr_lname=i["last_name"], dr_city=i["city"], dr_data=i["data"])
                    b.save()



        # /home/oem/Desktop/python_Sample/infob/Infoblox-Python-Django-Test/MOCK_DATA.json
