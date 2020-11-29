import time
import datetime
import logging
import os


def weeklog():
    # 获取当期日期
    now = datetime.date.today()

    # 日志绝对路径
    logPath = '/var/log/python-{0}/week01.log'.format(now)

    # 日志所在目录
    logDir = os.path.dirname(logPath)
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    
    logging.basicConfig(filename=logPath,
                        format='%(asctime)s - %(levelname)s - [line: %(levelno)d ] %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        level=logging.INFO)
    
    logging.info('调用程序啦啦啦~')

if __name__ == '__main__':
    while True:
        weeklog()
        time.sleep(2)