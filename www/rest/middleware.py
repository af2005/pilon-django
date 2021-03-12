class RestMiddleware:
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.method != "GET":
            print(request.body)
            print(request.POST)
            print(request.__dict__)
            print(type(request.method))
            print(request.method)
            print(request.path)
            print(request.path_info)

        # Code to be executed for each request/response after
        # the view is called.
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method != "GET":
            print(request.body)
            print(request.POST)
            print(request.__dict__)
            print(type(request.method))
            print(request.method)
            print(request.path)
            print(request.path_info)

        return
        # return login_required(view_func)(request, *view_args, **view_kwargs)