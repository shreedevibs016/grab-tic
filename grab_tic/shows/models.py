from django.db import models

import uuid

from multiselectfield import MultiSelectField

# Create your models here.


class BaseClass(models.Model):

    uuid = models.UUIDField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class CertificationChoices(models.TextChoices):

    U = 'U','U'

    A = 'A','A'

    U_OR_A = 'U/A','U/A'

    S = 'S','S'

class LanguagesChoices(models.TextChoices):

    MALAYALAM = 'Malayalam','Malayalam'

    ENGLISH = 'English','English'

    TAMIL  = 'Tamil','Tamil'

    TELUGU = 'Telugu','Telugu'

    HINDI = 'Hindi','Hindi'

    KANNADA = 'Kannada','Kannada'

class CastChoices(models.TextChoices):

    MOHANLAL = 'Mohan Lal','Mohan Lal'

    MAMMOOTTY = 'Mammootty','Mammootty'

    NIVIN_PAULY = 'Nivin Pauly','Nivin Pauly'

    SHOBANA = 'Shobana','Shobana'

    SAI_PALLAVI = 'Sai Pallavi','Sai Pallavi'

    ANUPAMA_PARAMESWARAN = 'Anupama Parameswaran','Anupama Parameswaran'

class GenreChoices(models.TextChoices):

    ACTION = 'Action','Action'

    CRIME = 'Crime','Crime'

    THRILLER = 'Thriller','Thriller'

    ROMANCE = 'Romance','Romance'

class Certification(BaseClass):

    name = models.CharField(max_length=50)

    class Meta :

        verbose_name = 'Certifications'

        verbose_name_plural = 'Certifications'

    def __str__(self):

        return f'{self.name}'
    
class Language(BaseClass):

    name = models.CharField(max_length=50)

    class Meta :

        verbose_name = 'Languages'

        verbose_name_plural = 'Languages'

    def __str__(self):

        return f'{self.name}'
    
class Cast(BaseClass):

    name = models.CharField(max_length=50)

    photo = models.ImageField(upload_to='cast-images')

    class Meta :

        verbose_name = 'Cast'

        verbose_name_plural = 'Cast'

    def __str__(self):

        return f'{self.name}'
    
class Genre(BaseClass):

    name = models.CharField(max_length=50)

    class Meta :

        verbose_name = 'Genre'

        verbose_name_plural = 'Genre'

    def __str__(self):

        return f'{self.name}'

class Movie(BaseClass):

    name = models.CharField(max_length=50)

    description = models.TextField()

    runtime = models.TimeField()

    photo = models.ImageField(upload_to='movie-images')

    release_date = models.DateField()

    # certification =models.CharField(max_length=20,choices=CertificationChoices.choices)

    certification =models.ForeignKey('Certification',on_delete=models.CASCADE)

    # languages = MultiSelectField(choices=LanguagesChoices.choices)

    languages = models.ManyToManyField('Language',)

    # cast = MultiSelectField(choices=CastChoices.choices)

    cast = models.ManyToManyField('Cast')

    # genre = MultiSelectField(choices=GenreChoices.choices)

    genre = models.ManyToManyField('Genre')

    class Meta :

        verbose_name = 'Movies'

        verbose_name_plural = 'Movies'

    def __str__(self):

        return f'{self.name}-{self.release_date}'