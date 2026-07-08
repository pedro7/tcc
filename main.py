import json

import psycopg
from pydantic import ValidationError

from aita.aita_comment import AitaComment
from aita.aita_submission import AitaSubmission
from zst import read_lines


def decompress_submissions_to_postgres(file_path = r'aita\zst\submissions.zst'):
    conn_str = 'host=localhost dbname=aita user=postgres password=root'

    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            with cur.copy("COPY submissions (id, title, body, verdict, label, edited, score, num_comments, created_utc) FROM STDIN") as copy:
                for line in read_lines(file_path):
                    try:
                        obj = json.loads(line)
                        submission = AitaSubmission(**obj)

                        copy.write_row((
                            submission.id,
                            submission.title,
                            submission.selftext,
                            submission.link_flair_text.name,
                            submission.label,
                            bool(submission.edited),
                            submission.score,
                            submission.num_comments,
                            submission.created_utc
                        ))
                    except ValidationError:
                        continue


def decompress_comments_to_postgres(file_path = r'aita\zst\comments.zst'):
    conn_str = "host=localhost dbname=aita user=postgres password=root"

    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            with cur.copy("COPY comments (submission_id, body, score, permalink) FROM STDIN") as copy:
                for line in read_lines(file_path):
                    try:
                        obj = json.loads(line)
                        comment = AitaComment(**obj)

                        copy.write_row((
                            comment.parent_id,
                            comment.body,
                            comment.score,
                            comment.permalink
                        ))
                    except ValidationError:
                        continue


if __name__ == "__main__":
    decompress_submissions_to_postgres()
