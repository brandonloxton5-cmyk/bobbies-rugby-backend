from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def health(request):
    """
    Health check endpoint.
    - Does NOT touch the database
    - Safe for Render health checks
    """
    return Response(
        {"status": "ok"},
        status=status.HTTP_200_OK
    )


@api_view(["GET"])
def hello(request):
    """
    Simple test endpoint to confirm the API is running
    """
    return Response(
        {"message": "Bobbies Rugby API is running"},
        status=status.HTTP_200_OK
    )
