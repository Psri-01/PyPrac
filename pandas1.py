import pandas
visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45, 33, 44, 76]
df = pandas.DataFrame({"visitors": visitors, "errors": errors}, index=["Mon", "Tue", "Wed", "Thu", "Fri"])
print(df)
