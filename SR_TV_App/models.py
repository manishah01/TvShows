from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "SHOW TITLE MUST BE ATLEAST 2 CHARACTERS"
        if len(postData['network']) < 3:
            errors['network'] = "NETWORK MUST BE AT LEAST 3 CHARACTERS"
        if len(postData['release_date']) <8:
            errors['release_date'] = "DATE MUST BE AT LEAST 8 CHARACTERS"
        if len(postData['description']) < 10:
            errors['description'] = "DESCRIPTION MUST BE AT LEAST 10 CHARACTERS"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
