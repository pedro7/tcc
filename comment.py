from pydantic import BaseModel


class Comment(BaseModel):
    all_awardings: list | None = None
    approved_at_utc: None = None
    approved_by: dict | None = None
    archived: bool | None = None
    associated_award: dict | None = None
    author: str
    author_cakeday: bool | None = None
    author_created_utc: int | None = None
    author_flair_background_color: str | None = None
    author_flair_css_class: str | None
    author_flair_richtext: list | None = None
    author_flair_template_id: str | None = None
    author_flair_text: str | None
    author_flair_text_color: str | None = None
    author_flair_type: str | None = None
    author_fullname: str | None = None
    author_is_blocked: bool | None = None
    author_patreon_flair: bool | None = None
    author_premium: bool | None = None
    awarders: list | None = None
    banned_at_utc: None = None
    banned_by: dict | None = None
    body: str
    body_html: str | None = None
    can_gild: bool | None = None
    can_mod_post: bool | None = None
    collapsed: bool | None = None
    collapsed_because_crowd_control: None = None
    collapsed_reason: str | None = None
    collapsed_reason_code: str | None = None
    comment_type: None = None
    controversiality: int
    created: int | None = None
    created_utc: int
    distinguished: str | None
    downs: int | None = None
    editable: bool | None = None
    edited: int
    gilded: int
    gildings: dict | None = None
    id: str
    is_submitter: bool | None = None
    likes: dict | None = None
    link_id: str
    locked: bool | None = None
    mod_note: None = None
    mod_reason_by: None = None
    mod_reason_title: None = None
    mod_reports: list | None = None
    name: str | None = None
    no_follow: bool | None = None
    num_reports: int | None = None
    parent_id: str
    permalink: str | None = None
    quarantined: bool | None = None
    removal_reason: str | None = None
    replies: str | None = None
    report_reasons: dict | None = None
    retrieved_on: int | dict | None = None
    retrieved_utc: int | None = None
    rte_mode: str | None = None
    saved: bool | None = None
    score: int
    score_hidden: int | None = None
    send_replies: bool | None = None
    steward_reports: list | None = None
    stickied: bool | None = None
    subreddit: str
    subreddit_id: str
    subreddit_name_prefixed: str | None = None
    subreddit_type: str | None = None
    top_awarded_type: None = None
    total_awards_received: int | None = None
    treatment_tags: list | None = None
    unrepliable_reason: None = None
    ups: int | None = None
    user_reports: list | None = None

    class Config:
        extra = 'forbid'
