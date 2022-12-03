from mydict.mydict.parser import Parser, ParserException
from mydict.mydict.terminals import TokenType, Token


parser = Parser()
string = ">= 12, == 13"

parser.init_parser(string)
parser.factor()

tokens = []
print(f"Исходая строка: {string}")
for token in parser.get_tokens():
    print(token)
    tokens.append(token)

print(tokens)

#print(len(parser.tokens))
# assert parser.tokens == [Token(TokenType.CONDITION, ">="), Token(TokenType.NUMBER, "12")]