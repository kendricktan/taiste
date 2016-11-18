from django.shortcuts import render
from home.forms import SubscriberForm

# Create your views here.
def home_view(request):
    # Did the user post
    post_success = None
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        post_success = False
        if form.is_valid():
            post_success = True
            form.save()

    return render(request, 'signup.html', {'form': SubscriberForm(), 'post_success': post_success})