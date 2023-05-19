from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    """
    1. get all the drinks
    2. serialize them
    3. return json
    """
    if request.method == 'GET':
        drinks = Drink.objects.all() # Access the Drink class and get all the drink
        serializer = DrinkSerializer(drinks, many = True) # It will serialize many(all) of them and we have list
        #return JsonResponse({'drinks':serializer.data}, safe=False)
        ##return JsonResponse({'drinks':serializer.data}) # Since we are no lonnger dealing witj non-dict object, but with dict object (the use of curly braces has made it a dictionary), we no longer need Safe = False
        return Response(serializer.data)

    if request.method == 'POST': # Add a drink to the DB
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id, format=None):

    try: 
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DrinkSerializer(drink, data = request.data)
        # check if the serializer is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)