import requests
import re
import pymysql

db = pymysql.connect(
    host = 'localhost',
    port = 3309,
    user = 'root',
    password = '',
    database = 'test',
    charset = 'utf8'
    )

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

def baidu(company, page):
    
    # 参数设置
    num = page * 10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company +'&pn=' + str(num)
    data = requests.get(url, headers=headers).text
    p_block = '<div class="result-op c-container xpath-log new-pmd(.*?)</div></div>'
    block = re.findall(p_block, data, re.S)

    title = []
    href = []
    time = []
    source = []

    # 匹配部分
    for i in range(len(block)):
        p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)"'
        href1 = re.findall(p_href, block[i], re.S)
        href.append(href1[0])

        p_title = '<h3 class="news-title_1YtI1 ">.*?aria-label="标题：(.*?)"'
        title.append(re.findall(p_title, block[i], re.S)[0])

        p_source = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
        source.append(re.findall(p_source, data, re.S)[0])

        p_time = '<span class="c-color-gray2 c-font-normal c-gap-right-xsmall" aria-label="发布于：(.*?)"'
        time1 = re.findall(p_time, block[i], re.S)
        if time1 == []:
            time1 = ['无时间来源']
        time.append(time1[0])



    # 导入数据库代码块
    cur = db.cursor() # 获取会话指针，用来调用 SQL 语
    sql = 'SELECT * FROM `test`'
    cur.execute(sql)
    data_all = cur.fetchall() # 提取所有数据，并且赋值给 data 变量
    

    
    # 评价部分
    score = []
    keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '京东', '互联网', '拼多多']
    for i in range(len(title)):
        num = 0
        try:
            article = requests.get(href[i][0], headers = headers).text
        except:
            article = '爬取失败'
        try:
            article = article.encode('ISO-8859-1').decode('utf-8')
        except:
            try:
                article = article.encode('ISO-8859-1').decode('gbk')
            except:
                article = article
        
        p_article = '<p.*?>(.*?)</p>'
        article_main = re.findall(p_article, article, re.S)
        article = ''.join(article_main)
        for k in keywords:
            if (k in article) or (k in title[i]):
                num -= 5
        score.append(num)
    print(score)      
    
    
    # 写入部分
    title_all = []
    for j in range(len(data_all)):
        title_all.append(data_all[j][1])
    for k in range(len(title)):
        if title[k] not in title_all:
            sql_2 = 'INSERT INTO test(company, title, href, source, date, score) VALUES(%s, %s, %s, %s, %s, %s)'
            cur.execute(sql_2, (company, title[k], href[k], source[k], time[k], score[k]))
            db.commit()
    cur.close() # 关闭会话指针

# 调用函数
baidu('拼多多', 10)
        
db.close() # 关闭数据库连接
