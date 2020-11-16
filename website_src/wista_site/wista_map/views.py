from django.shortcuts import render
from django.http import JsonResponse

# from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'wista_map/index.html')

# def get_data(request):
#     data = {
#         "cars": 2573,
#         "bikes": 23,
#         "pedestrians": 231,
#         "busses": 84
#     }
#     return JsonResponse(data)

# class ListUsers(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)