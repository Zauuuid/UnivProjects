# Question 2 of TM112 MTA :
# I am asked to answer the first and second sections of question two.


# I will open a file with my name and the format will be a text file (.txt). I will use 'w' to write in it
file = open("ZayedAbdullahBawzeer.txt", "w")

# The first thing the file contains is my identity as a student
file.write("This file was created by student: Zayed Abdullah Bawazeer\n\n")

# I added spaces between the code for better readability and easier modification.


# These lines will contain the requirements for the first part of the question
# I will add at least 3 animals for each type: mammals, birds, and reptiles, and specify their status as Halal or Haram.
# The mammals section.
file.write("Ox,Mammal,Halal\n")
file.write("Panther,Mammal,Not Halal\n")
file.write("Ram,Mammal,Halal\n")
file.write("Monkey,Mammal,Not Halal\n")
file.write("Camel,Mammal,Halal\n")
file.write("Deer,Mammal,Halal\n")

# The Birds section.
file.write("Parrot,Bird,Halal\n")
file.write("Falcon,Bird,Not Halal\n")
file.write("Nightingale,Bird,Halal\n")
file.write("Dove,Bird,Halal\n")
file.write("Sparrow,Bird,Halal\n")
file.write("Crow,Bird,Not Halal\n")

# The Reptiles section.
file.write("Tortoise,Reptile,Not Halal\n")
file.write("Lizard,Reptile,Not Halal\n")
file.write("Chameleon,Reptile,Not Halal\n")
file.write("Crocodile,Reptile,Not Halal\n")
file.write("Snake,Reptile,Not Halal\n")
file.write("Dhab,Reptile,Halal\n")   
# حديث ابن عمر -رضي الله عنهما- عن النبيّ -صلّى الله عليه وسلّم-: (الضَّبُّ لَسْتُ آكُلُهُ ولا أُحَرِّمُهُ).[٣]
# لا اعرف هل فعلا الضب حلال ام حرام , انا لا أكله لاكن احضرت الحديث هذا الي ينفي " تحريمه " فقط


# End of the first part of question two, moving on to the second part.
file.close()

# Beginning of the second part of question two: processing, printing, and reading.
# Opening the file in read mode to process its contentس
file2 = open("ZayedAbdullahBawzeer.txt", "r")

# Setting the variables to 0 to initialize and fix their values
halal = 0
nothalal = 0

# This will print the header for the animal classification report, indicating the start of the output.
print("Animal Classification Report:\n")
print("[" , "_" * 25, "]")

# Now, we start looping through each line in the file for further analysis and extraction of data.
for line in file2:
    # Checking if the line contains data in the correct format (i.e., it has a comma separating values).
    if line.find(",") != -1:
        # Stripping any extra spaces from the line to ensure clean and consistent data handling.
        line = line.strip()
        
        # Splitting the line into its individual components: the animal name, category, and halal status.
        values = line.split(",")

        # Verifying that the line contains exactly three parts: animal name, category, and halal status.
        if len(values) == 3:
            animal = values[0]  # Storing the animal's name.
            typee = values[1]   # Storing the category (Mammal, Bird, Reptile, etc.).
            status = values[2]  # Storing the halal status (Halal / Not Halal).

            # Displaying the information for the current animal to provide a clean and structured output.
            print("Animal: " + animal)
            print("Category: " + typee)
            print("Halal Status: " + status)
            print("[" , "_" * 25, "]")

            # Depending on the halal status, incrementing the corresponding counter for halal or non-halal animals.
            if status == "Halal":
                halal += 1  # Incrementing the halal count.
            else:
                nothalal += 1  # Incrementing the non-halal count.

# After processing all the lines, we close the file to free up resources and avoid any issues.
file2.close()

# Finally, displaying a summary of the counts for halal and non-halal animals processed from the file.
print("\nSummary:")
print("Total Halal Animals: " + str(halal))  # Showing the total number of halal animals.
print("Total Non-Halal Animals: " + str(nothalal))  # Showing the total number of non-halal animals.
