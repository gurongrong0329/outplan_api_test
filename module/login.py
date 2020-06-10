#倒包requests,json
import requests
import json
import hashlib
import rsa
import base64

#定义login类，login方法
class Login:

    def __init__(self,address):
        self.address=address
        self.login_url = '/newLogin/doLogin'
        self.logout_url = '/newLogin/logout'
        self.getPublicKey='/newLogin/getPublicKey'

    # 获取公钥
    def get_PublicKey(self):
        res = requests.get(self.address + self.getPublicKey)
        return json.loads(res.text)

    def get_login(self,account,password):
        # md5加密
        md = hashlib.md5()
        md.update(password.encode())
        # 获取公钥
        pubkey = self.get_PublicKey()
        b_str = base64.b64decode(pubkey['data'])
        # 转换成16进制
        hex_str = b_str.hex()
        # 找到模数和指数的开头结束位置
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2

        modulus = hex_str[m_start:m_start + m_len]
        exponent = hex_str[e_start:e_start + e_len]
        rsa_pubkey = rsa.PublicKey(int(modulus, 16), int(exponent, 16))
        # rsa加密
        pswd = rsa.encrypt(md.hexdigest().encode('utf-8'), rsa_pubkey)

        headers = {'Content-Type': 'application/json'}

        data = {'userName': account, 'password': str(base64.b64encode(pswd), 'utf-8'), 'publicKey': pubkey['data']}

        res = requests.post(self.address + self.login_url, headers=headers, data=json.dumps(data))
        assert res.status_code,200
        return json.loads(res.text)