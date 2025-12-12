from rest_framework import serializers
from .models import DailyReport

class DailyReportCSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = "__all__"
