import pytest
from mydict.lexer import Lexer, LexerException
from mydict.terminals import TokenType, Token

class TestLexer:
    def test_next(self):
        lexer = Lexer()
        lexer.init_lexer("23")
        
        assert lexer.next() == Token(TokenType.NUMBER, "23") 
        
        with pytest.raises(LexerException):
            lexer.init_lexer("blabla")
            lexer.next()
        
        with pytest.raises(LexerException):
            lexer.init_lexer("")
            lexer.next()
    
    def test_prev(self):
        lexer = Lexer()
        lexer.init_lexer(">= 3")
        lexer.next()
        
        assert lexer.prev() == "="