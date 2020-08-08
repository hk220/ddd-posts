from typing import List
from dataclasses import dataclass

from injector import inject

from ddd_posts.domain.model.post import PostFactoryInterface, PostRepositoryInterface
from ddd_posts.domain.model.post import PostID, Post


@inject
@dataclass
class PostApplicationService:
    factory: PostFactoryInterface
    repository: PostRepositoryInterface

    def post(self, content: str) -> PostID:
        post: Post = self.factory.create(content)
        self.repository.save(post)
        return post.post_id

    def detail(self, post_id: PostID) -> Post:
        return self.repository.find(post_id)

    def list_(self) -> List[Post]:
        return self.repository.find_all()
