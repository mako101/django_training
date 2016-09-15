from django.db import models as m


# Create your models here.
class Genre(m.Model):
    name = m.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(m.Model):
    name = m.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(m.Model):
    title = m.CharField(max_length=100)
    artist = m.CharField(max_length=100)
    album = m.CharField(max_length=100)
    desc = m.CharField(max_length=200)
    genre = m.ForeignKey(Genre)  # one-to-one relationship, where we dont delete anything
    categories = m.ManyToManyField(Category)  # this is a many-to-many relationship
    upload_date = m.DateTimeField('Date Uploaded')





