from django.db import models

# Create your models here.
class DiabetesPrediction(models.Model):
    pregnancies = models.IntegerField()
    glucose_Level = models.IntegerField()
    blood_Pressure = models.IntegerField()
    skin_Tickness = models.IntegerField()
    insulin = models.IntegerField()
    body_Mass_Index = models.FloatField()
    diabetes_Pedidree_Function = models.FloatField()
    age = models.IntegerField()
    outcome = models.IntegerField(default=None)

    def __str__(self):
        diabetes_status = None
        if self.outcome == 1:
            diabetes_status = "Yes"
        elif diabetes_status == None:
            diabetes_status = "Unknown"
        else:
            diabetes_status = "No"
        return f"User {self.id} | Have Heart Disease?  {diabetes_status}"