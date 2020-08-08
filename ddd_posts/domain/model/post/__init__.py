
from abc import ABCMeta, abstractclassmethod
from dataclasses import dataclass
from typing import Protocol
from uuid import UUID, uuid4


@dataclass(frozen=True)
class PostID:
    value: UUID

    def __post_init__(self):
        if not isinstance(self.value, UUID):
            raise ValueError("{}はUUIDのインスタンスではありません。".format(type(self.value)))


@dataclass(frozen=True)
class PostContent:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError("{}はstrのインスタンスではありません。".format(type(self.value)))
        if len(self.value) > 140:
            raise ValueError("140文字以下である必要があります。")


@dataclass
class Post:
    post_id: PostID
    post_content: PostContent

    def __post_init__(self):
        if not isinstance(self.post_id, PostID):
            raise ValueError("{}はPostのインスタンスではありません。".format(type(self.post_id)))
        if not isinstance(self.post_content, PostContent):
            raise ValueError("{}はPostContentのインスタンスではありません。".format(type(self.post_content)))

    def __eq__(self, other: "Post") -> bool:
        return self.post_id == other.post_id


class PostFactoryInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def create(self, content: str) -> Post:
        ...


class PostRepositoryInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def find(self, post_id: PostID):
        ...

    @abstractclassmethod
    def find_all(self):
        ...

    @abstractclassmethod
    def save(self, post):
        ...
