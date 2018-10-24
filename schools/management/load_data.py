from csv import DictReader
from django.core.management import BaseCommand

from schools.models import School

ALREADY_LOADED_ERROR_MESSAGE = """If you need to reload the schools data from the CSV file,first delete the db.sqlite3 file to destroy the database.Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from data.csv into our School model"

    def handle(self, *args, **options):
        if School.objects.exists():
            print('Schools data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        for row in DictReader(open('./data.csv')):
            school = School()
            school.name = row['SchoolName']
            school.description = row['SchoolDescription']
            school.save() #this should save
