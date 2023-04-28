from django.db import models

# Create your models here.

class Client(models.Model):
    from_date=models.CharField(max_length=50,null=True,blank=True,verbose_name="qaysi vaqtdan")
    to_date=models.CharField(max_length=50,null=True,blank=True,verbose_name="qachongacha")
    kattalar=models.CharField(max_length=20,null=True,blank=True,verbose_name="kattalar soni")
    bolalar=models.CharField(max_length=20,null=True,blank=True,verbose_name="bolalar soni")
    xonalar=models.CharField(max_length=20,null=True,blank=True,verbose_name='xonalar soni')
    checkbox=models.BooleanField(default=False,verbose_name='status')
    def __str__(self):
        return self.from_date

