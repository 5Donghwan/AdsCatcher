# -*- coding: cp949 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdsCatcher.settings")
import django
django.setup()


import json
import datetime
import time
import urllib.request

from blog.models import Blog


app_id = "1925461554405728"
app_secret = "d00b4a7b6385c0bba1d9bc3c3502539e"
access_token = app_id + "|" + app_secret
page_id = "1846148835712539"
since = "2017-06-10"
until = "2017-06-12"


def getFacebookPageFeedData(page_id, access_token, since, unitl):
    # construct the URL string
    base = "https://graph.facebook.com"
    node = "/" + page_id + "/feed"
    parameters1 = "/?fields=message,created_time,likes.limit(1).summary(true),"
    # -b - cf -  comments.fields(message,parent).summary(true) (- cannot see replies)
    # -b - changed if you add parent in  filter(stream){message,id,"parent"}, you can see parent
    parameters2 = "comments.summary(true).filter(stream){message}"
    time = "&since=%s&until=%s" % (since, until)
    access = "&access_token=%s" % access_token
    url = base + node + parameters1 + parameters2 + time + access
    print(url)  ###DEL

    # retrieve data
    data = json.loads(request_until_suceed(url))

    return data


def request_until_suceed(url):
    req = urllib.request.Request(url)
    success = False
    while success is False:
        try:
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)  # wnat to know what error it is
            time.sleep(5)
            print("Error for url %s : %s" % (url, datetime.datetime.now()))

    return response.read().decode(response.headers.get_content_charset())


def fetch_comments(status, status_message):
    com = status_message
    page = ' ' if 'comments' not in status.keys() else status['comments']
    # print json.dumps(page, indent=4, sort_keys=True) ###DELETE
    j = 0  ################DELETE
    while True:  # until no more next
        try:

            comments = ' ' if 'comments' not in status.keys() else page['data']
            ##########until no more comment in page
            i = 0
            while True:
                try:
                    # append message and comments using :]
                    # http://me2.do/5ZryZrRd(not considering codec error)
                    com = com + ' : ' + comments[i]['message'].encode('cp949', errors= 'replace').decode('cp949')
                    i = i + 1
                except:
                    break
                    ############

            # get next page comment json
            nex = json.loads(request_until_suceed(page['paging']['next']))
            page = nex
            j = j + 1;
            print("   %d th comment in one status" % j)
            # print json.dumps(page, indent=4, sort_keys=True)###DELETE

        except KeyError:  # no more next
            break

    return com


def processFacebookPageFeedStatus(status):
    # key is the name of the list
    status_message = ' ' if 'message' not in status.keys() else status['message'].encode('cp949', errors= 'replace').decode('cp949')
    # time(http://devanix.tistory.com/306)
    status_published = datetime.datetime.strptime(status['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    status_published = status_published + datetime.timedelta(hours=+9)
    status_published = status_published.strftime('%Y-%m-%d %H:%M:%S')

    num_likes = 0 if 'likes' not in status.keys() else status['likes']['summary']['total_count']
    num_comments = 0 if 'comments' not in status.keys() else status['comments']['summary']['total_count']
    com = fetch_comments(status, status_message)

    return (status_message, status_published, num_likes, com)


def fetch_feed():
    one_json = getFacebookPageFeedData(page_id, access_token, since, until)
    wan_data = []
    j = 0
    i = 0
    num = 0
    while True:
        try:
            test_status = one_json["data"][i]
            processed_test_status = processFacebookPageFeedStatus(test_status)
            wan_data.append(list(processed_test_status))
            print("%d th status in %d" % (i, num))
            i = i + 1
            num = num + 1
        except Exception as e:
            print(e)
            try:
                next_url = one_json["paging"]["next"]  # next url
                print(next_url)
                j = j + 1
                print("----")
                # print j #FOR CHECK
                one_json = json.loads(request_until_suceed(next_url))
                i = 0
                continue
            except KeyError:
                print('End of Document')
                break

    return wan_data, num


wan_data, num = fetch_feed()


def main():    
    my_feed_list = []

    for i in range(num):
        parse_data = wan_data[i][3].split(':')
        title = parse_data[0]
        content = parse_data[1:]
        date = wan_data[i][1]
        
        my_feed_list.append(Blog(feed_title=title, content=content, created_at=date))
    return my_feed_list


if __name__ == '__main__':
    from django.db import connection

    my_feed_list = main()

    Blog.objects.bulk_create(my_feed_list)

