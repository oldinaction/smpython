# -*- coding: utf-8 -*-
import json
import codecs

from testScrapy.items import HSCodeItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TestscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, HSCodeItem):
            file_name = "./out/%s.json" % item['hsCode']
            # 使用codecs解决中文乱码
            self.file = codecs.open(file_name, 'wb', encoding='utf-8')

            line = json.dumps(dict(item)) + "\n"
            self.file.write(line.decode("unicode_escape"))
        return item