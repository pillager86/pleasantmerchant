import csv

from django.core.management import BaseCommand
from inventory.models import Item

class Command(BaseCommand):
    help = 'Load item data from csv into database'
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                Item.objects.create(
                    upc=row[0],
                    name=row[1],
                    case_qty=row[2],
                    case_cost=row[3],
                    full_price=row[4],
                    member_price=row[5],
                    qoh=row[6]
                )