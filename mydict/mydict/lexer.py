from .terminals import TerminalsType, TokenType, Token

class LexerException(Exception):
    ...

class Lexer:
    def __init__(self):
        self.pos = 0
        self.string = ""
        self.current_char = ""
    
    def init_lexer(self, string : str):
        self.pos = 0
        self.string = string
        self.current_char = string[self.pos]
    
    
    def forward(self):
        self.pos += 1
        if self.pos == len(self.string):
            self.current_char = ""
        else:
            self.current_char = self.string[self.pos]
    
    def next(self):
        while self.current_char != "":
            if self.current_char.isspace():
                self.skip()
                continue
            if self.current_char in TerminalsType.NUMBER.value:
                return Token(TokenType.NUMBER, self.number())
            if self.current_char in TerminalsType.CONDITION.value:
                return Token(TokenType.CONDITION, self.condition())
            if self.current_char in TerminalsType.CONDITION_SEPARATOR.value:
                return Token(TokenType.SEPARATOR, self.current_char)

            raise LexerException("Unexpected terminal")
        
    def prev(self):
        return self.string[self.pos - 1]
    
    def skip(self):
        while self.current_char != "" and self.current_char.isspace():
            self.forward()
    
    def number(self) -> str:
        result = []
        
        if self.prev in TerminalsType.NUMBER_SEPARATOR.value:
            while self.current_char != "" and \
                self.current_char in TerminalsType.NUMBER.value: 
                    result.append(self.current_char)
            self.forward()
            return "".join(result)
        
        while self.current_char != "" and \
                (self.current_char in TerminalsType.NUMBER.value or 
                self.current_char in TerminalsType.NUMBER_SEPARATOR.value):
            result.append(self.current_char)
            self.forward()
        return "".join(result)
    
    def condition(self) -> str: 
        result = []
        
        while self.current_char != "" and \
            self.current_char in TerminalsType.CONDITION.value:
            result.append(self.current_char)
            self.forward()
            
        return "".join(result)