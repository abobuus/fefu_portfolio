from rest_framework.views import APIView
from .serializers import UserInfoSerializers
from rest_framework.response import Response


class UserInfoAPIView(APIView):
    def post(self, request):
        serializer = UserInfoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.get_response())
