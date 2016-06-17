# -*- coding: utf-8 -*-
__author__ = 'kangkang'
import re
import rsa
import base64
import requests
import binascii
from PIL import Image
from urllib import parse
import logging
import time

session = requests.Session()


class Weibo_login(object):
    """
    weibo login. try to call login() to run the class 
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 获取加密后的账号su值
    def get_su(self, username):
        # 将username转换成html字符
        username_html = parse.quote(username).encode('utf-8')
        # 进行base64编码
        su = base64.b64encode(username_html).decode('utf-8')
        return su

    # 获取其他post时所需的data值的字典
    def get_sth(self, su):
        # 改字典内的数据经过精简，只有在这些数据存在下才不影响获得所需的准确数据
        payload = {'entry': 'weibo', 'rsakt': 'mod', 'su': su, 'checkpin': '1', "client": "ssologin.js(v1.4.18)",
                   "_": str(int(time.time() * 1000))}
        res = requests.get('http://login.sina.com.cn/sso/prelogin.php',
                           params=payload).text
        res = eval(res)
        return res

    # 对密码进行加密
    def get_sp(self, password, pubkey, servertime, nonce):
        # rsa加密

        key = rsa.PublicKey(int(pubkey, 16), 65537)
        message = str(servertime) + '\t' + str(nonce) + '\n' + password
        passwd = rsa.encrypt(message.encode("utf8"), key)
        # 将加密信息转换成16进制
        sp = binascii.b2a_hex(passwd)
        # print(sp)
        return sp

    # 获取验证码
    def get_pin(self, pcid):
        payload = {'s': '0', 'p': pcid}
        pin_url = "http://login.sina.com.cn/cgi/pin.php"
        pin_picture = session.get(pin_url, params=payload)
        with open("cha.jpg", 'wb') as f:
            f.write(pin_picture.content)
            f.close()
        try:
            im = Image.open("cha.jpg")
            im.show()
            im.close()
        except:
            print("请到当前目录下，找到验证码后输入")

    # 调度中心
    def login(self):
        su = self.get_su(self.username)

        res = self.get_sth(su)
        nonce = res['nonce']
        servertime = res['servertime']
        rsakv = res['rsakv']
        pubkey = res['pubkey']
        showpin = res['showpin']
        sp = self.get_sp(self.password, pubkey, servertime, nonce)
        # 构造headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/47.0.2526.80 Safari/537.36'
        }
        # 构造登陆需要上传的表单form data
        payload = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'userticket': '1',
            'pagerefer': 'http://login.sina.com.cn/sso/logout.php?entry=miniblog'
                         '&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F',
            'vsnf': '1',
            'su': su,
            'service': 'miniblog',
            'servertime': servertime,
            'nonce': nonce,
            'pwencode': 'rsa2',
            'rsakv': rsakv,
            'sp': sp,
            'encoding': 'UTF-8',
            'prelt': '106',
            'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback='
                   'parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META'
        }
        # 判断是否需要验证码
        if showpin:
            pcid = res['pcid']
            self.get_pin(pcid)
            payload['door'] = input('请输入验证码:')
            res = session.post('http://login.sina.com.cn/sso/login.php?client='
                               'ssologin.js(v1.4.18)', data=payload, headers=headers)
            res = res.content.decode('GBK')
            # print(res)
        else:
            res = session.post('http://login.sina.com.cn/sso/login.php?client='
                               'ssologin.js(v1.4.18)', data=payload, headers=headers)
            res = res.content.decode('GBK')
            # print(res)
        pattern = r'location\.replace\([\'"](.*?)[\'"]\)'
        login_url = re.findall(pattern, res)[0]
        # print(login_url)
        login_test = session.get(login_url, headers=headers)
        #print(page.content.decode('gb2312'))
        pattern2 = r"location\.replace\([\'\"](?P<login_url>.*)[\'\"]\)"


        uuid_res = re.findall(r'"uniqueid":"(.*?)"', page.content.decode('gb2312'), re.S)[0]
        weibo = session.get('http://weibo.com/%s/profile?topnav=1&wvr=6&is_all=1' % uuid_res)
        id_pa = r'<title>(.*?)</title>'
        # print(weibo_page.content.decode("utf-8"))
        weiboID = re.findall(id_pa, weibo.content.decode("utf-8"), re.S)[0]
        test = weibo.content.decode('utf-8')

        logging.warning('{}成功登录,id为{}'.format(weiboID[:-3], uuid_res))


class Weibo_Fetch(Weibo_login):
    """
    Try to fetch the response
    """

    def __init__(self, username, password):
        Weibo_login.__init__(self, username, password)
        self.login()

    def analyse_html(self, url):
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s\t%(levelname)s\t%(message)s')
    username = 'ckj20060101@sina.com'
    password = 'V0cal0id'

    test = Weibo_Fetch(username, password)

    fetch_url = 'http://weibo.com/u/3974469906?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop'

    test.analyse_html(fetch_url)
