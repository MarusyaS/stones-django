from django.db import models

class Site(models.Model):
    ID = models.CharField(max_length=5, primary_key=True, unique = True)
    NameToponim = models.CharField(max_length=30)
    NamePerson = models.TextField(blank=True, null=True)
    NameVariations = models.TextField(blank=True, null=True)
    Type = models.TextField(blank=True, null=True)
    FirstNotion = models.TextField(blank=True, null=True)
    YearExcavate = models.IntegerField( blank=True, null=True)
    Country = models.TextField(blank=True, null=True)
    Region = models.TextField(blank=True, null=True)
    Area = models.TextField(blank=True, null=True)
    LAT = models.FloatField( blank=True, null=True)
    LON = models.FloatField(blank=True, null=True)

    def __str__(self):
        # return self.NameToponim 
        return '%s, %s' % (self.Country, self.Region)


class Inscription(models.Model):
    ID = models.CharField(max_length=6, primary_key=True, unique = True)
    Name = models.TextField()
    NameVariations = models.TextField(blank=True, null=True)
    ContextType = models.TextField(blank=True, null=True)
    DigitalDocumentation = models.TextField(blank=True, null=True) #must be boolean
    CitDTS = models.CharField(max_length=10, blank=True, null=True)
    CitVasilev = models.CharField(max_length=10, blank=True, null=True)
    CitBazylhan = models.CharField(max_length=10, blank=True, null=True)
    CitKormushin = models.CharField(max_length=10, blank=True, null=True)
    LAT = models.FloatField(blank=True, null=True)
    LON = models.FloatField( blank=True, null=True)
    Site = models.ForeignKey(Site, related_name='inscriptions', db_column = 'Site_id', on_delete = models.SET_NULL, blank=True, null=True)
    BitigKz = models.URLField(
        max_length=128, 
        db_index=True, 
        blank=True
    )

    def __str__(self):
        return self.Name


class Museum(models.Model):
    MusID = models.CharField(max_length=6,  primary_key=True, unique = True)
    Name = models.CharField(max_length=30)
    OfficialName = models.TextField()
    InstitutionClass = models.TextField()
    LAT = models.FloatField(blank=True, null=True)
    LON = models.FloatField( blank=True, null=True)
    Docmethod = models.TextField()
    Description = models.TextField()
    Country = models.TextField()
    Adress = models.TextField(blank=True)
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
    Object = models.TextField(blank=True,)
    Process = models.TextField()
    Camera = models.TextField()
    Lens = models.TextField()
    FrameCount = models.IntegerField(blank=True, null=True)
    Scheme = models.TextField()
    Date = models.DateField()
    Photographer =  models.TextField(blank=True,)
    ModelProcesser =  models.TextField(blank=True,)
    PolygonCountMaster = models.FloatField( blank=True, null=True)
    PolygonCountGeneral = models.FloatField( blank=True, null=True)
    AreaCM = models.IntegerField( blank=True, null=True)
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
