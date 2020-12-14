from django.db import models

# Create your models here.

class BookNumber(models.Model):
    isbn_10=models.CharField(max_length = 10)
    isbn_13=models.CharField(max_length = 13)

class Book(models.Model):
  
    title = models.CharField(max_length = 36, blank=False, unique=True)
    description = models.TextField(max_length = 256, blank=True, default=None, null=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    createdtime = models.DateTimeField(auto_now=True)
    published = models.DateField(blank = True, null=True)
    is_published=models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank = True)
    number = models.OneToOneField(BookNumber, blank=True, null=True,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length = 30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')
 

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    books = models.ManyToManyField(Book, related_name='authors')
