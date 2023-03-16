name = "Bro Code"
first_name = name[:3]
last_name = name[4:]
full_name = name[::]
reverse_name = name[::-1]
print(first_name)  # Bro
print(last_name)  # Code
print(full_name)  # Bro Code
print(reverse_name)  # edoC orB

website_1 = "http://google.com"
website_2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website_1[slice]) # google
print(website_2[slice]) # wikipedia
