def guest_list(people):
    count = 0
    if count < 3:
    # Iterate over each "person" in the given "people" list of tuples. 
        for person in people:

        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"   
            name, age, profession = person  

        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
            print("{} is {} years old and works as {}".format(name, age, profession))


# Call to the function:
guest_list([('Ken', 30, 'Chef'), ('Raj', 35, 'Lawyer'), ('Maria', 25, 'Engineer')])

# Click Run to submit code

# Output should match:
# Ken is 30 years old and works as a Chef
# Pat is 35 years old and works as a Lawyer
# Amanda is 25 years old and works as an Engineer
