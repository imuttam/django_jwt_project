from django.urls import path
from .views import DailyReportCSVUploadAPIView, DailyReportListAPIView

urlpatterns = [
    path("upload-csv/", DailyReportCSVUploadAPIView.as_view()),
    path("reports/", DailyReportListAPIView.as_view()),
]
