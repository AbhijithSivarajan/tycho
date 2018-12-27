import asyncio
from event_tracking.app import create_app
from event_tracking.models.config import Config

config = Config({
    "mongo": {
        "db_name": "tycho",
        "hosts": "mongo:27017",
        "max_pool_size": 1,
        "write_concern": 1
    },
})


loop = asyncio.get_event_loop()
app = loop.run_until_complete(create_app(loop, config))