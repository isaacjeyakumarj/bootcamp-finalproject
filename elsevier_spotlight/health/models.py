from django.db import models

# Create your models here.
class healthblog(models.Model):
    title=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False,default="Default Value")
    date=models.DateTimeField(auto_now_add=True)
    categories=models.CharField(max_length=300,blank=False)
    tags=models.CharField(max_length=300,blank=False)
    text=models.CharField(max_length=300,blank=False)
    image=models.ImageField(upload_to='healthblog/',blank=False)
    image1=models.ImageField(upload_to='healthblog/',blank=False)
    image2=models.ImageField(upload_to='healthblog/',blank=False)

    def __str__(self):
        return self.title