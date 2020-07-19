# Dictionary from flowers.txt
def create_flowerdict(filename):
    dictionary = {}
    with open(filename, 'r') as fl:
        print("Contents of file :\n")
        for line in fl:
            print(line)
            # A : African Daisy
            #line.strip().split(":") => Line content split ":" -> ['A','African Daisy]
            dictionary[line.strip().split(":")[0]] = line.strip().split(":")[1]
        print(40*'-')
        print("Alphabets:Flower_Name dictionary:",dictionary)
    return dictionary


# Function to ask for user's first and last name
def main():
    dic = create_flowerdict('flowers.txt')
    first_last_name = input("Enter your First [space] Last name only: ").title()
    first_letter = first_last_name.split()[0][0] # Brad Pitt -> .split()[0] ->Brad -> split()[0][0]-> B
    if first_letter in dic.keys():
        print("Unique flower name with the first letter:{}".format(dic[first_letter]))


main()

# print the desired output
