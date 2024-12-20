from dataclasses import dataclass

@dataclass
class Haiku:
  haiku_id: int
  created_at: str
  author: str
  text: str
