# -*- coding: utf-8 -*-
# 系统库
import os
import socket
import scrapy
from scrapy import signals
from scrapy.contrib.loader import ItemLoader

from testScrapy.items import HSCodeItem
from testScrapy.tools.smexcel import SmExcel

import sys

# 防止运行os.system等命令时中文乱码
reload(sys)
sys.setdefaultencoding('utf8')


class HSCodeSpider(scrapy.Spider):
    name = "hscode"

	domain = "http://www.mydomain.com"
    # hscode代码文件(注意相对路径加./)
    hscode_file = './testScrapy/spiders/hscode.xls'
    # 分布式爬取
    task_index = {
        '192.168.17.212': 1,
        '10.172.203.23': 1,
        '172.31.2.2': 4001,
        '172.31.2.84': 8001,
    }
    # 每台机器爬取的数量
    # TODO task_count = 4000
    task_count = 10
    # 本机要开始爬取的下标
    this_task_index = task_index.get(socket.gethostbyname(socket.gethostname()))

    # 减慢爬取速度为2s, 防止被禁
    download_delay = 2

    '''
    # 可代替start_requests函数
    start_urls = [
        domain + 'HS_Search/Hs_ZhcxDetail.aspx?spbm=7616999000',
    ]
    '''
    def start_requests(self):
        # 机器名
        hostname = socket.gethostname()
        print hostname
        # 内网ip
        print socket.gethostbyname(hostname)
        print socket.gethostbyname_ex(hostname)

        # 运行shell命令
        os.system("rm ./out/error.logs ./out/info.logs")
        os.system("touch ./out/error.logs ./out/info.logs")
        # 获取excel数据
        rows = SmExcel().excel_row_byindex(file=self.hscode_file, colnameindex=self.this_task_index)
        for i in range(0, self.task_count):
            try:
                hscode_id = rows.next()[0]
                url = self.domain + 'HS_Search/Hs_ZhcxDetail.aspx?spbm=' + str(hscode_id)
                # 类似于generator（生成器），此时返回一个iterable对象，使用iterable_obj.next()获取下一条数据
                yield scrapy.Request(url=url, callback=self.parse)
            except StopIteration, e:
                os.system("echo 'StopIteration index: " + str(i) + "    %s' >> ./out/info.logs" % e)
                print e

    '''
    爬虫主入口, 运行命令: scrapy crawl hscode
    '''
    def parse(self, response):
        hscode = ItemLoader(item=HSCodeItem(), response=response)

        try:
            '''申报信息'''
            hscode.add_css("hsCode", "table>tr>td:nth-child(3)>span")
            hscode.add_css("unit", "table>tr>td:nth-child(5)>span")
            hscode.add_css("name", "table>tr:nth-of-type(2)>td:nth-child(2)>span")
            hscode.add_css("enName", "table>tr:nth-of-type(2)>td:nth-child(4)>span")
            # 申报信息-申报要素
            hscode.add_css("shanghai", "table>tr:nth-of-type(3)>td:nth-child(3)>span")
            hscode.add_css("china", "table>tr:nth-of-type(4)>td:nth-child(2)>span")

            '''税费信息'''
            # 进口
            hscode.add_css("lbzuihui", "table>tr:nth-of-type(5)>td:nth-child(4)>span")
            hscode.add_css("lbzanding", "table>tr:nth-of-type(5)>td:nth-child(6)>span")
            hscode.add_css("lbputong", "table>tr:nth-of-type(5)>td:nth-child(8)>span")
            hscode.add_css("lbzengzhi", "table>tr:nth-of-type(5)>td:nth-child(10)>span")

            # 协定税率(self.domain + 'HS_Search/Tanchu.aspx?spbm=7616999000&type=xieding')
            hscode.add_css("lbxieding", "table>tr:nth-of-type(5)>td:nth-child(12)>span")
            if response.css("table>tr:nth-of-type(5)>td:nth-child(12)>a::text").extract_first() is not None:
                # 异步请求
                yield scrapy.Request(self.domain + 'HS_Search/Tanchu.aspx?type=xieding&spbm=' + hscode.load_item()['hsCode'], meta={'hscode': hscode},
                                     callback=self.parse_xieding)

            # 特惠税率(self.domain + 'HS_Search/Tanchu.aspx?spbm=7616999000&type=tehui')
            hscode.add_css("lbtehui", "table>tr:nth-of-type(6)>td:nth-child(2)>span")
            hscode.add_css("lbxiaofei", "table>tr:nth-of-type(6)>td:nth-child(4)>span")
            hscode.add_css("lbfuhe", "table>tr:nth-of-type(6)>td:nth-child(6)>span")
			
            # 双反税率(HS_Search/Hs_Fanqingxiao.aspx?spcode=0207141100)
			if response.css("table>tr:nth-of-type(6)>td:nth-child(8)>a::text").extract_first() is not None:
                hscode.add_css("lbshuangfan", "table>tr:nth-of-type(6)>td:nth-child(8)>a")
                yield scrapy.Request(self.domain + 'HS_Search/Hs_Fanqingxiao.aspx?spcode=' + hscode.load_item()['hsCode'],
                    meta={'hscode': hscode, 'page_index': 1},
                    callback=self.parse_shuangfan)
            else:
                hscode.add_css("lbshuangfan", "table>tr:nth-of-type(6)>td:nth-child(8)>span")
				
            hscode.add_css("lbita", "table>tr:nth-of-type(6)>td:nth-child(10)>span")
            # 出口
            hscode.add_css("lbckshuilv", "table>tr:nth-of-type(7)>td:nth-child(3)>span")
            hscode.add_css("lbcktuishui", "table>tr:nth-of-type(7)>td:nth-child(5)>span")
            hscode.add_css("lbckzanding", "table>tr:nth-of-type(7)>td:nth-child(7)>span")

            '''监管信息'''
            hscode.add_css("haiguanjianguan", "table>tr:nth-of-type(8)>td:nth-child(3)>span")
            hscode.add_css("jianyanjianyi", "table>tr:nth-of-type(8)>td:nth-child(5)>span")

            '''参考信息'''
            hscode.add_css("tupianku", "table>tr:nth-of-type(9)>td:nth-child(3)>span")
            hscode.add_css("lishiku", "table>tr:nth-of-type(9)>td:nth-child(5)>span")

            os.system("echo " + hscode.load_item()['hsCode'] + " >> ./out/info.logs")
            yield hscode.load_item()
        except Exception, e:
            os.system("echo '%s    parse Exception: %s' >> ./out/info.logs" % (hscode.load_item()['hsCode'], e))
			os.system("echo '%s' >> ./out/error.logs" % hscode.load_item()['hsCode'])

    '''
    解析协定费率(self.domain + 'HS_Search/Tanchu.aspx?spbm=7616999000&type=xieding')
    '''
    def parse_xieding(self, response):
        hscode = response.meta['hscode']

        try:
            lbxieding_detail = []
            for tr in response.css('table>tr'):
                lbxieding_detail.append({'key': tr.css('td::text').extract_first(),
                                         'value': tr.css('span::text').extract_first()})
			
			# lbxieding_detail需要在HSCodeItem中声明
            hscode.add_value("lbxieding_detail", lbxieding_detail)
            return hscode.load_item()
        except Exception, e:
            os.system("echo '%s    parse_xieding Exception: %s' >> ./out/error.logs" % (hscode.load_item()['hsCode'], e))
			os.system("echo '%s' >> ./out/error.logs" % hscode.load_item()['hsCode'])
			
	'''
    解析双反费率(HS_Search/Hs_Fanqingxiao.aspx?spcode=0207141100). ###使用post提交
    '''
    def parse_shuangfan(self, response):
        hscode = response.meta['hscode']
        page_index = response.meta['page_index']
        try:
            page_size = response.css('table>tr:nth-of-type(8)>td>span:nth-of-type(2)::text').extract_first()

            if not os.path.exists('./out/shuangfan'):
                os.system("mkdir ./out/shuangfan")
            if not os.path.exists('./out/shuangfan/' + hscode.load_item()['hsCode']):
                os.system("mkdir ./out/shuangfan/%s" % hscode.load_item()['hsCode'])

            os.system("echo '%s' >> ./out/shuangfan/%s/%s.html" % (response.body, hscode.load_item()['hsCode'], page_index))

            page_index = page_index + 1
			# page_size从页面获取的为字符串型, 进行大小比较需要转成int型
            if page_index <= int(page_size):
                yield scrapy.FormRequest(
                    self.domain + 'HS_Search/Hs_Fanqingxiao.aspx?spcode=' + hscode.load_item()['hsCode'],
                    meta={'hscode': hscode, 'page_index': page_index},
                    formdata={'__EVENTTARGET': 'gv_FanQingXiaoList$ctl09$btnGo',
                              '__EVENTARGUMENT': '',
                              '__VIEWSTATE': response.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first(),
                              '__VIEWSTATEENCRYPTED': '',
                              '__EVENTVALIDATION': response.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first(),
                              'gv_FanQingXiaoList$ctl09$txtNewPageIndex': str(page_index)},
                    callback=self.parse_shuangfan)
        except Exception, e:
            os.system("echo '%s    parse_shuangfan Exception: %s' >> ./logs/info.log" % (hscode.load_item()['hsCode'], e))
            os.system("echo '%s' >> ./logs/error.log" % hscode.load_item()['hsCode'])

	'''
    爬虫执行完成后执行程序。参考signals信号
    '''
	@classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(HSCodeSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        os.system("tar -czf out.tar.gz ./out/ ")
