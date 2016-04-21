# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class myImagePipelines(ImagesPipeline):
    def get_media_requests(self, item, info):
        #通过mate把item绑定到request中 ，其他地方可以使用
        return [Request(x, meta={'name': item["name"]})
                for x in item.get('image_urls', [])]

    def file_path(self, request, response=None, info=None):
        fullname = request.meta['name'][0]
        part = u"，"
        ps = part.encode("gbk")
        s = fullname.encode("gbk")
        pos = s.rfind(ps)
        dir = s[:pos]
        name = s[pos+2:]
        return 'full/%s/%s.jpg' %(dir,name)


