from .parser import Parser
from .terminals import TokenType, Token
class myDictException(Exception):
    ...

class myDict(dict):
    def toSortedMap(self) -> "myDict":
        sorted_dict = myDict()
        keys = sorted(self.keys())
        
        for key in keys:
            sorted_dict[key] = self[key]
        
        return sorted_dict
    
    def iloc(self, index):
        keys = list(self.keys())
        if index in range(0, len(keys)):
            return self[keys[index]]
        else:
            raise myDictException(f"Index {index} out of range! Size = {len(keys) - 1}")
    
    def __getitem__(self, key):
        if isinstance(key, str):
            key = key.strip('(').strip(')')
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        if isinstance(key, str):
            key = key.strip('(').strip(')')
        val = dict.__setitem__(self, key, value)

        return(val)
    
    
    def ploc(self, condition : str):
        
        self.parser = Parser()
        self.parser.init_parser(condition)
        self.parser.factor()
        
        tokens = self.parser.get_tokens()
        conditions_count = self.parser.conditions_count
        
        keys = self.keys()
        new_keys = []
        int_keys = []
        str_keys = []
        for key in keys:
            if isinstance(key, int):
                if conditions_count == 1:
                    new_keys.append([key])
                    int_keys.append(key)
                else:
                    continue
            else:    
                value = key.split(',')
                str_keys.append(key)
                try:
                    value = list(map(int, value))
                    if len(value) == conditions_count:
                        new_keys.append(value)
                
                except ValueError:
                    continue
        
        num = 0
        condition = ""
        
        index_condition = 0
        
        for token in tokens:
            match token.type:
                case TokenType.CONDITION:
                    condition = token.value
                case TokenType.NUMBER:
                    if('.' in token.value):
                        num = float(token.value)
                    else: 
                        num = int(token.value)
                    new_keys = self.compare(new_keys, condition, num, index_condition)
                case TokenType.SEPARATOR:
                    index_condition += 1
                    continue
                
                case _:
                    raise myDictException(f"Unknown token {token}")
        
        
        result = myDict()
        for key in new_keys:
            if (key[0] in int_keys):
                if str(key[0]) in str_keys and result.get(str(key[0])) is None:
                    result[str(key[0])] = self[str(key[0])]
                    continue
                result[key[0]] = self[key[0]]
                continue
            
            try:
                print("here")
                str_key = ', '.join(list(map(str, key)))
                result[str_key] = self[str_key]            
            except KeyError:
                raise myDictException("????, ?? ???????? ???? ???????? ????????????????, ????????????, ?????? \
                                      ?? ?????????????????? ???????????? ?? ???? ???????? ???????????????? ?????????? ????????????????????????????, \
                                      ?? ???????????? ???????????? ?? ?????????????????? ???????????? ????????????, \
                                      ?? ?????????? ???????????? ?????????????? ?????? ?????????????????? ?????????? ???? ??????????????")        
        
        return result 


    def compare(self, keys, condition, num, index_condition) -> list:
        new_keys = []
        match condition:
            case ">=":
                for key in keys:
                    if key[index_condition] >= num:
                        new_keys.append(key)
            case "<=":
                for key in keys:
                    if key[index_condition] <= num:
                        new_keys.append(key)
            
            case "==":
                for key in keys:
                    if key[index_condition] == num:
                        new_keys.append(key)
            case ">":
                for key in keys:
                    if key[index_condition] > num:
                        new_keys.append(key)
            case "<":
                for key in keys:
                    if key[index_condition] < num:
                        new_keys.append(key)
            case "<>":
                for key in keys:
                    if key[index_condition] != num:
                        new_keys.append(key)
            
            case _:
                raise myDictException(f"Invalid condition {condition}")
        
            
        return new_keys