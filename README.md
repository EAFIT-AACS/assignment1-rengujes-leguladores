# Equivalent States Of A DFA
This script allows the user to input all the aspects of a DFA in a .txt file. According to the transition table, the script will find the states equivalent to others, simplifying the DFA.

## Students participating in the project
- Simon Sloan Garcia Villa
- Alejandro Tirado Ramirez
  
Class number **7308**

## Details about the tools used for making the script
- The script was made using Python 3.12.9.
- The operating systems we used for the testing and programming were Windows 11 and Kali Linux (Version 2024.4).
- The tools used for the project were:
  
    - **Visual Studio** as the code editor.
    - **Git** for version control.
    - **GitHub** was used to upload the code to the cloud.
      
- The main algorithm was implemented based on lecture 14 of the book *Automata and Computability* by Kozen

- Original repository [Here](https://github.com/Alejoso/EquivalentStatesOfADFA)

## How to run the code?

First, clone the Github project on your machine. Then, if you want to modify the script's inputs, you will need to modify the .txt document. The document already contains five cases (one extra that we took from Kozen's book). After changing the document data or leaving it untouched, you can run the script the way you prefer. 

## Code explanation

    class Automata:
        def __init__(self, Σ, δ, F):
            self.Σ = list(Σ)  # Convert the alphabet into a list
            self.δ = δ  
            self.s = 0  
            self.F = set(F)  
            
We created the class Automata, where we will store the variables needed for our calculations, such as the alphabet, transition table, starting state, and final estates.

    def getEquivalentStates(self):
        states = len(self.δ) # We establish the number of states according to the transition table
        table = [[False] * states for _ in range(states)]  # Initialize the table with all False, create a nxn table

We are defining a new method called "getEquivalentStates", here is where the main program is developed. Technically we have two tables: The **transition table** and a **true or false** one. This true or false table is for mapping which transitions are marked as not equivalent.  
        
        change = False # Initialize the change variable to False
        # Mark the pairs {p, q} if p is final and q is not, or vice versa
        for i in range(states):  
            for j in range(states):
                if (i in self.F) != (j in self.F):
                    table[i][j] = True 
                    change = True # We iterate over the transition table and mark the pairs that one of them is a final state and the other is not
                    
We do the first step of the algorithm, which is setting up the first true pairs according to whether one of the pairs is a final state and the other is not. 

        while(change): # While there is a change in the table
            change = False # Set the change variable to False so we can know if there are further changes in the table
            for i in range(1 , states): # Iterate from one to the number of states, because the first row will always be false
                for j in range(states):
                    if i > j and not table[i][j]: # We only need to check for false values and for the lower triangle of the table
                        for lexema in range(len(self.Σ)): # Iterate through 1 and 2
                            p = self.δ[j][lexema + 1] # Get the next state for the lexeme, being p the initial state we are looking to
                            q = self.δ[i][lexema + 1] # Get the next state for the lexeme, being q the final state we are looking to
                            if p != q and table[q][p] == True: # If the states are different and the position we are looking to is marked as True
                               table[i][j] = True # Mark the state as a nonequivalent state
                               change = True # Put it as True to continue the loop 

Then, we check if there have been changes in the table. This step is important, because the moment we don't make any progress identifying true pairs, we have finished the iterations. Then, we iterate through our true or false matrix, only checking the lower triangle (because all other values will always be false no matter what). After that, for every accepted value of i and j, we get the next state of our original state using the transition table's position. Lastly, we check if they are not the same state and if the position they landed on our **true or false** matrix is equal to true. That means we found another pair that is not equivalent, we mark that spot as true and set changes to true for doing another iteration when this one finishes. 
                             
          
        # Identify equivalent states
        equivalentPairs = []
        for i in range(states):
            for j in range(i):
                if not table[i][j]:  # if isn't mark, is a equivalent state 
                    equivalentPairs.append((j,i))  #Add it to equivalent states array
                    
        return equivalentPairs

When the iteration finishes, spaces marked as false on our **true or false** matrix will be the equivalent states of our Automata.

    # Read the file and give it the alias "file"
    with open("example.txt", "r") as file:
        lines = file.readlines()
        
Reads the .txt file with .readlines() method

    # Extract number of automata
    NumberOfAutomata = int(lines[0].strip())
    i = 1
    cases = []
    
    # Procces every automata in the .txt
    for _ in range(NumberOfAutomata):
        nLines = int(lines[i].strip())  #Get the numbre of states, then convert it into an int 
        Σ = lines[i+1].strip().split(" ")  # Get the alphabet, taking into account split for not getting empty spaces 
        F = list(map(int, lines[i+2].strip().split(" ")))  # Get final states 

    #Read the transition table
    δ = [list(map(int, lines[i+3+j].strip().split(" "))) for j in range(nLines)] #Convert the transition table data into an integer to create a matrix
    
    # Save the automata in the automata list
    cases.append(Automata(Σ, δ, F))

    # Increase the counter
    i = nLines + 3 + I

Extracts all the information from the .txt file according to the structure proposed in the document

    for idx, automata in enumerate(cases): #Print the equivalent states
        equivalentes = automata.getEquivalentStates()
        print(" ".join(f"({p},{q})" for p, q in equivalentes))

Prints the equivalent states of the DFA 
