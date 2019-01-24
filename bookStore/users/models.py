from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Profle model with data regarding the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Features to include on the profile

    #Image feature upload
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

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