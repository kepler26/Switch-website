from django.db import models


class LogEntry(models.Model):
    date = models.DateField()
    time = models.TimeField()
    username = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255, blank=True, default="No change")
    ip_address = models.CharField(max_length=255, blank=True, default="No change")
    vlan_changes = models.CharField(max_length=255, blank=True, default="No change")
    view_log = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date", "-time"]

    def __str__(self):
        return f"{self.date} {self.time} - {self.username}"
