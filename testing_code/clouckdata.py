import requests
import json
post_url = "http://hrms.tforcehrms.com/admin/api/clockInOut"
employee_id = "571"
post_data = {
    "user_id": employee_id,
    "clock_state":"clock_out",
    "latitude":"1",
    "longitude":"1",
    "ip_address":"127.0.0.1"
}
response = requests.post(post_url, data = json.dumps(post_data))
print(response.json())