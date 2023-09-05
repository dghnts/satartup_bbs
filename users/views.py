from django.shortcuts import render
from django.views import View

# Create your views here
class LoginRedirectView(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, "users/private.html")
    
login_redirect = LoginRedirectView.as_view()