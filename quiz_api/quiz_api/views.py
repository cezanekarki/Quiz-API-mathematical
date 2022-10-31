from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from accounts.models import Score
from .serializer import ScoreSerializer, UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#sponsor crud in api
class ScoreListCreate(generics.ListCreateAPIView):
	serializer_class = ScoreSerializer
	queryset = Score.objects.all()

class ScoreRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ScoreSerializer
	queryset = Score.objects.all()
	lookup_field = 'id'

class ScoreDetailRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ScoreSerializer
	queryset = Score.objects.all()
	lookup_field = 'player'