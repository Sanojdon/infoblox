from rest_framework.serializers import ModelSerializer

from jsonread.models import DataRead

class DataReadSerializer(ModelSerializer):
    class Meta:
        model = DataRead
        fields = (
            'dr_id', 'dr_fname', 'dr_lname', 'dr_city', 'dr_data'
        )
