from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length =30)
    image = CloudinaryField('image')
    posted_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length =200)
    
    class Meta:
        '''
        class method to display images by date posted
        '''
        ordering = ['posted_date']
        
    def __str__(self):
        return self.description
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()



    