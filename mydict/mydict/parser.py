from .lexer import Lexer
from .terminals import Token, TokenType, TokenExpect

class ParserException(Exception):
    ...

class Parser:  
    def __init__(self):
        self.tokens = []
        self.conditions_count = 1
        self.current_token: Token = None
        self.lexer = Lexer()
    
    def factor(self):
        token = self.current_token
        #print(self.current_token)
        match token.type:
            case TokenType.CONDITION:
                self.tokens.append(token)
                self.check_type(TokenExpect.CONDITION)
                return
            case TokenType.NUMBER:
                self.tokens.append(token)
                self.check_type(TokenExpect.NUMBER)
                return
            case TokenType.SEPARATOR:
                self.conditions_count += 1
                self.tokens.append(token)
                self.lexer.forward()
                self.check_type(TokenExpect.SEPARATOR)
                return
            case _:
                raise ParserException("Invalid token")

    def check_type(self, expected : TokenExpect):
        self.current_token = self.lexer.next()
        if self.current_token is None:
            if expected == TokenExpect.NUMBER:
                return
            else:
                raise ParserException("Invalid argument")
        if self.current_token.type in expected.value:
            self.factor()
        else:
            raise ParserException(f"Unexpected token {self.current_token.type}, expected {expected.value}") 

        
    def init_parser(self, s: str):
        self.lexer.init_lexer(s)
        self.current_token = self.lexer.next()
        self.tokens = []
    
    def get_tokens(self):
        return self.tokens