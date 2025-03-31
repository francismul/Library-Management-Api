from django.db import models
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    authors = models.TextField()
    published_date = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:60]
            slug = base_slug
            counter = 1
            
            while Book.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{str(self.title)[:50]} by {self.authors}"
        

