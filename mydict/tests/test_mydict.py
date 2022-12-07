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
        
        #Если инициализировать словарь таким образом, то значение в скобках затеряется навсегда
        #mydict = myDict({"3" : 0, "1, 2" : 1, "(1, 2)" : 0})
        
        mydict["1, 2"] = "without brackets"
        mydict["(1, 2)"] = "with brackets"
        assert mydict["1, 2"] == "with brackets"
        
    
    def test_ploc(self):
        assert myDict({"1" : 1, "2" : 2, "3" : 3}).ploc(">=2") == {"2" : 2, "3" : 3}
        
        assert myDict({1 : 1, "1" : 2,  0 : 3}).ploc(">= 1") == {1 : 1, "1" : 2}
                
        assert myDict({2 : 1,"2": 2, "2, 3" : 0, "3, 5": 0, "2, 3, 5": 0, "value" : 0}).ploc(">= 2, >= 3") \
                        == {"2, 3" : 0, "3, 5" : 0}    

        assert myDict({"2": 0, "0" : 0}).ploc(">= 1.10") == {"2" : 0}        
        
        assert myDict({"value" : 0, "1" : 0}).ploc("== 1") == {"1" : 0}
        
        assert myDict({"value1" : 0, "value2" : 0}).ploc("== 1") == {}
        
        assert myDict({"value" : 0, "1" : 0}).ploc("                ==                  1                  ") == {"1" : 0}
        
        assert myDict({"1" : 0, 2 : 0}).ploc("<= 1") == {"1" : 0}
        
        assert myDict({"1" : 0, 2 : 0, 0 : 0}).ploc("<> 1") == {2 : 0, 0 : 0}
        
        assert myDict({"1" : 0, 2 : 0, 0 : 0}).ploc("< 1") == {0 : 0}
        
        assert myDict({"1" : 0, 2 : 0}).ploc("> 1") == {2 : 0}
        
        with pytest.raises(myDictException):
            myDict({"1, 2" : 0}).ploc("== 1, >><<<><><><><><><><><> 2")
        with pytest.raises(myDictException):    
            myDict({"1,2" : 0}).ploc("== 1, == 2")
    
    def test_ploc_by_Kiselev(self):
        my_map = myDict()
        my_map["value1"] = 1
        my_map["value2"] = 2
        my_map["value3"] = 3
        my_map["1"] = 10
        my_map["2"] = 20
        my_map["3"] = 30
        my_map["(1, 5)"] = 100
        my_map["(5, 5)"] = 200
        my_map["(10, 5)"] = 300
        my_map["(1, 5, 3)"] = 400
        my_map["(5, 5, 4)"] = 500
        my_map["(10, 5, 5)"] = 600
        
        assert my_map.ploc(">=1") == {"1" : 10, "2" : 20, "3" : 30}
        assert my_map.ploc("<3") == {"1" : 10, "2" : 20}
        assert my_map.ploc(">=10, >0") == {"10, 5" : 300}
        assert my_map.ploc("<5, >=5, >=3") == {"1, 5, 3" : 400}            
    