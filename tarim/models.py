from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField("Категория", max_length=150)
    description=models.TextField("Описание")
    url=models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категория"


class Contributor(models.Model):
    contributor_team = (("Tarim Talks Team","Tarim Talks Team"),("Tarim Stars Team","Tarim Stars Team"),("Uyghur Exchange Team","Uyghur Exchange Team"))

    contributor_title = (("Research","Research"),("Editor","Editor"),("Logistics","Logistics"),("Moderator","Moderator"),("Graphics","Graphics"),("Video","Video"))

    name=models.CharField("Name", max_length=150)
    age=models.PositiveIntegerField("Age", default=0)
    title=models.CharField("Title", choices=contributor_title,max_length=150)
    team=models.CharField("Team", choices=contributor_team,max_length=150)
    description= models.TextField("Description")
    image = models.ImageField("Image", upload_to="contributors/", height_field=None, width_field=None, max_length=None)
    sm_instagram = models.CharField("Instagram",max_length=150)
    sm_twitter = models.CharField("Twitter",max_length=150)
    sm_linkedin = models.CharField("Linkedin",max_length=150)

    


    class Meta:
        verbose_name = "Contributors"
        verbose_name_plural = "Contributors"

    def __str__(self):
        return self.name


    