from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    autor = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")

    legenda = models.TextField(max_length=400,blank=True)

    imagem = models.ImageField(upload_to="posts/", blank=True,null=True)

    criado_em = models.DateTimeField(auto_now=True)

    atualizado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Post de {self.autor.username} '

    class Meta:
        ordering = ["-criado_em"]

