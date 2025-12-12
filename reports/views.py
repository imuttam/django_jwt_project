from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from .models import DailyReport
from .serializers import DailyReportCSVUploadSerializer
import csv
from datetime import datetime


class DailyReportCSVUploadAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]  # only admins

    def post(self, request):
        serializer = DailyReportCSVUploadSerializer(data=request.data)

        if serializer.is_valid():
            csv_file = serializer.validated_data["file"]
            decoded = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded)

            count = 0
            for row in reader:
                date = datetime.strptime(row["DATE"], "%d-%m-%Y").date()

                DailyReport.objects.update_or_create(
                    date=date,
                    defaults={
                         "er_voice_traffic": row["ER VOICE TRAFFIC   2G /3G"],
                        "er_busy_traffic": row["ER BUSY TRAFFIC 2G/3G"],
                        "zte_voice_traffic": row["ZTE VOICE TRAFFIC 2G/3G"],
                        "zte_busy_traffic": row["ZTE BUSY TRAFFIC 2G/3G"],
                        "vlr_count": row["VLR COUNT"],
                        "site_count": row["SITE COUNT 2G/3G/4G"],
                        "tcs_site_count": row["TCS SITE COUNT"] or 0,
                        "data_vol_2g": row["DATA VOL 2G(GB)"] or 0,
                        "data_vol_3g": row["DATA VOL 3G(GB)"] or 0,
                        "data_vol_zte_4g": row["DATA VOL ZTE 4G(GB)"] or 0,
                        "data_vol_tcs_4g": row["DATA VOL TCS 4G(GB)"] or 0,
                        "data_vlr_2g": row["DATA VLR 2G"] or 0,
                        "data_vlr_3g": row["DATA VLR 3G"] or 0,
                        "data_vlr_zte_4g": row["DATA VLR ZTE 4G"] or 0,
                        "data_vlr_tcs_4g": row["DATA VLR TCS 4G"] or 0,
                        "volte_traffic_zte": row["VOLTE TRAFFIC ZTE"] or 0,
                        "volte_traffic_tcs": row["VOLTE TRAFFIC TCS"] or 0,
                          
                           }
                )
                count += 1

            return Response({"message": f"{count} rows uploaded successfully"})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DailyReportSerializer
from .filters import DailyReportFilter

class DailyReportListAPIView(generics.ListAPIView):
    queryset = DailyReport.objects.all().order_by("-date")
    serializer_class = DailyReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_class = DailyReportFilter

    search_fields = [
        "er_voice_traffic",
        "er_busy_traffic",
        "site_count"
    ]

    ordering_fields = [
        "date",
        "vlr_count",
        "data_vol_zte_4g",
        "data_vol_tcs_4g"
    ]
