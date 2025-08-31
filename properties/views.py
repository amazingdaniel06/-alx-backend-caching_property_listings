from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.utils import timezone

from .models import Property


@cache_page(60 * 15)  # cache results for 15 minutes
def property_list(request):
    """Return a cached JSON response of all properties."""
    properties = Property.objects.all().values(
        "id", "title", "description", "price", "location", "created_at"
    )
    data = list(properties)

    return JsonResponse({
        "properties": data,
        "cached_at": timezone.now().isoformat()
    })
