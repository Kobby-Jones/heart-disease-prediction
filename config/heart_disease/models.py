from django.db import models

# Heart Disease Prediction Models

class HeartDiseasePrediction(models.Model):
    SEX_CHOICES = (
        (1, 'Male'),
        (0, 'Female')
    )
    CHEST_PAIN_CHOICES = (
        (0, 'Typical Angina'),
        (1, 'Atypical Angina'),
        (2, 'Non-Anginal Pain'),
        (3, 'Asymptomatic')
    )
    RESTECG_CHOICES = (
        (0, 'Normal'),
        (1, 'ST-T wave abnomality'),
        (2, 'Probable or definite left ventricular hypertrophy')
    )
    EXERCISE_INDUCED_ANGINA_CHOICES = (
        (1, 'Yes'),
        (0, 'No')
    )
    SLOPE_CHOICES = (
        (0, 'Upsloping'),
        (1, 'Flat'),
        (2, 'Downsloping')
    )
    THALIUM_STRESS_CHOICES = (
        (1, 'Normal'),
        (2, 'Fixed Defect'),
        (3, 'Reversible Defect')
    )
    FASTING_BLOOD_SUGAR_CHOICES = (
        (1, 'Blood sugar leve greater than 120mg/dl'),
        (0, 'Blood sugar level less than or equal to 120mg/dl')
    )

    age = models.IntegerField()
    sex = models.IntegerField(choices=SEX_CHOICES)
    chest_pain_type = models.IntegerField(choices=CHEST_PAIN_CHOICES)
    trestbps = models.IntegerField()
    cholestrol_level = models.IntegerField()
    fbs = models.IntegerField(choices=FASTING_BLOOD_SUGAR_CHOICES)
    restecg = models.IntegerField(choices=RESTECG_CHOICES)
    thalac = models.IntegerField()
    exang = models.IntegerField(choices=EXERCISE_INDUCED_ANGINA_CHOICES)
    oldpeak = models.DecimalField(max_digits=2, decimal_places=1)
    slope = models.IntegerField(choices=SLOPE_CHOICES)
    ca = models.IntegerField()
    thal = models.IntegerField(choices=THALIUM_STRESS_CHOICES)
    prediction_results = models.IntegerField(null=True)

    def __str__(self):
        return f"User {self.id}"
    