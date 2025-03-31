import csv

from pathlib import Path
from datetime import datetime

from django.core.management.base import BaseCommand

from core.models import Book

base_dir = Path(__file__).resolve().parent


class Command(BaseCommand):
	help = "Importing books in bulk from a csv file"
	
	def handle(self, *args, **options):
		file_path = base_dir / "books.csv"
		
		books_to_create = []
		existing_slugs = set(Book.objects.values_list("slug", flat=True))
		
		with open(file_path, newline="", encoding="utf-8") as theFile:
			reader = csv.DictReader(theFile)
			
			for row in reader:
				try:
					published_date = datetime.strptime(row["Published Date"], "%Y-%m-%d").date()
					title = row["Title"].strip()
					base_slug = title[:60]
					slug = base_slug
					counter = 1
					
					while slug in existing_slugs:
						slug = f"{base_slug}-{counter}"
						counter += 1
					
					existing_slugs.add(slug)
					
					books_to_create.append(Book(
						slug=slug,
						title=title,
						published_date=published_date,
						authors=row["Authors"],
					))
				except Exception as e:
					self.stdout.write(self.style.ERROR(f"Error: {e}"))
			
		if books_to_create:
			Book.objects.bulk_create(books_to_create, ignore_conflicts=True)
			self.stdout.write(self.style.SUCCESS(f"Successfully imported: {len(books_to_create)} books!"))
					
	
