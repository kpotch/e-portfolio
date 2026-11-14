# Baseball players starter file

def main():

    # Open an output file, players.txt (append mode)
    outfile = open("players.txt", "a")

    # Enter the player's number, name, and home runs for three additional players
    for i in range(3):
        print("Enter information for player", i + 1)

        number = int(input("Player number: "))
        name = input("Player name: ")
        hrs = int(input("Home runs: "))

        # Store each player's data in the output file
        outfile.write(f"{number: 2d} {name} {hrs: 2d}\n")

    # Close the output file
    outfile.close()

    # Reopen the file for input (printing)
    infile = open("players.txt", "r")

    # Print out the data for each player
    print("\nCurrent Players List:\n")

    for line in infile:
        print(line.strip())

    # Close the input file
    infile.close()


main()
