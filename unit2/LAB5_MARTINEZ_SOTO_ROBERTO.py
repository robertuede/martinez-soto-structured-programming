selection=""
#functions
def show_menu():
    print("-----CUEVANA-----\nSelect a genre: \n1.-Horror\n2.-Thriller\n3.-Action\n4.-Comedy")
def get_genre():
    selection=input("Please select an option: ")
    return selection.lower()
def recommend_content(selection):
    if selection == "1" or selection == "horror":
      print("- Midsommar \n- Incantation \n- Skinamarink")
      return True
    elif selection == "2" or selection == "thriller":
      print("- Incendies \n- Seven\n- Mulholland Drive")
      return True
    elif selection == "3" or selection == "action":
      print("- Tenet\n- Northman\n- Inception")
      return True
    elif selection == "4" or selection == "comedy":
      print("- Poor Things\n- Wolf of Wall Street\n- Dont look up")
      return True
    else:
      print("Invalid option ")
      return False
def rate_content():
    rate=input("Would you like to rate some content? ")
    if rate=="yes":
      movie=input("Choose the movie you want to rate ")
      rated=input("Score the movie from 1 to 5 ")
      print(f"You gave {movie} a {rated} ")
    else:
      print("Content not rated ")
# Main program
repeat="yes"
while repeat == "yes":
    while True:
        show_menu()
        selection = get_genre()
        if recommend_content(selection):
            break
    rate_content()
    repeat=input("Would you like to repeat your recomendations? (yes/no) ").lower()
print("Thank you for using ")
