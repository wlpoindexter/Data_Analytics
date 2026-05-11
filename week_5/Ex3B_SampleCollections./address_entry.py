contact_info = {
    "name":    "Will Poindexter",
    "address": "4821 Maple Street",
    "city":    "Chicago",
    "state":   "IL",
    "zip":     "60614" }

print(f"""{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

del contact_info["name"]

full_name = {
    "first name": "Will",
    "last name":  "Poindexter"}
full_name.update({"honorific": "Mr."})
contact_info.update({"full_name": full_name})

print(f"""{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")