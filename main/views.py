
from django.urls import reverse
from django.shortcuts import redirect, render
import stripe
stripe.api_key = "sk_test_51Kd8gGAWQSg3LicKwKJSs4VgrvNLysUdcORVZgNNSv8rbJunT8SSJfyPLHjjGpbiwR67ICfqjGAIazNYwS0P7OaL00uM17LbCj"

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:',request.POST)
         
    return redirect(reverse('success', args=[amount]))

def success(request, args):
    amount = args
    return render(request,'main/success.html', {'amount': amount})