from django.db import models

class Company(models.Model):
    companyid = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=15)
    pic = models.FileField(default=0)
    s_gender = models.CharField(max_length=30)

    def __str__(self):
        return f'id{self.id}:{self.s_name}|{self.s_age}|{self.s_grade}|{self.s_gender}'
