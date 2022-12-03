import pytest
from mydict.parser import Parser, ParserException
from mydict.terminals import TokenType, Token

class TestParser:
    def test_factor(self):
        parser = Parser()
        string = ">=12"
        
        parser.init_parser(string)
        parser.factor()
        
        assert parser.get_tokens() == [Token(TokenType.CONDITION, ">="), Token(TokenType.NUMBER, "12")]
        
        parser.init_parser("    >=   12                  ,                 == 13     ")
        parser.factor()
        
        assert parser.get_tokens() == [Token(TokenType.CONDITION, ">="), 
                                       Token(TokenType.NUMBER, "12"), 
                                       Token(TokenType.SEPARATOR, ","),
                                       Token(TokenType.CONDITION, "=="), 
                                       Token(TokenType.NUMBER, "13")
                                       ]
        
        with pytest.raises(ParserException):
            parser.init_parser(">= 12,")
            parser.factor()