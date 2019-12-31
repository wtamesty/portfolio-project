from django.db import models
from django.utils.timezone import now

# Create a blog model
# title, pub_date, body_text, image_blog

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=now, editable=False)
    body_text = models.CharField(max_length=2000)
    image_blog = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body_text[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
