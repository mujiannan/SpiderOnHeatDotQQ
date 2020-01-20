import requests
from PIL import Image
from io import BytesIO
import hashlib
class HeatDotQQ:
    '用于爬取腾讯位置服务|客留通(heat.qq.com/mall)数据'
    _session=requests.Session()
    def login(self,user_name,password):
        '登录到heat.qq.com/mall'
        img_validate = Image.open(BytesIO(self._session.get('https://heat.qq.com/mall/validatecode/captcha.php?sub_domain=mall').content))
        img_validate.show()
        success_validatecode=False
        success_validateuser=False
        while not(success_validatecode and success_validateuser):
            ##不向外返回验证码图片，一律手工输入验证码
            ##如后期有需要接入电子识别，可以考虑将登录方法拆分为获取验证码与登录两个方法
            code_validate=input('Please input validatecode:')
            loginPayLoad={"name":user_name+'@mall'
                          ,'passwd':hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
                          ,'validatecode':code_validate}
            response_login=self._session.post('https://heat.qq.com/mall/inner_api/login.php',data=loginPayLoad)
            json_login=response_login.json()
            if json_login['validatecode']=='ok':
                success_validatecode=True
                ##只有当验证码通过时，才存在validateuser键
                if json_login['validateuser']=='success':
                    success_validateuser=True
                else:
                    print('验证码通过，但用户名密码未通过')
                    return False
            else:
                print('验证码错误')
        print('登录成功！')
        return(True)
    def get_business_population_by_mall(self,adcode,date):
        '竞争环境-商圈影响力-商圈人口'
        params={'adcode':adcode,'date':date,'start':0,'end':100}
        response=self._session.get('https://heat.qq.com/mall/inner_api/getBusinessPopulationByMall.php',params=params)
        if response.status_code==200:
            json_response=response.json()
            return json_response
        else:
            print(response.status_code)
            return None
    def get_mall_ranking_list_competive(self,adcode,date):
        '竞争环境-商圈影响力-9平方公里商圈渗透率'
        params={'start':0,'end':100,'date':date,'adcode':adcode,'property':1,'type':403,'subtype':1}
        response=self._session.get('https://heat.qq.com/mall/inner_api/getMallRankingListCompetitive.php',params=params)
        if response.status_code==200:
            json_response=response.json()
            return json_response
        else:
            print(response.status_code)
            return None
