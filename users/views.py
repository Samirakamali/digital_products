import random
import uuid

from django.core.cache import cache
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  

from .models import User, Device

import random
import uuid

from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device


class RegistreView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response( status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
            # return Response({'detail': 'Phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)

        # user, created = User.objects.get_or_create(phone_number=phone_number)

        Device.objects.create(users=user)  

        code = random.randint(10000, 99999)
        cache.set(str(phone_number), code, 2 * 60)

        return Response({'code': code}, status=status.HTTP_201_CREATED)

        
class GetTokenView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))

        if not cached_code:
            return Response({'detail': 'Code expired or not found'}, status=status.HTTP_400_BAD_REQUEST)

        if str(code) != str(cached_code):
            return Response({'detail': 'Invalid code'}, status=status.HTTP_403_FORBIDDEN)

        token = str(uuid.uuid4())  # we can use django authentication or JWT(json web token) instead

        return Response({'token': token}, status=status.HTTP_200_OK)


# Create your views here.
