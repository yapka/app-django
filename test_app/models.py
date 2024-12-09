from django.db import models

class Personne(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=50)
    birth = models.DateField()  # Utilisation d'un champ DateField pour la date de naissance
    email = models.EmailField()
    tel = models.CharField(max_length=10)  # Peut aussi être remplacé par un PhoneNumberField si besoin
    ROLE = (('admin', 'admin'), ('user', 'user'))
    role = models.CharField(max_length=10, choices=ROLE)

    def __str__(self):
        return self.name + ' ' + self.subname


