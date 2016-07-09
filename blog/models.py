from django.db import models
from django.utils import timezone


#class es una palabra clave que indica que estamos definiendo un objeto
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #def significa que es una función/método 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#__unicode__ para python 2.7
        return self.title