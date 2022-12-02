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
        pass
        
        