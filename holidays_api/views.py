from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pathlib import Path
from datetime import datetime

import environ
import os
import requests
import json


env = environ.Env()
# Get the base dir of the project
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.secret'))

API_KEY = os.environ.get('CALEND_API_KEY',env('CALEND_API_KEY'))

# Start of class Holidays
class Holidays(APIView):

    # Start of method GET
    def get(self, request):
        # Get the current year
        try:
            year = datetime.now().year
            url = f'https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country=CO&year={year}'

            req = requests.get(url).json()
            resp = {
                "holidays": []
            }

            for d in req['response']['holidays']:
                year = d['date']['datetime']['year']
                month = d['date']['datetime']['month']
                day = d['date']['datetime']['day']
                date = f'{year}-{month}-{day}'
                resp['holidays'].append(date)
            # Send response and status OK
            return Response({'response': resp}, status=status.HTTP_200_OK)

        except Exception as exc:
            # Return server error
            print("Unexpected exception occurred: "+str(exc))
            return Response({"error": "Unexpected error occurred, please report this to Admin"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # End of method GET

# End of class Holidays
