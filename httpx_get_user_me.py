import httpx

login_payload = {
    "email": "admin@example.com",
    "password": "admin"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

access_token = login_response_data['token']['accessToken']

get_user_headers = {"Authorization": f"Bearer {access_token}"}

get_user_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=get_user_headers)

get_user_response_data = get_user_response.json()

print("Get user response:", get_user_response_data)

print("Get user status code:", get_user_response.status_code)