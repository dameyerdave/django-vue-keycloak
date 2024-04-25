from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
