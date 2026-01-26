from typing import Optional

class Professor:
    def __init__(self, name: str, rating: str, difficulty: str, percent_take_again: str):
        self.name: str = name
        
        try:
            self.rating: Optional[float] = float(rating)
        except ValueError:
            self.rating = None

        try:
            self.difficulty: Optional[float] = float(difficulty)
        except ValueError:
            self.difficulty = None

        try:
            self.percent_take_again: Optional[int] = int(percent_take_again.replace('%', ''))
        except ValueError:
            self.percent_take_again = None

    def __repr__(self):
        return f'<Professor {self.name}>'
    
    def __str__(self):
        return f'{self.name} | Rating: {self.rating} | Difficulty: {self.difficulty} | Take again: {self.percent_take_again}%'
    
    def to_dict(self) -> dict:
        return {
            'name': self.name, 
            'rating': self.rating, 
            'difficulty': self.difficulty, 
            'percent_take_again': self.percent_take_again
            }
    
    @classmethod
    def from_dict(cls, json: dict) -> Professor:
        return cls(
            name=json['name'],
            rating=json['rating'],
            difficulty=json['difficulty'],
            percent_take_again=json['percent_take_again']
        )