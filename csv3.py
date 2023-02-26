#read n write csv into dictionaries
cat software.csv
name,version,status,users
MailTree,5.34,production,324
CatDoor,1.25.2,beta,22
ChattyChicken,0.34,alpha,4

with open('software.csv') as software:
  reader = csv.DictReader(software)
  for row in reader:
    print("{} has {} users".format(row["name"], row["users"]))
# each element in the list will be a row in the file, and the values of each field will come out of each of the dictionaries.
