from django.utils.deprecation import MiddlewareMixin



class MyMw(MiddlewareMixin):


    # 每次请求到达主urls会调用
    #返回None 会继续执行 HttpResponse请求终止，直接响应
    def process_request(self,request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response

    def process_exception(self, request, exception):
        print("中间件方法 process_exception 被调用")

    def process_template_response(self, request, response):
        print("中间件方法 process_template_response 被调用")
        return response

class MyMw2(MiddlewareMixin):


    # 每次请求到达主urls会调用
    #返回None 会继续执行 HttpResponse请求终止，直接响应
    def process_request(self,request):
        print("2中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("2中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("2中间件方法 process_response 被调用")
        return response

    def process_exception(self, request, exception):
        print("2中间件方法 process_exception 被调用")

    def process_template_response(self, request, response):
        print("2中间件方法 process_template_response 被调用")
        return response