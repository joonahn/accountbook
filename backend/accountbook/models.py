from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.

INOUT_TYPE = (('income', '수입'), ('expenditure', '지출'),)


class Account(models.Model):
    account_name = models.CharField(max_length=20)
    owner = models.ForeignKey(
        'auth.User', related_name='account', on_delete=models.CASCADE)
    def __str__(self):
        return self.account_name

class Category(MPTTModel):
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class AccountBookData(models.Model):
    account_date = models.DateField()
    create_timestamp = models.DateTimeField(auto_now_add=True)
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='category')
    additional_category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='additional_category')
    inout = models.CharField(choices=INOUT_TYPE, default='expenditure', max_length=12)
    content = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    money = models.IntegerField(default=False)
    owner = models.ForeignKey(
        'auth.User', related_name='accountbookdata', on_delete=models.CASCADE)


class PreferenceData(models.Model):
    key = models.CharField(max_length=20)
    value = models.TextField()
