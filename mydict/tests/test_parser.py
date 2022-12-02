import pytest
from mydict.parser import Parser, ParserException
from mydict.terminals import TokenType, Token

class TestParser:
    def test_factor(self):
        parser = Parser()
        string = ">= 12"
        
        parser.init_parser(string)
        parser.factor()
        assert parser.tokens == [Token(TokenType.CONDITION, ">="), Token(TokenType.NUMBER, "12")]