from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .restapis import get_request, analyze_review_sentiments, post_review

from .models import CarMake, CarModel


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    data = {"userName":""}
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    # Check if user already exists
    username_exist = False
    email_exist = False
    try:
        User.objects.get(username=username)
        username_exist = True
        User.objects.get(email=email)
        email_exist = True
    except:
        logger.debug("{} is new user".format(username))

    if not username_exist and not email_exist:
        user = User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)


def get_cars(request):
    print("getting count")
    count = CarMake.objects.filter().count()
    print("count =", count)
    if (count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels":cars})

#Update the `get_dealerships` render list of dealerships all by default, particular state if state is passed
def get_dealerships(request, state="All"):
    if(state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/"+state
    dealerships = get_request(endpoint)
    return JsonResponse({"status":200,"dealers":dealerships})

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...
def get_dealer_reviews(request, dealer_id):
    if (dealer_id):
        endpoint = "/fetchReviews/dealer/{}".format(dealer_id)
        dealer_reviews = get_request(endpoint)
        if len(dealer_reviews) > 0:
            for review in dealer_reviews:
                sentiment = analyze_review_sentiments(review['review'])
                print(sentiment)
                review['sentiment'] = sentiment['sentiment']
        return JsonResponse({"status":200, "dealer_reviews":dealer_reviews})
    else:
        return JsonResponse({"status":400, "message":"Bad Request: Missing dealer_id"})

def get_dealer_details(request, dealer_id):
    if (dealer_id):
        endpoint = "/fetchDealer/{0}".format(dealer_id)
        dealer_details = get_request(endpoint)
        return JsonResponse({"status":200, "dealer_details":dealer_details})
    else:
        return JsonResponse({"status":400,"message":"Bad Request: Missing dealer_id"})

def add_review(request):
    if(request.user.is_anonymous == False):
        data = json.loads(request.body)
        try:
            response = post_review(data)
            return JsonResponse({"status":200})
        except:
            return JsonResponse({"status":401,"message":"Error in posting review"})
    else:
        return JsonResponse({"status":403,"message":"Unauthorized"})