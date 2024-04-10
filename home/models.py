from django.db import models

# Create your models here.

class Genre(models.Model):
    """
    Model representing a diary genre (e.g. daily, remainder).
    """
    name = models.CharField(max_length=200, help_text="请输入猫猫头今天的表现")

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.utils import timezone
class Diary(models.Model):
    """
    Model representing a diary
    """
    title = models.CharField(max_length=200, help_text="标题")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, help_text="观察员")
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="请输入今天要记录的内容：")
    genre = models.ManyToManyField(Genre, help_text="分类")
    date = models.DateField(default=timezone.now, help_text="日期")
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.author) +  " Blog Title: " + self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('diary-detail', args=[str(self.id)])
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'



class Author(models.Model):
    name = models.CharField(max_length=100, help_text="观察员")
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True,help_text="观察员介绍！")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name



# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.utils.timezone import now
 
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, help_text="观察员!")
#     image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
#     bio = models.TextField(blank=True, null=True,help_text="观察员介绍！")
    
#     def __str__(self):
#         return str(self.user)
 
# class BlogPost(models.Model):
#     title=models.CharField(max_length=255)
#     author= models.ForeignKey(User, on_delete=models.CASCADE)
#     slug=models.CharField(max_length=130)
#     content=models.TextField()
#     image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
#     dateTime=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return str(self.author) +  " Blog Title: " + self.title
    
#     def get_absolute_url(self):
#         return reverse('blogs')
    
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
#     parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
#     dateTime=models.DateTimeField(default=now)
 
#     def __str__(self):
#         return self.user.username +  " Comment: " + self.content