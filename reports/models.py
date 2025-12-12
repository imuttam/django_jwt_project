from django.db import models

class DailyReport(models.Model):
    date = models.DateField()

    er_voice_traffic = models.CharField(max_length=20, blank=True, null=True)
    er_busy_traffic = models.CharField(max_length=20, blank=True, null=True)
    zte_voice_traffic = models.CharField(max_length=20, blank=True, null=True)
    zte_busy_traffic = models.CharField(max_length=20, blank=True, null=True)

    vlr_count = models.PositiveIntegerField(null=True, blank=True)
    site_count = models.CharField(max_length=50, blank=True, null=True)
    tcs_site_count = models.PositiveIntegerField(null=True, blank=True)

    data_vol_2g = models.FloatField(null=True, blank=True)
    data_vol_3g = models.FloatField(null=True, blank=True)
    data_vol_zte_4g = models.FloatField(null=True, blank=True)
    data_vol_tcs_4g = models.FloatField(null=True, blank=True)

    data_vlr_2g = models.PositiveIntegerField(null=True, blank=True)
    data_vlr_3g = models.PositiveIntegerField(null=True, blank=True)
    data_vlr_zte_4g = models.PositiveIntegerField(null=True, blank=True)
    data_vlr_tcs_4g = models.PositiveIntegerField(null=True, blank=True)

    volte_traffic_zte = models.PositiveIntegerField(null=True, blank=True)
    volte_traffic_tcs = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.date)
