from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpeg", upload_to="default_pics")
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        #calling the parent class save method
        super().save()
        #now we open the image of the instance we are working with
        #the below opens the current instance of the image with the open method of the PIL liobrary and the self.image that refers to teh current instance
        img = Image.open(self.image.path)
        #now we need to resize the image according to what our website accepts, we add an if statement to check the size of the image
        if img.height > 300 or img.width > 300:
            #we choose a size that is an indication of when we would like to risize the picture 
            output_size = (300, 300)
            #then we overwrite the changes in the image
            img.thumbnail(output_size)
            #then we save the image with the same method as before so we oiverwrite the preceding image 
            img.save(self.image.path)



