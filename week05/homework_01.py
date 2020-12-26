import redis

client = redis.Redis(host='192.168.56.104',password='abc2020')


def counter(video_id: int):
    client.set(video_id, 0, nx=True)
    count_number = client.incr(video_id)
    print(count_number)
    return count_number

if __name__ == "__main__":
    counter(1001)
    counter(1002)
    counter(1001)

