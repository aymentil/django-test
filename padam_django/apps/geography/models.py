from django.db import models


class Place(models.Model):
    name = models.CharField("Name of the place", max_length=50)

    longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6)
    latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6)

    class Meta:
        # Two places cannot be located at the same coordinates.
        unique_together = (("longitude", "latitude"), )

    def __str__(self):
        return f"Place: {self.name} (id: {self.pk})"

class BusStop(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='bus_stops')

    def __str__(self):
        return f"BusStop: {self.place.name}"
