from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Grant(models.Model):

    THEMATIC_CHOIECES=(
        ('SRHR','SRHR'),
        ('HIV/TB','HIV/TB'),
        ('WLPR','WLPR'),
        ('SILU','SILU'),
        ('H&G','H&G')    
    )

            
    
    FREQUENCY=(
        ('Annual','Annual'),
        ('Bi-annual','Bi-annual'),    
    )
    CURRENCY=(
        ('USD','USD'),
        ('Ksh','Ksh'),   
    )

    # thematic_area=MultiSelectField(choices=THEMATIC_CHOIECES)
    thematic_area=models.CharField('Choose Thematic',choices=THEMATIC_CHOIECES,max_length=100)
    donor=models.CharField('Donor',max_length=200,blank=True,null=True)
    project_name=models.CharField('Project Name',max_length=200)
    log=models.ImageField(null=False,blank=False)
    info=RichTextField(blank=True,null=True)
    # person_responsible=MultiSelectField(PERSON_RESPONSIBLE,max_choices=3,max_length=10)
    person_responsible=models.CharField('Choose Persons',max_length=100 ,default='Jesica')

    # frequency=MultiSelectField(choices=FREQUENCY,max_choices=2,max_length=10)
    frequency=models.CharField('Choose Persons',choices=FREQUENCY,max_length=100)
    project_start=models.DateField()
    project_end=models.DateField()
    value=models.IntegerField(blank=True,null=True)
    currency=models.CharField('Choose Currency',max_length=100,choices=CURRENCY,blank=True,null=True)

    def __str__(self):
        return self.project_name

    
