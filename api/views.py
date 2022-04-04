from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import profileSerializer
from users.models import profiles

@api_view(['GET'])
def main(request):
    return Response([
        {'GET':'api/profiles/'},
        {'GET':'api/profile/<id>/'},
    ])

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfiles(request):
    users = profiles.objects.all()[:5]
    serialized = profileSerializer(users,many=True)
    return Response(serialized.data)


@api_view(['GET'])
def getProfile(request,pk):
    users = profiles.objects.get(id=pk)
    serialized = profileSerializer(users,many=False)
    return Response(serialized.data)