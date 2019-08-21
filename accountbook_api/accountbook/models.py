from django.db import models

# Create your models here.

INOUT_TYPE = (('income', '수입'), ('expenditure', '지출'),)


class AccountBookData(models.Model):
    account_date = models.DateField()
    create_timestamp = models.DateTimeField(auto_now_add=True)
    category1 = models.CharField(max_length=20)
    category2 = models.CharField(max_length=20)
    category3 = models.CharField(max_length=20)
    upper_catetory = models.CharField(max_length=20)
    inout = models.CharField(choices=INOUT_TYPE, default='expenditure', max_length=12)
    content = models.TextField()
    money = models.IntegerField(default=False)
    owner = models.ForeignKey(
        'auth.User', related_name='accountbookdata', on_delete=models.CASCADE)
