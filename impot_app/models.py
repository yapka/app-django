from django.db import models
from test_app.models import Personne
# Create your models here.
class Impot(models.Model):
    intule=models.CharField(max_length=50)
    prix=models.IntegerField()
    limite=models.DateField()

    person=models.ForeignKey(Personne, on_delete=models.CASCADE)
    def __str__(self):
        return self.intule + ' ' + str(self.prix)