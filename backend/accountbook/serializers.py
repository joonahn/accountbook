from rest_framework import serializers
from .models import AccountBookData, Account, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    accountbookdata = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AccountBookData.objects.all())
    account = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'accountbookdata', 'account')

class AccountBookDataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = AccountBookData
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Account
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = "__all__"
