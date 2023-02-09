from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Cada classe será sua própria tabela
# "nome_do_dado" = models."tipo do dado"("configurações do dado")

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Se o usuário for apagado o Post será apagado tambem
    
    def __str__(self):
        return self.title