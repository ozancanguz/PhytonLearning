ranking = ['John', 'Sen', 'Lisa']

rank = input("Enter the rank you want to see: ")
rank = int(rank)

while True:
    match rank:
        case 1:
            print(ranking[0])
            break  # exit the loop once the correct rank has been printed
        case 2:
            print(ranking[1])
            break
        case 3:
            print(ranking[2])
            break
