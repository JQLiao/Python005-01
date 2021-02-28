# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings

class mysqlPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.connect = pymysql.connect(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            port = settings['MYSQL_PORT'],
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO maoyan(name, star, releasetime, created_at) VALUES(%s, %s, %s, %s)"
        params = (item["name"], item["star"], item["releasetime"], item["created_at"])
        self.cursor.execute(sql,params)
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()