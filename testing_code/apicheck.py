import requests
result = requests.get("http://hrms.tforcehrms.com/admin/api/clockInOutState")

## Let assume our employee_id is '532'
# employee_id = "546"
employee_id = "571"

data = result.json()

# # # print(data)

container = []
for i in data:
  # print(i)
  if (i['employee_id'] == employee_id):
    container.append(i)

last_elem = container[-1]

current_clock_status = ""
if (last_elem['clock_in'] != "" and last_elem['clock_out']!= ""):
  current_clock_status = 'clock_out'
else:
  current_clock_status = 'clock_in'

print(current_clock_status)