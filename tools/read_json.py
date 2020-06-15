import json

class ReadJson(object):

    def __init__(self, filename):
        self.filepath = '../data/' + filename

    def read_json(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    #获取json参数中所有case值
    def get_data(self):
        ret = self.read_json()
        arr1 = []
        arr2 = []
        arr3 = []
        for v in ret.values():
            arr1.append(v)

        for i in arr1:
            for k, v in i.items():
                arr2.append(v)
            arr2 = tuple(arr2)
            arr3.append(arr2)
            arr2 = []
        return arr3

    #获取json参数中的一个case值
    def get_single_data(self,key):
        arr = []
        ret = self.read_json()
        for k in ret.keys():
            if k == key:
                for v in ret[k].values():
                    arr.append(v)
        return [tuple(arr)]
