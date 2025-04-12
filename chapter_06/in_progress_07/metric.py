from dataclasses import dataclass

@dataclass
class Metric:
  title: str
  func: callable
  type: str
