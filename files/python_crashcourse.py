print("Hello Python Interpreter!")


#Chapter 2
message="Hello Python world!"
print(message)


#adding witespace to strings with tabs or new lines

print("Python")
print("\tPython") #tabbed the word

print("Python by letters: \nP\ny\nt\nh\no\nn")#created each letter on a new line

print("Languages:\n\tPython\n\tC\n\tJavaScript")#this tabbed each new line



#getting rid of whitespace at the right end of a string
favorite_language='python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language=favorite_language.rstrip#this saves the removed whitespace version as the correct version

#strip left side and both sides
favorite_languages=" python "
print(favorite_languages.rstrip())
print(favorite_languages.lstrip())#left strip
print(favorite_languages.strip())#strip both sides at once


##Chapter 2 try it yourself 2-3.
first_name= "eric"
last_name= "smith"
message=f"Hello {first_name.title()}, would you like to learn some Python today?"
print(message)


##Chapter 2 try it yourself 2-4.
full_name=f"{first_name} {last_name}"
print(full_name.title())
print(full_name.upper())
print(full_name.lower())