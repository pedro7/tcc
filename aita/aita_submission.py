from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import field_validator

from submission import Submission


class AitaSubmission(Submission):
    created_utc: int
    domain: Literal['self.AmItheAsshole']
    edited: int
    id: str
    is_self: Literal[True]
    link_flair_text: Verdict
    num_comments: int
    score: int
    selftext: str
    subreddit: Literal['AmItheAsshole']
    subreddit_id: Literal['t5_2xhvq']
    title: str

    class Config:
        extra = 'allow'

    @field_validator('title', 'selftext')
    def validate_deleted(cls, v: str) -> str:
        v = v.strip()

        if v in ('[ Removed by moderator ]', '[deleted]', '[removed]'):
            raise ValueError()
        return v

    @property
    def label(self):
        return {
            'Not the A-hole': 0,
            'Asshole': 1,
            'No A-holes here': 0,
            'Everyone Sucks': 1
        } [self.link_flair_text]


class Verdict(str, Enum):
    YTA = 'Asshole'
    NTA = 'Not the A-hole'
    ESH = 'Everyone Sucks'
    NAH = 'No A-holes here'
