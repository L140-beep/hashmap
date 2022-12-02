from .lexer import Lexer
from .terminals import Token, TokenType

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
        print(self.current_token)
        match token.type:
            case TokenType.CONDITION:
                self.tokens.append(token)
                self.check_type(TokenType.NUMBER)
                return
            case TokenType.NUMBER:
                self.tokens.append(token)
                self.check_type(TokenType.SEPARATOR)
                return
            case TokenType.SEPARATOR:
                self.conditions_count += 1
                self.tokens.append(token)
                self.lexer.forward()
                self.check_type(TokenType.CONDITION)
                return
            case _:
                raise ParserException("Invalid token")

    def check_type(self, expected : Token):
        self.current_token = self.lexer.next()
        print(self.current_token)
        if self.current_token is None:
            return
        if self.current_token.type == expected:
            #self.current_token = self.lexer.next()
            self.factor()
            
        else:
            raise ParserException(f"Unexpected token {self.current_token.type}, expected {expected}") 

        
    def init_parser(self, s: str):
        self.lexer.init_lexer(s)
        self.current_token = self.lexer.next()
    
    def get_tokens(self):
        return list(self.tokens)