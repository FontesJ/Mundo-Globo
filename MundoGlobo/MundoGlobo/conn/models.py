from django.db import models
#from django.contrib.auth.models import User


class Client(models.Model):
    GENERO = (
        ('1', 'Masculino'),
        ('2', 'Feminino'),
        ('3', 'Outro'),
    )

    descricao = models.CharField(max_length=200)
    email = models.CharField(max_length=60)
    sexo = models.CharField(max_length=10, choices=GENERO)
    senha = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="MundoGlobo/photos/", null=True, blank=True)
    data_pub = models.DateTimeField(auto_now_add=True)
    #writer = models.ForeignKey(User)

    def __str__(self):
        return self.name