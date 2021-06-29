import requests
result = requests.get("http://hrms.tforcehrms.com/admin/api/clockInOutState")

# # Let assume our employee_id is '532'
employee_id = "532"

# data = result.json()
# container = []
# for i in data:
#   # print(i)
#   if (i['employee_id'] == employee_id):
#     container.append(i)

# last_elem = container[-1]

# current_clock_status = ""
# if (last_elem['clock_in']!= None and last_elem['clock_out']!= None):
#   current_clock_status = 'clock_out'
# else:
#   current_clock_status = 'clock_in'

# print(current_clock_status)

#=========================================



print(result.json())

post_url = "http://hrms.tforcehrms.com/admin/api/clockInOut"
post_data = {
    "user_id": employee_id, # employee_id must be in string format (not integer)
    "clock_state":"clock_in", # reverse of the previous state
    "latitude":"1",
    "longitude":"1",
    "ip_address":"1"
}

result = requests.post(url = post_url, data = post_data)

