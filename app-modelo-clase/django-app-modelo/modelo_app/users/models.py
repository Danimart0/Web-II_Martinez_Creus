from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default="default@example.com")
    age = models.IntegerField()
    rfc = models.CharField(max_length=13, default="RFC_DEFAULT")
    photo = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.street}, {self.city}, {self.country}"