from .models import TravelBuddy
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class TravelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TravelBuddy
        fields = ['id','name','location','description','img','upvote','downvote']