from mydict.mydict.parser import Parser, ParserException
from mydict.mydict.terminals import TokenType, Token


parser = Parser()
string = ">= 12.1,  11"

parser.init_parser(string)
parser.factor()

print(f"Исходая строка: {string}")
for token in parser.get_tokens():
    print(token)
#print(len(parser.tokens))
# assert parser.tokens == [Token(TokenType.CONDITION, ">="), Token(TokenType.NUMBER, "12")]