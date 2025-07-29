print("welcome to fruit checker")
favorite_fruits = ["apple", "banna", "mango", "grapes"]
fruit = input("Enter a fruit name: ").lower()
if fruit in favorite_fruits:
    print("Yay! That's one of my favorite fruits too!")
else:
    print("hmm...thats not on my favourites list")