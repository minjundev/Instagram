from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from uuid import uuid4
import os
from Instagram.settings import MEDIA_ROOT


class Main(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request, "instagram/main.html", context=dict(feed_list=feed_list))


class UploadFeed(APIView):
    # noinspection PyMethodMayBeStatic
    def post(self, request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)

        return Response(status=200)
