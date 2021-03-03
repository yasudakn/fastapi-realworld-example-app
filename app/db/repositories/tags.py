from typing import List, Sequence
import os
from aiocache import cached, Cache
from aiocache.serializers import PickleSerializer

from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.db.caches import key_builder


class TagsRepository(BaseRepository):
    @cached(cache=Cache.REDIS,
            serializer=PickleSerializer(),
            endpoint=os.environ.get('REDIS_HOST'),
            key_builder=key_builder)
    async def get_all_tags(self) -> List[str]:
        tags_row = await queries.get_all_tags(self.connection)
        return [tag[0] for tag in tags_row]

    async def create_tags_that_dont_exist(self, *, tags: Sequence[str]) -> None:
        await queries.create_new_tags(self.connection, [{"tag": tag} for tag in tags])
