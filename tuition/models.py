from django.db import models

# Create your models here.
CLASSES = [
    ('EIGHT','EIGHT'),
    ('NINE','NINE'),
    ('SSC','SSC'),
    ('HSC','HSC'),
    ('ADMISION','ADMISION'),
]
TYPE = [
    ('ONLINE','ONLINE'),
    ('OFFLINE','OFFLINE'),
]
DAYS = [
    ('3_Days', 3),
    ('4_Days', 4),
    ('5_Days', 5),
    ('6_Days', 6),
]

CATEGORY = [
    ("Bangla Medium","Bangla Medium"),
    ("English Medium","English Medium"),
    ("English Version","English Version"),
]

class TuitionModel(models.Model):
    grade = models.CharField(choices=CLASSES,max_length=12)
    grade_slug = models.SlugField(max_length=12)
    tuition_type = models.CharField(max_length=12,choices=TYPE)
    salary = models.IntegerField()
    address = models.CharField(max_length=60,null=True)
    location = models.CharField(max_length=30)
    location_slug = models.SlugField(max_length=30)
    day_perweek= models.CharField(choices =DAYS,max_length=10 )
    available = models.BooleanField(default=True)
    category = models.CharField(choices=CATEGORY,max_length=60,null=True)
    subject = models.CharField(max_length=60,null=True)
    tuition_duration = models.CharField(max_length=40,null=True)
    no_of_student = models.IntegerField(null=True)
    def __str__(self) :
        return f"{self.id}"