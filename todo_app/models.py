from django.contrib.auth.models import User, Group
from djongo import models

class todolist(models.Model):
    name = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=25)
    done = models.BooleanField(default=False)
    usr = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usr')
#    id = models.ForeignKey(User.get_username(User),on_delete=models.CASCADE);

    def __str__(self):
        return self.name + " - " + self.mobile + " - " + str(self.done)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description + " - " + self.document
