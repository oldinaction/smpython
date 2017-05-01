# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.contrib.loader.processor import MapCompose, TakeFirst
from w3lib.html import remove_tags


class HSCodeItem(scrapy.Item):
    """HSCodeItem, 存放抓去数据的临时容器"""

    '''申报信息'''

    # 商品编码
    hsCode = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 计量单位
    unit = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 商品名称
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 商品英文名称
    enName = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 申报要素-上海版
    shanghai = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 申报要素-全国版
    china = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )

    '''税费信息'''

    # 税费信息-进口
    # 最惠国税率(%)
    lbzuihui = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 暂定税(%)
    lbzanding = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 普通税率(%)
    lbputong = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 增值税(%)
    lbzengzhi = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 协定税率(%)
    lbxieding = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 协定税率详情(另外一个页面)
    lbxieding_detail = scrapy.Field()
    # 特惠税率(%)
    lbtehui = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    lbtehui_detail = scrapy.Field()
    # 消费税率(%)
    lbxiaofei = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 复合从量(%)
    lbfuhe = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 双反税率(%)
    lbshuangfan = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # ITA税率(%)
    lbita = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )

    # 税费信息-出口
    # 税率(%)
    lbckshuilv = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 退税(%)
    lbcktuishui = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 暂定税率(%)
    lbckzanding = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )

    '''监管信息'''

    # 海关监管条件
    haiguanjianguan = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 检验检疫内别
    jianyanjianyi = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )

    '''参考信息'''

    # 图片库
    tupianku = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 历史库
    lishiku = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )


class XieDingItem(scrapy.Item):
    """协定费率详情"""

    # 地区
    key = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    # 费率
    value = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )