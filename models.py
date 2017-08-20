from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords 
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
#from django.contrib.auth.models import User

# Create your models here.

# let's deal with this later
#class CatColor(models.Model):
#    DEFAULT_PK=1
#    color_name = models.CharField(max_length=256, default='unspecified')

class CatCaretaker(models.Model):
    caretaker_first_name = models.CharField(max_length=256,null=True,blank=False)
    caretaker_last_name = models.CharField(max_length=256,null=True,blank=False)
    caretaker_birthdate = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    caretaker_email = models.EmailField()
    caretaker_phone = models.CharField(max_length=256,null=True,blank=True)
    caretaker_street_address = models.CharField(max_length=256,null=True,blank=True)
    caretaker_city = models.CharField(max_length=256,null=True,blank=True)
    caretaker_state = models.CharField(max_length=256,null=True,blank=True)
    caretaker_zip = models.IntegerField(null=True,blank=True)
    caretaker_date_joined = models.DateField(default=timezone.now)

    # using simple history
    history = HistoricalRecords()

    def __str__(self):
        return self.caretaker_first_name + " " + self.caretaker_last_name

    
class CatColony(models.Model):
    DEFAULT_PK=1
    colony_name = models.CharField(max_length=256,null=False)
    colony_location_name = models.CharField(max_length=256,null=True)
    colony_street_address = models.CharField(max_length=256,null=True)
    colony_cross_street = models.CharField(max_length=256,null=True)
    colony_city = models.CharField(max_length=256,null=True)
    colony_state = models.CharField(max_length=256,null=True)
    colony_zip = models.IntegerField(null=True)
    colony_year_formed = models.IntegerField(blank=True,null=True)
    SETTING_CHOICES = (
        ('R','Rear of address'),
        ('A','Alley'),
        ('O','Offices'),
        ('F','Apartment'),
        ('E','Residential'),
        ('P','Park'),
        ('I','Industrial'),
        ('O','Other')
        )
    colony_setting = models.CharField(max_length=1,choices=SETTING_CHOICES,default='R',null=True)
    colony_setting_other = models.TextField(blank=True)

    # using simple history
    history = HistoricalRecords()

    def __str__(self):
        return self.colony_name

    
class Cat(models.Model):
    HAIR_CHOICES = (
        ('S', 'DSH'),
        ('M', 'DMH'),
        ('L', 'DLH')
        )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
        )
    YESNO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        )
    YESNOUNKNOWN_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('U', 'Unknown')
        )
    cat_name = models.CharField(max_length=256)
#    cat_color = models.ForeignKey(CatColor, default=CatColor.DEFAULT_PK, on_delete=models.SET_DEFAULT)
    cat_type_color = models.CharField(max_length=1024)
    cat_type_color_markings_notes = models.TextField(null=True,blank=True)
    cat_hair_length = models.CharField(max_length=1,choices=HAIR_CHOICES,default='S')
    cat_birthdate = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    cat_gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='U')
    cat_neutered = models.CharField(max_length=1,choices=YESNOUNKNOWN_CHOICES,default='U')
    cat_eartip = models.CharField(max_length=1,choices=YESNOUNKNOWN_CHOICES,default='U')
    cat_other_notes  = models.TextField(null=True,blank=True)
    cat_colony = models.ForeignKey(CatColony, default=CatColony.DEFAULT_PK, on_delete=models.SET_DEFAULT)
    cat_chipped = models.CharField(max_length=1,choices=YESNOUNKNOWN_CHOICES,default='U')
    cat_chip_brand = models.CharField(max_length=256,null=True,blank=True)
    cat_chip_id = models.CharField(max_length=256,null=True,blank=True)

    # housekeeping
    cat_created = models.DateTimeField(editable=False,default=timezone.now)
    cat_modified = models.DateTimeField(default=timezone.now)
    
    # using simple history
    history = HistoricalRecords()
    
    def __str__(self):
        return self.cat_name

    # a save method to update timestamps
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.cat_created = timezone.now()
        self.cat_modified = timezone.now()
        return super(Cat, self).save(*args, **kwargs)

class CatVaccines(models.Model):
    CAT_VACCINES = (
        ('Rabies','Rabies'),
        ('Distemper','Distemper (Panleukopenia)'),
        ('Rhinotracheitis','Rhinotracheitis'),
        ('Calicivirus','Calicivirus'),
        ('Feline Leukemia','Feline Leukemia'),
        ('Other','Other'),
        ('None','None'))
    vac_name = models.CharField(max_length=30,choices=CAT_VACCINES, unique=True)

    def __str__(self):
        return self.vac_name

class CatParasites(models.Model):
    CAT_PARA = (
        ('Fleat Treatment','Flea Treatment'),
        ('Dewormed','Dewormed') )
    para_name = models.CharField(max_length=30,choices=CAT_PARA, unique=True)

    def __str__(self):
        return self.para_name

    
class CatLogEntry(models.Model):
    STATUS_CHOICES = (
        ('H', 'healthy'),
        ('S', 'sick'),
        ('U', 'unclear'),
        ('D', 'dead')
        )
    OUTCOME_CHOICES = (
        ('R', 'returned'),
        ('A', 'adopted/fostered'),
        ('E', 'euthanized'),
        ('O', 'other')
        )
    YESNO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        )
    log_cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    log_date = models.DateTimeField(default=timezone.now)
    log_notes = models.TextField(null=True,blank=True)
    log_status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='H')
    log_outcome = models.CharField(max_length=1,choices=OUTCOME_CHOICES,default='H')
    log_outcome_other = models.TextField(max_length=25,null=True,blank=True)
    log_feral_level = models.IntegerField(default=1,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    log_caretakers = models.ManyToManyField(CatCaretaker, verbose_name="Caretakers")
    log_any_vacs = models.CharField(max_length=1,choices=YESNO_CHOICES,default='N')
    log_vaccinations = models.ManyToManyField(CatVaccines, verbose_name="Vaccinations",blank=True)
    log_vac_other = models.TextField(max_length=256,null=True,blank=True)
    log_any_para_treatment = models.CharField(max_length=1,choices=YESNO_CHOICES,default='N')
    log_parasites = models.ManyToManyField(CatParasites, verbose_name="Parasite Treatment",blank=True)
    
    # using simple history
    history = HistoricalRecords()

    def __str__(self):
        return self.log_cat.cat_name + " " + (self.log_date).isoformat()

    
