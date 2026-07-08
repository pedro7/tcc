from typing import Optional

from pydantic import BaseModel


class Submission(BaseModel):
    archived: Optional[bool] = None # True if post is archived and can’t be edited.
    author: Optional[str] = None
    author_flair_css_class: Optional[str] = None
    author_flair_text: Optional[str] = None
    banned_by: Optional[str] = None
    created_utc: Optional[int] = None
    distinguished: Optional[str] = None # Moderator/admin special status. Can be "moderator", "admin", "special", or None.
    domain: Optional[str] = None
    downs: Optional[int] = None
    edited: Optional[int] = None
    gilded: Optional[int] = None # Number of times the post received Reddit Gold (or other awards).
    id: Optional[str] = None
    is_self: Optional[bool] = None # True if the post is a text/self post, False for link posts.
    link_flair_css_class: Optional[str] = None
    link_flair_text: Optional[str] = None
    media: Optional[dict] = None # Dictionaries with information about embedded media (videos, images, or third-party embeds). Can be None if not present.
    media_embed: Optional[dict] = None
    mod_reports: Optional[list] = None
    name: Optional[str] = None
    num_comments: Optional[int] = None
    over_18: Optional[bool] = None
    permalink: Optional[str] = None
    report_reasons: Optional[list] = None
    retrieved_on: Optional[int] = None
    score: Optional[int] = None # Net score (ups - downs). Can be None if missing or hidden.
    secure_media: Optional[dict] = None
    secure_media_embed: Optional[dict] = None
    selftext: Optional[str] = None
    selftext_html: Optional[str] = None
    stickied: Optional[bool] = None # True if post is pinned to the top of the subreddit.
    subreddit: Optional[str] = None
    subreddit_id: Optional[str] = None
    thumbnail: Optional[str] = None # Small preview image URL or placeholder ("self", "default", "nsfw").
    title: Optional[str] = None
    ups: Optional[int] = None
    url: Optional[str] = None
    user_reports: Optional[list] = None

    class Config:
        extra = 'forbid'