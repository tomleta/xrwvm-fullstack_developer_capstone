from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from .restapis import get_request, analyze_review_sentiments, post_review
from djangoapp.populate import initiate
from .models import CarMake, CarModel

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    """Handle sign in request"""
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}

    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


def logout_user(request):
    """Terminate user session"""
    data = {"userName": ""}
    return JsonResponse(data)


@csrf_exempt
def registration(request):
    """Handle user registration"""
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    username_exist = False
    email_exist = False

    try:
        User.objects.get(username=username)
        username_exist = True
        User.objects.get(email=email)
        email_exist = True
    except Exception:
        logger.debug("{} is new user".format(username))

    if not username_exist and not email_exist:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)

    data = {"userName": username, "error": "Already Registered"}
    return JsonResponse(data)


def get_cars(request):
    """Retrieve all cars"""
    count = CarMake.objects.filter().count()
    if count == 0:
        initiate()

    car_models = CarModel.objects.select_related('car_make')
    cars = [{"CarModel": car_model.name, "CarMake": car_model.car_make.name}
            for car_model in car_models]

    return JsonResponse({"CarModels": cars})


def get_dealerships(request, state="All"):
    """Retrieve dealerships by state"""
    endpoint = "/fetchDealers" if state == "All" else "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_reviews(request, dealer_id):
    """Retrieve reviews for a dealer"""
    if not dealer_id:
        return JsonResponse({"status": 400, "message": "Bad Request"})

    endpoint = "/fetchReviews/dealer/" + str(dealer_id)
    reviews = get_request(endpoint)

    for review_detail in reviews:
        response = analyze_review_sentiments(review_detail['review'])
        review_detail['sentiment'] = response['sentiment']

    return JsonResponse({"status": 200, "reviews": reviews})


def get_dealer_details(request, dealer_id):
    """Retrieve dealer details"""
    if not dealer_id:
        return JsonResponse({"status": 400, "message": "Bad Request"})

    endpoint = "/fetchDealer/" + str(dealer_id)
    dealership = get_request(endpoint)
    return JsonResponse({"status": 200, "dealer": dealership})


def add_review(request):
    """Add a review for a dealer"""
    if request.user.is_anonymous:
        return JsonResponse({"status": 403, "message": "Unauthorized"})

    data = json.loads(request.body)
    try:
        post_review(data)
        return JsonResponse({"status": 200})
    except Exception:
        return JsonResponse({
            "status": 401,
            "message": "Error in posting review"
        })
