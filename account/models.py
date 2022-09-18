from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from urllib.request import urlopen
from django.core.files import File 
from django.core.files.temp import NamedTemporaryFile
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='account/image',null=True)
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=True)
    birthday = models.DateField(null=True,blank=True)
    country = CountryField(default='EG',blank=True)
    facebook = models.URLField(max_length=500,null=True, blank=True)
    # //////////////////////////////////////////


    def get_image_from_url(self, url):
        img_temp = NamedTemporaryFile()
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        self.image.save("image_%s" % self.pk +'.jpg', File(img_temp))
        self.is_active = True
        self.save()

    def save_url(self,url):
        self.facebook = url    