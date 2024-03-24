from django.db import models
from django.contrib.auth.models import User
# Create your models here.

EDUCATION_TYPE = [
    ("SSC","SSC"),
    ("HSC","HSC"),
    ("HONOURS","HONOURS"),
    ("MASTERS","MASTERS"),
]

class TeacherModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user/images",null=True)
    birth_date = models.DateField(null=True)
    mobile_no = models.CharField(max_length=12,null=True)
    education = models.CharField(choices =EDUCATION_TYPE,null=True , max_length=12)
    def __str__(self) :
        return self.user.username