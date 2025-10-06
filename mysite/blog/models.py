from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class post(models.Model):
    image = models.ImageField(upload_to='blog/' , default='blog/defualt.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL ,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True ,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # def snippets(self):
    #     return self.content[:254]+"..."

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.content