from django.db import models

class Property(models.Model):
    final_location = models.CharField(max_length=200)          # Text column
    year = models.IntegerField()                                # Year
    city = models.CharField(max_length=100)                    # Text column
    loc_lat = models.FloatField()                               # Latitude
    loc_lng = models.FloatField()                               # Longitude
    total_carpet_area = models.FloatField()                     # Total carpet area
    flat_total = models.IntegerField()                          # Total flats
    shop_total = models.IntegerField()                          # Total shops
    office_total = models.IntegerField()                        # Total offices
    others_total = models.IntegerField()                        # Other properties
    extra_data = models.JSONField(blank=True, null=True)  # store extra Excel columns

    def __str__(self):
        return f"{self.final_location} - {self.year}"          # Makes it easy to identify in admin or shell

