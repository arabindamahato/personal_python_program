class Movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    def display(self):
        print('The title name is :', self.title)
        print('The Hero name is :', self.hero)
        print('The Heroine name is :', self.heroine)

list_of_movies = []             #Empty list where movies are been added
while True:
    title = input('Enter Title Name :') #Take user input for title name
    hero = input('Enter Hero Name :')   #Take user input for hero name
    heroine = input('Enter Heroine Name :') #Take user input  for heroine name

    m = Movie(title, hero, heroine) # Create object
    list_of_movies.append(m)        # Add movie
    print('Movie added successfully')
    option = input('Do you want to add one more movie [Yes|No] : ')
    if option == 'no':
        break
print('Movies Information.\n--------------------------')
for m in list_of_movies:
    m.display()                     # call the display function
    print()





