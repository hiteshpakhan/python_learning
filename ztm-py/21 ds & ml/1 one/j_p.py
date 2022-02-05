import pandas
data_collection = pandas.read_csv("data.csv")
# print(data_collection.head(2))   #head only print the first rows in the given numbers
# print(data_collection.shape)       #output:- (18207, 89)
# print(data_collection["Age"].head(10))   #it will print only data realted to the age
# print(data_collection[data_collection["Nationality"] == "India"])

new_data = pandas.DataFrame(data_collection, columns=["Name","Wage","Value"])   #you can choose multiple columns
# print(new_data)

