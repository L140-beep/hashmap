from mydict.mydict.parser import Parser, ParserException
from mydict.mydict.terminals import TokenType, Token
from mydict.mydict.myDict import myDict

parser = Parser()
string = ">= 12, == 13"

parser.init_parser(string)
parser.factor()


# tokens = []
# print(f"Исходая строка: {string}")
# for token in parser.get_tokens():
#     print(token)
#     tokens.append(token)

mydict = myDict({2 : 1,"2": 2, "2, 3" : 0, "3, 5": 0, "1, 3, 5": 0, "value" : 0})

result = mydict.ploc(">= 2")

dick = dict({2 : 1,"2": 2, "2, 3" : 0, "3, 5": 0, "1, 3, 5": 0, "value" : 0})

print(result)

#print(len(parser.tokens))
# assert parser.tokens == [Token(TokenType.CONDITION, ">="), Token(TokenType.NUMBER, "12")]