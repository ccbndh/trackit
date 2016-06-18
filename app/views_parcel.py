from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from app.models import Parcel


class ParcelList(APIView):
    """
    List all snippets, or create a new task spider.
    """

    queryset = Parcel.objects.all()

    def post(self, request):
        """
        ---
        parameters:
            - name: parameters
              type: json
              paramType: body
              description: "`parcel_id`"
              defaultValue: '{"parcel_id": "30929083467443"}'
        response_serializer: ''
        responseMessages:
            - code: 400
              message: '{"message": "", "data": ""}'
            - code: 200
              message: '{"message": "", "data": ""}'
        """
        return Response({'message': ''}, status=status.HTTP_200_OK)
