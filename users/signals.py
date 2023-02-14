"""
    Arquivo com o responsável por criar profiles para cada usurário
"""


# sinal que é disparado quando um objeto é salvo
from django.db.models.signals import post_save
# o sinal, pois irá enviar o sinal
from django.contrib.auth.models import User
# o receptor
from django.dispatch import receiver
# importando os profiles, pois iremos criar profiles na nossa função
from .models import Profile 


#função disparada sempre que um novo usuário é criado
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

# salva
@receiver(post_save, sender=User)
def save_profile(sender, instance,  **kwargs):
    instance.profile.save()