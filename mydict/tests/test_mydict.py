import pytest
from mydict.myDict import myDict, myDictException

class TestMyDict:
    def test_init(self):
        mydict = myDict()
        mydict = myDict({1 : 2, 3 : 4})
    
    def test_toSetMap(self):
        mydict = myDict({"3" : 3, "1" : 1, "2" : 2, "value" : 4})
        mydict = mydict.toSortedMap()
        
        assert list(mydict.keys()) == ["1", "2", "3", "value"]
        
                
    def test_iloc(self):
        mydict = myDict({"1" : 1, "2" : 2, "3" : 3})
        
        assert mydict.iloc(2) == 3
        
        with pytest.raises(myDictException):
            mydict.iloc(-100)
            
        mydict.clear()
        
        mydict["value1"] = 1
        mydict["value2"] = 2
        mydict["value3"] = 3
        mydict["1"] = 10
        mydict["2"] = 20
        mydict["3"] = 30
        mydict["1, 5"] = 100
        mydict["5, 5"] = 200
        mydict["10, 5"] = 300

        mydict = mydict.toSortedMap()
        
        assert mydict.iloc(0) == 10
        assert mydict.iloc(2) == 300
        assert mydict.iloc(5) == 200
        assert mydict.iloc(8) == 3
        
    def test_setitem(self):
        mydict = myDict()
        
        #Если инициализировать инициализировать таким образом, то значение в скобках затеряется навсегда
        #mydict = myDict({"3" : 0, "1, 2" : 1, "(1, 2)" : 0})
        
        mydict["1, 2"] = "without brackets"
        mydict["(1, 2)"] = "with brackets"
        assert mydict["1, 2"] == "with brackets"
        
    
    def test_ploc(self):
        mydict = myDict({"1" : 1, "2" : 2, "3" : 3})
        
        assert mydict.ploc(">=2") == {"2" : 2, "3" : 3}        
        

    