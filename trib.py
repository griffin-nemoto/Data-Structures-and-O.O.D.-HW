
def trib(num):
    return _trib(num,dict())

def _trib(num, dict = {1:0,2:0,3:1}):
    if num == 1 or num == 2:
        return 0
    if num == 3:
        return 1
    if num not in dict:
        dict[num] = _trib(num-1,dict) + _trib(num-2,dict) + _trib(num-3,dict)
        
    return dict[num]
        