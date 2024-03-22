from django.db import models
from user.models import TeacherModel
from tuition.models import TuitionModel
# Create your models here.

class ApplicationModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    tuition = models.ForeignKey(TuitionModel, on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)
    
    def __str__(self) :
        return f"{self.user.user.username} | {self.tuition.grade}"
    