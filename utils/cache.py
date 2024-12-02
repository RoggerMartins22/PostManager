import redis
import os
import json
import logging

logger = logging.getLogger(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"), 
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True, 
)

class SystemCache:
    def set_cache(key: str, value: str, ex=300):
        try:
            value_json = json.dumps(value)
            redis_client.setex(key, ex, value_json)
        except Exception as e:
            logger.error(f"Erro ao definir o cache: {str(e)}") 
    
    def get_cache(key: str):
        try:
            value = redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Erro ao acessar o cache: {str(e)}")
            return None

    def invalidate_cache(key: str):
        redis_client.delete(key)
