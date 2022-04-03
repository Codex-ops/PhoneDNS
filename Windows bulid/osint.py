try:
    from googlesearch import search
except ImportError:
    print("No Module named 'google' found")

query = input("Would you like to dork: ")

if query == 'yes':
    input("Please enter website: ")
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)
elif query == 'no':
    print("Goodbye")
    exit()   
else:
    input()
    exit()    