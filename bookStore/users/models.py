from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from localflavor.us.models import USStateField


# All user data is/should be linked to this profile, so when user gets deleted, all data deletes as well
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField('Nick name', max_length=30, blank=True, default='')
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Address = models.ForeignKey('Address', on_delete=models.CASCADE)

    # If we don't have this, it's going to say profile object only
    def __str__(self):
        return self.user.username
        #return f'{self.user.username}'  # it's going to print username Profile

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)


class Address(models.Model):
    # users = models.ManyToManyField(Profile, blank=True)
    name = models.CharField(max_length=100, blank=False)
    address1 = models.CharField("Address lines 1", max_length=128)
    address2 = models.CharField("Address lines 2", max_length=128, blank=True)
    city = models.CharField("City", max_length=64)
    # state = USStateField("State", default='FL')
    state = models.CharField("State", max_length=128, default='FL')
    zipcode = models.CharField("Zipcode", max_length=5)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return self.name
