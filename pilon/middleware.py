from django.contrib.auth.decorators import login_required
from django.conf import settings
import re


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Called Middleware")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response
        public_urls = getattr(settings, "PUBLIC_URLS", ())
        public_urls += (getattr(settings, "LOGIN_URL", None),)
        public_urls += (getattr(settings, "LOGOUT_REDIRECT_URL", None),)
        self.public_view_urls = [re.compile(rf"^{url}") for url in public_urls]

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(self.public_view_urls)
        if self.is_public_url(request.path):
            return view_func(request, *view_args, **view_kwargs)
        return login_required(view_func)(request, *view_args, **view_kwargs)
        # return login_required(view_func)(request, *view_args, **view_kwargs)

    def is_public_url(self, url):
        return any(public_url.match(url) for public_url in self.public_view_urls)
