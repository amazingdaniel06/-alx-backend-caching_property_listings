import logging
from django.core.cache import cache
from .models import Property

logger = logging.getLogger(__name__)

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



def get_redis_cache_metrics():
    """
    Retrieve Redis cache performance metrics.
    Returns keyspace_hits, keyspace_misses, and hit_ratio.
    """
    try:
        client = cache.client.get_client()
        stats = client.info("stats")

        keyspace_hits = stats.get("keyspace_hits", 0)
        keyspace_misses = stats.get("keyspace_misses", 0)
        total_requests = keyspace_hits + keyspace_misses

        hit_ratio = (
            keyspace_hits / total_requests if total_requests > 0 else 0
        )

        return {
            "keyspace_hits": keyspace_hits,
            "keyspace_misses": keyspace_misses,
            "hit_ratio": hit_ratio,
        }

    except Exception as e:
        logger.error(f"Error retrieving Redis metrics: {e}")
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0,
        }
