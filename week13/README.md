#### 下载中间件
- process_request(request,spider)
  request 对象经过下载中间件时被调用，优先级高优先
  
 - process_response(request, response, spider)
   response 对象经过狭隘中间件时被调用，优先级高后执行
   
 - process_exception(request, exception, spider)
   当如上两点抛出异常时调用
   
 - from_crawl(cls, crawler)
   使用crawler来创建中间件器对象，并返回一个中间件对象
   
  