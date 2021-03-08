from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from mattermost_auth.models import MatthermostAuth
from mattermost_auth.serializer import MattermostAuthSerializer


class MattermostViewSet(ViewSet):


    def list(self, request):
        queryset = MatthermostAuth.objects.order_by('pk')
        serializer = MattermostAuthSerializer(queryset, many=True)
        return Response(serializer.data)

    @permission_classes((IsAuthenticated,))
    def create(self, request):
        serializer = MattermostAuthSerializer(data=request.data)
        if serializer.is_valid():
            print(request.user)

            request_data = request.data
            mattermost_user = MatthermostAuth(login_id=request_data['login_id'],
                                              password=make_password(request_data['password']),user=request.user)

            mattermost_user.save()
            # serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, pk=None):
        queryset = MatthermostAuth.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = MattermostAuthSerializer(item)
        return Response(serializer.data)

    @permission_classes((IsAuthenticated,))
    def update(self, request, pk=None):
        try:
            item = MatthermostAuth.objects.get(pk=pk)
        except MatthermostAuth.DoesNotExist:
            return Response(status=404)
        serializer = MattermostAuthSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @permission_classes((IsAuthenticated,))
    def destroy(self, request, pk=None):
        try:
            item = MatthermostAuth.objects.get(pk=pk)
        except MatthermostAuth.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)