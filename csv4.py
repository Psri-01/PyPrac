users = [{"name":"Sol Mansi", "username": "solm", "department: "IT infra"},
{"name":"Leo Nelson", "username": "leon", "department: "User exp research"},
{"name":"Charl Grey", "username": "greyc", "department: "Web development"}]
keys = ["name", "username", "department"]
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames = keys)
    writer.writeheader()
    writer.writerows(users)

cat by_department.csv
