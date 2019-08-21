from rest_framework import serializers
from .models import AccountBookData
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    accountbookdata = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AccountBookData.objects.all())
    class Meta:
        model=User
        fields = ('id', 'username', 'accountbookdata')

class AccountBookDataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = AccountBookData
        fields = ("account_date", "create_timestamp", "category1", "category2",
                  "category3", "upper_catetory", "inout", "content", "money", "owner", )


