from rest_framework import serializers
from .models import Metrics

class DataSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)
    channel = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    impressions = serializers.IntegerField(required=False)
    os = serializers.CharField(required=False)
    clicks = serializers.IntegerField(required=False)
    installs = serializers.IntegerField(required=False)
    spend = serializers.DecimalField(max_digits=25, decimal_places=2, required=False)
    revenue = serializers.DecimalField(max_digits=25, decimal_places=2, required=False)
    #cpi = serializers.FloatField(required=False)

    class Meta:
        model = Metrics
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi')