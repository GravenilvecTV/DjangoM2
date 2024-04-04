from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    image = models.TextField(default="https://resize-elle.ladmedia.fr/rcrop/638,,forcex/img/var/plain_site/storage/images/elle-a-table/les-dossiers-de-la-redaction/dossier-de-la-redac/blog-cuisine/68970235-2-fre-FR/Quels-sont-les-10-blogs-de-cuisine-les-plus-influents.jpg")
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title
    
    def calculate_words(self):
        mots = self.content.split(' ')
        nb_mots = len(mots)
        return nb_mots
