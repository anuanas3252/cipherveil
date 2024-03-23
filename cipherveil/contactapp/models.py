from django.db import models
import uuid

# Create your models here.
class ContactBook(models.Model):
    tag = models.CharField(max_length=255,unique=True,blank=False,null=False)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
    

def generate_alphanumeric_id():
    unique_id = str(uuid.uuid4().hex)
    return unique_id

class OpenID(models.Model):
    tag = models.CharField(max_length=255,unique=True)

    def save(self, *args, **kwargs):
        if not self.contactID:
            self.contactID = generate_alphanumeric_id()
        super(OpenID, self).save(*args, **kwargs)

    def __str__(self):
        return self.contactID