from django.shortcuts import render
from .models import Comment
from django.http import HttpResponse

import requests
from lxml import etree
from time import sleep
import re
from .models import Comment

# 首页展示
def movie_short(request):

    q = request.GET.get("q")
    if q:
        shorts = Comment.objects.filter(short__icontains=q)
    else:
        shorts = Comment.objects.filter(m_star__gt=3)
    return render(request, 'index.html', locals())

# 抓取电影短评
def crawl_movie(request):
    movie_url = "https://movie.douban.com/subject/30444960/comments?start=0&limit=20"
    resultList = get_url_name(movie_url)
    comment_list = []

    for item in resultList:
        stars_m, comment, date = item
        result = Comment(m_star=stars_m, short=comment, sentiment=date)
        comment_list.append(result)
    Comment.objects.all().delete()
    create_result = Comment.objects.bulk_create(comment_list)

    return HttpResponse("ok")


def get_url_name(myurl):

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    header = {'user-agent': ua}
    response = requests.get(myurl, headers=header)

    selector = etree.HTML(response.text)
    print(selector)

    auth_date = selector.xpath('//span[@class="comment-time "]/@title')
    movie_stars = selector.xpath(
        '//span[@class="comment-info"]/span[2]/@class')
    short_comment = selector.xpath(
        '//p[@class=" comment-content"]/span[1]/text()')

    result = []
    for i in range(0, len(auth_date)):
        date = auth_date[i]
        comment = short_comment[i]
        stars = movie_stars[i]
        stars_num = re.findall(r'\d+', stars)
        if stars_num:
            stars_m = int(stars_num[0])/10
        else:
            stars_m = 0
        i_result = (int(stars_m), comment, date)
        result.append(i_result)
    # print(result)
    return result
