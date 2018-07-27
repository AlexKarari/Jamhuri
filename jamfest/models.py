from django.db import models


# Create your models here.
class Type_of_Event(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Talent(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='profilepic/')
    bio = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    genre = models.ManyToManyField(Genre, blank=True)
    event = models.ManyToManyField(Type_of_Event, blank=True)
    talent = models.ManyToManyField(Talent, blank=True)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_name(cls, search_term):
        artist = cls.objects.filter(name__icontains=search_term)
        return artist

class Events(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    poster = models.ImageField(upload_to='poster/')
    eventtime = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    image = models.ImageField(upload_to='newsimages/', blank=True)
    postDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Releases(models.Model):
    album_title = models.CharField(max_length=100)
    album_image = models.ImageField(upload_to='album/')
    producer = models.CharField(max_length=100)
    releaseDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.album_title

class Merchandise(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to='merch/')
    item_price = models.CharField(max_length=100)
    
    def __str__(self):
        return self.item_name


class Testimonials(models.Model):
    testimonial = models.CharField(max_length=5000)
    author = models.CharField(max_length=100)


    def __str__(self):
        return self.testimonial

class Services(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name

