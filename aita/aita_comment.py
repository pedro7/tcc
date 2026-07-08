from typing import Literal

from pydantic import BaseModel, field_validator


class AitaComment(BaseModel):
    author: str
    body: str
    parent_id: str
    permalink: str | None = None
    score: int
    subreddit: Literal['AmItheAsshole']
    subreddit_id: Literal['t5_2xhvq']

    class Config:
        extra = 'ignore'

    @field_validator('author')
    def validate_author(cls, v: str) -> str:
        if v == 'AutoModerator':
            raise ValueError()
        return v

    @field_validator('body')
    def validate_deleted(cls, v: str) -> str:
        v = v.strip()

        if v in ('[deleted]', '[removed]'):
            raise ValueError()
        return v

    @field_validator('parent_id')
    def validate_is_submission(cls, v: str) -> str:
        v = v.strip()

        if not v.startswith('t3_'):
            raise ValueError()
        return v.removeprefix('t3_')

    @field_validator('score')
    def validate_score(cls, v: int) -> int:
        if v < 0:
            raise ValueError()
        return v