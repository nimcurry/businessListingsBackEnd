from rest_framework import serializers
from .models import Listings

class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields=('business_id','business_name','business_website','business_category','business_email_id')