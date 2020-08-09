from copy import copy
from typing import List, Dict
from uuid import UUID, uuid4

import inject

from ddd_posts.domain.model.post import PostFactoryInterface, PostRepositoryInterface
from ddd_posts.domain.model.post import Post, PostID, PostContent


class InMemoryPostFactory(PostFactoryInterface):
    
    def __init__(self):
        super().__init__()

    def create(self, content: str) -> Post:
        post_id = PostID(uuid4())
        post_content = PostContent(content)
        return Post(post_id, post_content)


class InMemoryPostRepository(PostRepositoryInterface):

    __kv: Dict[PostID, Post] = {}

    def __init__(self):
        super().__init__()

    def find(self, post_id: PostID) -> Post:
        return copy(self.__kv[post_id])

    def find_all(self) -> List[Post]:
        return list(map(copy,self.__kv.items()))

    def save(self, post: Post):
        self.__kv[post.post_id] = copy(post)


def configure(binder):
    binder.bind_to_constructor(PostFactoryInterface, InMemoryPostFactory)
    binder.bind_to_constructor(PostRepositoryInterface, InMemoryPostRepository)


inject.configure(configure)
