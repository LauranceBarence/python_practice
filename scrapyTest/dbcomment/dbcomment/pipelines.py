# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class DbcommentPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['书名', '评论ID', '短评内容'])

    def process_item(self, item, spider):
        line = [item['title'], item['id'], item['comment']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('./dbcomment.xlsx')
        self.wb.close()
