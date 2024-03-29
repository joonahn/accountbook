from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework import views
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.decorators import action, api_view
from .models import AccountBookData, Account, Category
from .serializers import AccountBookDataSerializer, AccountSerializer, UserSerializer, CategorySerializer
from .permissions import IsOwner


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'accountbook': reverse('accountbook-list', request=request, format=format),
    })


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(views.APIView):
    authentication_classes = (authentication.SessionAuthentication,)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response("OK")
        else:
            raise PermissionDenied()

    def get(self, request):
        return render(request, 'accountbook/login.html')


class LogoutView(views.APIView):
    def get(self, request):
        logout(request)
        return Response("OK")


class CheckLoginView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response("OK")


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AccountBookDataViewSet(viewsets.ModelViewSet):
    serializer_class = AccountBookDataSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        try:
            return AccountBookData.objects.all().filter(owner=self.request.user)
        except TypeError:
            raise PermissionDenied()

    @action(methods=['GET'], detail=False)
    def search(self, request):
        filter_dict = {'owner': self.request.user}
        
        if request.query_params.get('account'):
            filter_dict['account'] = int(request.query_params.get('account'))

        if request.query_params.get('date_str'):
            target_date = datetime.strptime(
                request.query_params.get('date_str'), "%Y-%m-%d").date()
            filter_dict['account_date'] = target_date

        if request.query_params.get('date_from') and request.query_params.get('date_to'):
            date_from = datetime.strptime(
                request.query_params.get('date_from'), "%Y-%m-%d").date()
            date_to = datetime.strptime(
                request.query_params.get('date_to'), "%Y-%m-%d").date()
            filter_dict['account_date__range'] = [date_from, date_to]

        if not filter_dict:
            abd = AccountBookData.objects.none()
        else:
            abd = AccountBookData.objects.filter(**filter_dict)
        serializer = self.get_serializer(abd, many=True)
        return Response(serializer.data)


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        try:
            return Account.objects.all().filter(owner=self.request.user)
        except TypeError:
            raise PermissionDenied()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
