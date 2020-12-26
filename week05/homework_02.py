import redis
import time

client = redis.Redis(host='192.168.56.104', password='abc2020')

def sendsms(telephone_number: int, content: str, key=None):
    if client.exists(telephone_number):
        count_num = client.get(telephone_number)
        if int(count_num.decode()) < 5:
            client.incr(telephone_number)
            print(f"发送成功: {content}")
        else:
            extime=client.ttl(telephone_number)
            print(f"1分钟内发送次数超过 5 次, 请等待{extime}秒")
    else:
        client.set(telephone_number, 0, nx=True)
        client.expire(telephone_number, time=60)

if __name__ == "__main__":
    while True:
        sendsms(1234567890, content="hello")
        time.sleep(5)