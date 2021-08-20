from rest_framework import serializers 
from src.models import Reservation,  Tutorial, Tennis_court
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published'
                  )

class ReservationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Reservation
        fields = ('id',
                  'title',
                  'client',
                  'description',
                  'data_init',
                  'data_end',
                  'published'
                    )
                  
class CourtSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tennis_court
        fields = ('id',
                  'client',
                  'type',
                  'umpire',
                  'teacher'
                  )