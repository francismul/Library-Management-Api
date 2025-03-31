import csv

from pathlib import Path

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


base_dir = Path(__file__).resolve().parent


class Command(BaseCommand):
	help = "Populate the database with users from a csv file"

	def handle(self, *args, **kwargs):
		csv_file = base_dir / "users.csv"
		try:
			with open(csv_file, newline="", encoding="utf-8") as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					user, created = User.objects.get_or_create(
						username=row["username"],
						defaults={
							"first_name":row["firstname"],
							"last_name":row["lastname"],
						}
					)	
					if created:
						user.set_password(row["password"])
						user.save()
						self.stdout.write(self.style.SUCCESS(f"User: {user.username} created successfully!"))
					else:
						self.stdout.write(self.style.WARNING(f"User: {user.username} already exists!"))
                        
		except Exception as e:
			self.stdout.write(self.style.ERROR(f"Error: {e}"))               
                        
                        
                        
                        
                        
        
