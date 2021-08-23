from rest_framework import serializers 
from src.models import Tennis_court_1, Tennis_court_2, Tennis_court_3 #,  Tutorial, Tennis_court
 

class CourtSerializer1(serializers.ModelSerializer):
 
    class Meta:
        model = Tennis_court_1
        fields = ('id',
                  'title',
                  'client',
                  'description',
                  'date_init',
                  'date_end',
                  'referee',
                  'instructor'
                    )

class CourtSerializer2(serializers.ModelSerializer):
 
    class Meta:
        model = Tennis_court_2
        fields = ('id',
                  'title',
                  'client',
                  'description',
                  'date_init',
                  'date_end',
                  'referee',
                  'instructor'
                    )

class CourtSerializer3(serializers.ModelSerializer):
 
    class Meta:
        model = Tennis_court_3
        fields = ('id',
                  'title',
                  'client',
                  'description',
                  'date_init',
                  'date_end',
                  'referee',
                  'instructor'
                    )

