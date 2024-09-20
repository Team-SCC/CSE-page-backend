from dataclasses import dataclass
from datetime import datetime


@dataclass
class CommentDocument:
    sid: str
    content: str
    create: datetime
