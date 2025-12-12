from django.contrib import admin
from .models import DailyReport
import csv
from datetime import datetime
from django.http import HttpResponse


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("date", "vlr_count", "site_count")

    change_list_template = "reports/dailyreport_changelist.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        if "csv" in request.POST:
    
            csv_file = request.FILES["csv_file"]
            decoded = csv_file.read().decode("utf-8").splitlines()
            
            reader = csv.DictReader(decoded)

            # Normalize headers
            reader.fieldnames = [
                name.strip().replace("\ufeff", "")
                for name in reader.fieldnames
            ]

            for raw_row in reader:
                # Normalize row keys
                row = {
                    key.strip().replace("\ufeff", ""): value.strip()
                    for key, value in raw_row.items()
                }

                # Parse date
                date_str = row["DATE"]
                report_date = datetime.strptime(date_str, "%d-%m-%Y").date()

                # Convert helpers
                def to_int(x):
                    try:
                        return int(float(x)) if x else 0
                    except:
                        return 0

                def to_float(x):
                    try:
                        return float(x) if x else 0.0
                    except:
                        return 0.0

                DailyReport.objects.update_or_create(
                    date=report_date,
                    defaults={
                        "er_voice_traffic": row["ER VOICE TRAFFIC   2G /3G"],
                        "er_busy_traffic": row["ER BUSY TRAFFIC 2G/3G"],
                        "zte_voice_traffic": row["ZTE VOICE TRAFFIC 2G/3G"],
                        "zte_busy_traffic": row["ZTE BUSY TRAFFIC 2G/3G"],

                        "vlr_count": to_int(row["VLR COUNT"]),
                        "site_count": row["SITE COUNT 2G/3G/4G"],
                        "tcs_site_count": to_int(row["TCS SITE COUNT"]),

                        "data_vol_2g": to_float(row["DATA VOL 2G(GB)"]),
                        "data_vol_3g": to_float(row["DATA VOL 3G(GB)"]),
                        "data_vol_zte_4g": to_float(row["DATA VOL ZTE 4G(GB)"]),
                        "data_vol_tcs_4g": to_float(row["DATA VOL TCS 4G(GB)"]),

                        "data_vlr_2g": to_int(row["DATA VLR 2G"]),
                        "data_vlr_3g": to_int(row["DATA VLR 3G"]),
                        "data_vlr_zte_4g": to_int(row["DATA VLR ZTE 4G"]),
                        "data_vlr_tcs_4g": to_int(row["DATA VLR TCS 4G"]),

                        "volte_traffic_zte": to_float(row["VOLTE TRAFFIC ZTE"]),
                        "volte_traffic_tcs": to_float(row["VOLTE TRAFFIC TCS"]),
                    }
                )


            self.message_user(request, "CSV Upload Successful!")

        return super().changelist_view(request, extra_context)
