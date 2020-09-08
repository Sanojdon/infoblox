from rest_framework import serializers
from jsonread.models import DataRead

class DataReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRead
        fields = (
            'dr_id', 'dr_fname', 'dr_lname', 'dr_city', 'dr_data'
        )
