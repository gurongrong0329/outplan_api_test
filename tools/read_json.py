import json


class ReadJson(object):

    def __init__(self,filename):
        self.filepath='../data/'+filename

    def read_json(self):
        with open(self.filepath,'r',encoding='utf-8') as f:
            return json.load(f)

if __name__ == '__main__':
    ret=ReadJson('login.json').read_json()
    arr = []
    for k,v in ret.items():
        arr.append(v)

    # arr.append((ret.get('url'),ret.get('account'),ret.get('password'),ret.get('status')))
    print([tuple(arr)])