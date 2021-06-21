from django.db import models

# Create your models here.
class Todos(models.Model):
    task_name=models.CharField(max_length=150)
    status=models.CharField(max_length=25,default="not completed")
    user=models.CharField(max_length=150)
    date=models.DateField(auto_now=True)


    def __str__(self):
        return self.task_name

#orm ueries
# reference name=class name(field name ="value"....)
# reference name.save()
