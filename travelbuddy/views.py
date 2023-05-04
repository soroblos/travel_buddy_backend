from .models import TravelBuddy
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TravelSerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = TravelBuddy.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [permissions.AllowAny]