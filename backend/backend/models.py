from django.db import models

class Property(models.Model):
    final_location = models.CharField(max_length=200)          # Property location
    year = models.IntegerField()                                # Year
    city = models.CharField(max_length=100)                    # City
    loc_lat = models.FloatField()                               # Latitude
    loc_lng = models.FloatField()                               # Longitude
    total_carpet_area = models.FloatField()                     # Total carpet area
    flat_total = models.IntegerField()                          # Total flats
    shop_total = models.IntegerField()                          # Total shops
    office_total = models.IntegerField()                        # Total offices
    others_total = models.IntegerField()                        # Others

    def __str__(self):
        return f"{self.final_location} - {self.year}"          # Makes it easy to read in admin or shell
