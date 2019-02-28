from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Address(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60, default="Miami")
    state = models.CharField(max_length=30, default="Florida")
    zipcode = models.CharField(max_length=5, default="33165")
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'

    def __str__(self):
        return self.name

# All user data is/should be linked to this profile, so when user gets deleted, all data deletes as well
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField('Nick name', max_length=30, blank=True, default='')
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    addresses = models.ManyToManyField(
        Address,
        through='AddressType',
        through_fields=('address', 'profile')
        )

    # If we don't have this, it's going to say profile object only
    def __str__(self):
        return f'{self.user.username} Profile'  # it's going to print username Profile

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)


class AddressType(models.Model):

    HOME_ADDRESS = 1
    SHIPPING_ADDRESS = 2

    TYPE_ADDRESS_CHOICES = (
        (HOME_ADDRESS, "Home address"),
        (SHIPPING_ADDRESS, "Shipping address"),
    )

    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # This is the field you would use for know the type of address.
    address_type = models.PositiveIntegerField(choices=TYPE_ADDRESS_CHOICES)

    class Meta:
        verbose_name = 'Type of Address'
        verbose_name_plural = 'Type of Address'

    def __str__(self):
        return f'{self.address_type}'
