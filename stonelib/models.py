from django.db import models
import datetime

class Site(models.Model):
    ID = models.CharField(max_length=5, primary_key=True, unique = True)
    NameToponim = models.CharField(max_length=30)
    NamePerson = models.TextField()
    NameVariations = models.TextField()
    Type = models.TextField()
    FirstNotion = models.TextField()
    YearExcavate = models.IntegerField( null=True)
    Country = models.TextField()
    Region = models.TextField()
    Area = models.TextField()
    LAT = models.FloatField( null=True)
    LON = models.FloatField( null=True)
    # LAT = models.DecimalField( max_digits=13, decimal_places=10)
    # LON = models.DecimalField( max_digits=13, decimal_places=10)

    def __str__(self):
        # return self.NameToponim 
        return '%s, %s' % (self.Country, self.Region)


class Inscription(models.Model):
    ID = models.CharField(max_length=6, primary_key=True, unique = True)
    Name = models.TextField()
    NameVariations = models.TextField()
    ContextType = models.TextField()
    DigitalDocumentation = models.TextField() #must be boolean
    CitDTS = models.CharField(max_length=10)
    CitVasilev = models.CharField(max_length=10)
    CitBazylhan = models.CharField(max_length=10)
    CitKormushin = models.CharField(max_length=10)
    LAT = models.FloatField( null=True)
    LON = models.FloatField( null=True)
    # LAT = models.DecimalField( max_digits=13, decimal_places=10)
    # LON = models.DecimalField( max_digits=13, decimal_places=10)
    Site = models.ForeignKey(Site, related_name='inscriptions', db_column = 'Site_id', on_delete = models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.Name

    #def get_absolute_url(self):
    # """Returns the URL to access a particular instance of the model.\
    # Of course to make this work you still have to write the URL mapping, view, and template!"""
      #  return reverse('model-detail-view', args=[str(self.id)])

class Museum(models.Model):
    MusID = models.CharField(max_length=6,  primary_key=True, unique = True)
    Name = models.CharField(max_length=30)
    OfficialName = models.TextField()
    InstitutionClass = models.TextField()
    LAT = models.FloatField( null=True)
    LON = models.FloatField( null=True)
    Dates = models.DateField()
    Docnumber = models.IntegerField( null=True)
    Docmethod = models.TextField()
    Description = models.TextField()
    Country = models.TextField()
    Adress = models.TextField()
    Link = models.URLField(
        # ("ModelID"), 
        max_length=128, 
        # db_index=True, 
        # unique=True, 
        blank=True
    )
    Showing = models.TextField() #should be boolean 
   
   
    def __str__(self):
        return self.Name


class Model3D(models.Model):
    ID = models.CharField(max_length=6,  primary_key=True, unique = True)
    Object = models.TextField()
    Process = models.TextField()
    Camera = models.TextField()
    Lens = models.TextField()
    FrameCount = models.IntegerField( null=True)
    Scheme = models.TextField()
    Date = models.DateField()
    PolygonCount = models.IntegerField( null=True)
    PolygonCM = models.FloatField( null=True)
    Link = models.URLField(
        ("ModelID"), 
        max_length=128, 
        db_index=True, 
        # unique=True, 
        blank=True
    )
    Site = models.ForeignKey(Museum, db_column = 'Site_id', on_delete = models.SET_NULL, db_constraint = False,
    blank=True,
    null=True)
    Inscription = models.ForeignKey(Inscription, related_name='models', db_column = 'Inscription_id', on_delete = models.SET_NULL, 
    # db_constraint = False,
    blank=True,
    null=True)  # if you have a nullable ForignKey and you want it to be set null when the referenced object is deleted

    def __str__(self):
        return self.ID

class Image(models.Model):
    ID = models.CharField(max_length=10, primary_key=True, unique = True)
    Inscription = models.ForeignKey(Inscription, related_name='images',db_column = 'Inscription_id',on_delete = models.SET_NULL,
    blank=True,
    null=True)  # if you have a nullable ForignKey and you want it to be set null when the referenced object is deleted

    Type = models.TextField()
    AdditionalDescription = models.TextField(blank=True)
    Link = models.URLField(
        # ("ModelID"), 
        max_length=128, 
        db_index=True, 
        # unique=True, 
        blank=True
    )
