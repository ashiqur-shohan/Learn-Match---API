from django.db import models
from user.models import TeacherModel
from tuition.models import TuitionModel
# Create your models here.

class ReviewModel(models.Model):
    user = models.OneToOneField(TeacherModel,on_delete=models.CASCADE)
    tuition = models.OneToOneField(TuitionModel,on_delete=models.CASCADE)
    body = models.CharField(max_length = 100)
    date = models.DateField(auto_now = True)

    def __str__(self) -> str:
        return f"{self.user.user.username} | {self.tuition.grade} | {self.body}"