from enum import Enum, auto


class TerminalsType(Enum):
    CONDITION = ['<', '>', '=']
    NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    NUMBER_SEPARATOR = ['.']
    CONDITION_SEPARATOR = [',']

class TokenType(Enum):
    CONDITION = auto()
    SEPARATOR = auto()
    # EQUAL = auto()
    # EQUAL_OR_MORE = auto()
    # EQUAL_OR_LESS = auto()
    # NOT_EQUAL = auto()
    # LESS = auto()
    # MORE = auto()
    NUMBER = auto()

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value
    
    def __str__(self) -> str:
        return f"Token ({self.type}, {self.value})"
    