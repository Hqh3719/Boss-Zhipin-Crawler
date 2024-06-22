import requests
import csv

# 创建文件
f = open('boss_zhipin_jobs.csv', mode='a', encoding='utf-8', newline='')
# 使用字典写入csv文件
csv_writer = csv.DictWriter(f, fieldnames=[
    '职位',
    '薪资',
    '经验',
    '学历',
    '城市',
    '地区',
    '公司名称',
    '公司规模',
    '职位描述',
    '公司福利',
])
# 写入表头
csv_writer.writeheader()
# 确认请求url地址
url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=python&city=101280100&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30'
# 设置请求头，模拟浏览器访问
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
    'cookie': 'wd_guid=d859bcd6-64e9-4c1a-86ef-b879193cec6c; historyState=state; _bl_uid=zzlw1iOd21eg18uLyoC0qp7lh2Uz; lastCity=101280100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1685534187,1685548152,1685593075,1685706186; wt2=DAxMgwouiHcn2t8dr6cwpluOJzebQR7KF-AjMOaC8YThisJ_n4UgZFjNnvfHnxmeLzFf2d109ttihOfuu-wAfxA~~; wbg=0; __zp_seo_uuid__=03426e1e-0a0a-4deb-a4a7-550c5f51e326; __g=-; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1685716247; __zp_stoken__=40daeGg97QXNHN2QBIUJidm8kLVBMe14IKikdJ3IAclRFdWZmYjlSPXVFISdAA3t%2BD2RWBhk3dg8leyZAJQhxbhwPNEc9eRotFlxlDwFfSiVUAxJ3cjADWTMEG3xOBBg1TV1kfRxWXQVyYXQ%3D; __c=1685706185; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3Dpython%26city%3D101280100&s=3&g=&friend_source=0&s=3&friend_source=0; __a=85088397.1684978766.1685593074.1685706185.83.6.42.42; geek_zp_token=V1RNMiE-T-3VltVtRvxxgfKy236DjWxSg~',
}
# 发送请求
response = requests.get(url=url, headers=headers)
# 解析json数据并写入csv文件
for index in response.json()['zpData']['jobList']:
    dit = {
        '职位': index.get('jobName', ''),
        '薪资': index.get('salaryDesc', ''),
        '经验': index.get('jobExperience', ''),
        '学历': index.get('jobDegree', ''),
        '城市': index.get('cityName', ''),
        '地区': index.get('areaDistrict', ''),
        '公司名称': index.get('brandName', ''),
        '公司规模': index.get('brandScaleName', ''),
        '职位描述': index.get('skills', ''),
        '公司福利': index.get('welfareList', ''),
    }
    # 写入数据
    csv_writer.writerow(dit)
    # 打印数据
    print(dit)
# 关闭文件
f.close()
