## Number Classification API

A Django-based API that classifies a given number and returns its mathematical properties along with a fun fact.

Table of Contents

1. Overview

2. Features

3. Requirements

4. Setup

5. API Endpoint

6. Example Requests and Responses

7. Deployment


### Overview

This API accepts a number as input and returns:

- Mathematical properties of the number (e.g., prime, perfect, Armstrong, odd/even).

- A fun fact about the number fetched from the Numbers API.

- The sum of the digits of the number.

The API is built using Django and is designed to be simple, fast, and easy to use.

### Features

- Number Classification: Determines if a number is prime, perfect, Armstrong, or odd/even.

- Digit Sum Calculation: Calculates the sum of the digits of the number.

- Fun Fact Integration: Fetches a fun fact about the number from the Numbers API.

- Error Handling: Returns appropriate error messages for invalid inputs.

- CORS Support: Handles Cross-Origin Resource Sharing (CORS) for frontend integration.

### Requirements

- Python 3.8+

- Django 4.0+

- requests library (for fetching fun facts)

- django-cors-headers (for CORS support)

### Setup

1. Clone the Repository
   

```
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api

```
2. Set Up a Virtual Environment
   

```

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
1. Install Dependencies
`
`pip install -r requirements.txt`


4. Set Up Environment Variables
   
Create a .env file in the project root and add the following:


```

SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

```
5. Run Migrations

`python manage.py migrate`


6. Start the Development Server


```
python manage.py runserver
The API will be available at http://127.0.0.1:8000/api/classify-number.

```

### API Endpoint

GET `/api/classify-number`

Classifies a number and returns its properties.

Query Parameters

`number` (required): The number to classify.

Example Request

`GET /api/classify-number?number=371`

Example Response (200 OK)


```
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

```

Example Response (400 Bad Request)

```

{
    "number": "alphabet",
    "error": true
}

```

### Example Requests and Responses

Valid Input

Request:


`GET /api/classify-number?number=28`

Response:

```
{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["perfect", "even"],
    "digit_sum": 10,
    "fun_fact": "28 is the number of days in February in a common year."
}
```
Invalid Input

Request:

`GET /api/classify-number?number=abc`

Response:


```
{
    "number": "abc",
    "error": true
}
```
### Deployment

Deploy the API on [pythonanywhere.com](https://kihuni.pythonanywhere.com/api/classify-number/?number=371)
