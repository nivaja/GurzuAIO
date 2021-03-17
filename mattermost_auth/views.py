from django.contrib.auth.models import User
from django.shortcuts import render
import requests

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from mattermost_auth.models import MatthermostAuth


def token(request):
    permission_classes = (IsAuthenticated,)
    mattermost_user=MatthermostAuth.objects.get(pk=request.user.id)
    print(request)
    print(request.user)
    response=requests.post('https://gurzu.cloud.mattermost.com/api/v4/users/login', data={
        'login_id':mattermost_user.login_id,
        'password':mattermost_user.password
    })
    return Response(response.json(), status=200)

    # login_id
    # password
