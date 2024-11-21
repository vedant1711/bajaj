import base64
import mimetypes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def bfhl_view(request):
    if request.method == 'GET':
        # Return hardcoded operation code
        return Response({"operation_code": 1}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Extract data from the request
        data = request.data.get('data', [])
        file_b64 = request.data.get('file_b64', None)
        
        # User ID
        user_id = "trideep_nandi_14082003"  # Replace with dynamic data if needed
        
        # Parse numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase_alphabet = (
            [max(lowercase_alphabets)] if lowercase_alphabets else []
        )
        
        # Prime number check
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        is_prime_found = any(is_prime(int(num)) for num in numbers)
        
        # File handling
        file_valid, file_mime_type, file_size_kb = False, None, None
        if file_b64:
            try:
                file_data = base64.b64decode(file_b64)
                file_size_kb = len(file_data) / 1024
                file_mime_type = mimetypes.guess_type("file")[0]
                file_valid = bool(file_mime_type)
            except Exception:
                file_valid = False
        
        # Response
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": "nandi.trideep2003@gmail.com",
            "roll_number": "0827CS211248",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet,
            "is_prime_found": is_prime_found,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb,
        }
        return Response(response, status=status.HTTP_200_OK)
