from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class agblog(models.Model):
    title=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False,default="Default Value")
    date=models.DateTimeField(auto_now_add=True)
    categories=models.CharField(max_length=300,blank=False)
    tags=models.CharField(max_length=300,blank=False)
    text=models.CharField(max_length=300,blank=False)
    image=models.ImageField(upload_to='agblog/',blank=False)
    image1=models.ImageField(upload_to='agblog/',blank=False)
    image2=models.ImageField(upload_to='agblog/',blank=False)

    def __str__(self):
        return self.title
    
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class ag1(models.Model):
    title = models.CharField(max_length=200, unique=True)
    name=models.CharField(max_length=100,blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='ag_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories=models.CharField(max_length=300,blank=False)
    tags=models.CharField(max_length=300,blank=False)
    text=models.CharField(max_length=300,blank=False)
    image=models.ImageField(upload_to='ag1/',blank=False)
    image1=models.ImageField(upload_to='ag1/',blank=False)
    image2=models.ImageField(upload_to='ag1/',blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title