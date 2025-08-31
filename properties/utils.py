from django.core.cache import cache
from .models import Property


def get_all_properties():
    """
    Retrieve all properties from cache if available,
    otherwise fetch from the database and cache them.
    Cached for 1 hour (3600 seconds).
    """
    all_properties = cache.get("all_properties")

    if not all_properties:
        all_properties = list(
            Property.objects.all().values(
                "id", "title", "description", "price", "location", "created_at"
            )
        )
        cache.set("all_properties", all_properties, timeout=3600)

    return all_properties
