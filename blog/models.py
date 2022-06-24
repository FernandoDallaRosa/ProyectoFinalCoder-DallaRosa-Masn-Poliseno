from django.db import models
from django.contrib.auth.models import User
from operator import truediv
from pyexpat import model
from statistics import mode


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo