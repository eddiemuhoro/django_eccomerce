project:
  name: "Django E-Commerce API with M-Pesa Daraja Integration"
  description: >
    A Django REST API for handling e-commerce transactions, including seamless payment integration with the M-Pesa Daraja API using STK Push. 
    This project supports token generation, payment initiation, and callback processing — ideal for online stores targeting the Kenyan market.
  status: "Active"
  license: "MIT"
  author:
    name: "Your Name"
    github: "https://github.com/yourusername"
  features:
    - "Secure access token generation for M-Pesa Daraja API"
    - "STK Push payment initiation via M-Pesa"
    - "Webhook (callback) listener to process transaction responses"
    - "JSON-based API with Django REST Framework"
    - "Tested with Ngrok for local-to-live development"
  tech_stack:
    backend:
      - Django
      - Django REST Framework
    payments:
      - M-Pesa Daraja API (STK Push)
    utilities:
      - requests
      - python-decouple
    deployment:
      - Ngrok
      - Render

structure:
  ecommerce_project:
    - ecommerce/: "Django project configuration"
    - payments/:
        - views.py: "Handles payment and callback views"
        - urls.py: "URL routes for payment and callback"
        - utils.py: "Contains M-Pesa token and STK logic"
        - serializers.py: "Serializers for request/response validation"
    - .env: "Environment variables (excluded from git)"
    - requirements.txt: "Python dependency list"
    - manage.py: "Project management script"

setup:
  clone:
    - "git clone https://github.com/yourusername/django-mpesa-api.git"
    - "cd django-mpesa-api"
  virtual_environment:
    - "python -m venv env"
    - "source env/bin/activate  # For Windows: env\\Scripts\\activate"
  install_dependencies:
    - "pip install -r requirements.txt"
  environment_variables:
    note: "Create a .env file with the following"
    example:
      MPESA_ENVIRONMENT: "sandbox"
      MPESA_CONSUMER_KEY: "your_key"
      MPESA_CONSUMER_SECRET: "your_secret"
      MPESA_SHORTCODE: "174379"
      MPESA_PASSKEY: "your_passkey"
  run:
    - "python manage.py migrate"
    - "python manage.py runserver"

testing_with_ngrok:
  command: "ngrok http 8000"
  callback_url_usage: "Use the public ngrok URL in your STK Push payload: https://abc123.ngrok-free.app/callback/"

api_endpoints:
  - method: GET
    path: "/api/mpesa/token/"
    description: "Generates M-Pesa access token"
  - method: POST
    path: "/api/mpesa/pay/"
    description: "Initiates STK Push payment"
  - method: POST
    path: "/api/mpesa/callback/"
    description: "Handles transaction callback from M-Pesa"

example_request:
  endpoint: "/api/mpesa/pay/"
  method: POST
  payload:
    phone_number: "254712345678"
    amount: 100

license:
  type: "MIT"
  location: "LICENSE file"

notes:
  - "Do not commit .env files to source control."
  - "Use f-strings in Python to embed access tokens in headers (e.g., f'Bearer {access_token}')."
  - "Ensure ALLOWED_HOSTS includes your ngrok domain for local testing."

