from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def classify_number(request):
    # Get the number from the query parameter
    number = request.GET.get('number')

    # Validate the input
    if not number or not number.lstrip('-').isdigit():
        return JsonResponse({
            "number": number if number else "null",
            "error": True
        }, status=400)

    number = int(number)

    # Check if the number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check if the number is perfect
    def is_perfect(n):
        if n < 2:
            return False
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

    # Check if the number is an Armstrong number
    def is_armstrong(n):
        digits = [int(d) for d in str(n)]
        length = len(digits)
        return sum([d**length for d in digits]) == n

    # Calculate the sum of digits
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    # Fetch fun fact from Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{number}?json")
        fun_fact = response.json().get('text', 'No fun fact available.')
    except requests.RequestException:
        fun_fact = 'No fun fact available.'

    # Determine properties
    properties = []
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    # Return JSON response
    return JsonResponse({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    })