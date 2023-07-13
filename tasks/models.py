from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#Cuando creamos la tabla por primera vez
#ejecutamos python manage.py makemigrations  para generar la tabla
#Luego ejecutamos python manage.py migrate
class Task(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' - by ' + self.user.username
    
#luego ir a admin para agregarlo en el visual del adminsitrador