from datetime import datetime,date
import pandas as PD
import sys
from Core.Recorder import Recorder
from Core.HeatDotQQ import HeatDotQQ

heat_dot_qq=HeatDotQQ()
while not heat_dot_qq.login(user_name=input('UserName:'),password=input('password:')):
    print('登录失败，请重试')
##输入日期范围
datestr_start=input('开始日期(默认2020-03-01）：')
if datestr_start=='':
    datestr_start='2020-03-01'
datestr_end=input('结束日期(默认2020-03-31）：')
if datestr_end=='':
    datestr_end='2020-03-31'
date_start=date.fromisoformat(datestr_start)
date_end=date.fromisoformat(datestr_end)
dates=PD.date_range(date_start,date_end)
adcode=input('请输入adcode:')
recorder=Recorder()
for date_ in dates:
    datestr=date_.strftime('%Y-%m-%d')
    json_response=heat_dot_qq.get_mall_ranking_list_competive(adcode=adcode,date=datestr)
    recorder.save_json(obj_json=json_response,file_name='MallRankingListCompetitive'+'_'+adcode+'_'+datestr+'.json')
    print(datestr)

