from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import SubscriptionInfo
from .forms import SubscriptionForm
from .webpush import process_subscription_info, get_vapid_data

from pywebpush import webpush
import json


@require_GET
def home(request):
   webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
   vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
   return render(request, 'home.html', {'vapid_key': vapid_key})


@require_POST
@csrf_exempt
def send_push_form(request):
    body = request.body
    data = json.loads(body)

    if 'head' not in data or 'body' not in data:
        return JsonResponse(status=400, data={"message": "Invalid data format"})

    # Create message
    payload = {"head": data['head'], "body": data['body']}
    payload = json.dumps(payload)

    # Get Subscription data
    subscription = SubscriptionInfo.objects.first()
    if not subscription:
        return JsonResponse(status=400, data={"message": "Subscription not exist"})

    subscription_data = process_subscription_info(subscription)
    vapid_data = get_vapid_data()

    req = webpush(subscription_info=subscription_data, data=payload, ttl=0, **vapid_data)

    return JsonResponse(status=200, data={"message": "Web push successful"})


@require_GET
def send_push(request):

    # Create message
    payload = {"head": 'Test', "body": 'Real Test'}
    payload = json.dumps(payload)

    # Get Subscription data
    subscription = SubscriptionInfo.objects.first()
    print(subscription)
    if not subscription:
        return JsonResponse(status=400, data={"message": "Subscription not exist"})
    subscription_data = process_subscription_info(subscription)
    vapid_data = get_vapid_data()

    req = webpush(subscription_info=subscription_data, data=payload, ttl=0, **vapid_data)

    return JsonResponse(status=200, data={"message": "Web push successful"})


@require_POST
@csrf_exempt
def subscribe(request):
    # Parse the  json object from post data. return 400 if the json encoding is wrong
    try:
        post_data = json.loads(request.body.decode('utf-8'))
    except ValueError:
        return HttpResponse(status=400)

    subscription_data = SubscriptionForm.process_subscription_data(post_data)
    subscription_form = SubscriptionForm(subscription_data)

    # Check if subscription info is valid
    if subscription_form.is_valid():
        # Save the subscription info with subscription data
        # as the subscription data is a dictionary and its valid
        subscription = subscription_form.save()

        # Object created
        return HttpResponse(status=200)

    return HttpResponse(status=400)
