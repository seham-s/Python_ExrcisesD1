# Create the dictionary
person = {"name": "Ahmad", "age": 25, "occupation": "doctor", "country": "Jordan"}
# Add a new key-value pair with "city": "Amman"
person["city"] = "Amman"
print(person)
# Update the occupation to "Surgeon"
person["occupation"] = "Surgeon"
print(person)
# Remove the "country" key-value pair from the dictionary
del person["country"]
# Print out the updated dictionary
print(person)