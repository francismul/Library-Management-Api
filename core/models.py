from datetime import timedelta

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Book(models.Model):
    type = models.CharField(max_length=50)
    pub_date = models.DateField()
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True)
    language = models.CharField(max_length=10)
    authors = models.TextField()
    subjects = models.TextField()
    locc = models.CharField(max_length=100, blank=True, null=True)
    bookshelves = models.TextField()
    total_copies = models.PositiveIntegerField(
        default=1, null=True, blank=True)
    available_copies = models.PositiveIntegerField(
        default=1, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's empty
            base_slug = slugify(self.title)[:50]  # Limit to 50 chars
            slug = base_slug
            counter = 2

            # Check if slug already exists
            while Book.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"  # Append a number
                counter += 1

            self.slug = slug  # Set unique slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.authors}"


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.return_date:
            self.return_date = self.borrow_date + \
                timedelta(days=14)  # Auto-set return date

        if self.book.available_copies > 0:
            self.book.available_copies -= 1  # Reduce available copies
            self.book.save()
        else:
            # Prevent borrowing if no copies left
            raise ValueError("No copies available for borrowing.")

        super().save(*args, **kwargs)


class Return(models.Model):
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
    return_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.borrow.returned:
            self.borrow.returned = True
            self.borrow.book.available_copies += 1
            self.borrow.book.save()
            self.borrow.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.borrow.user.username} returned {self.borrow.book.title}"
