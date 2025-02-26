class Automata:
    def __init__(self, Σ, δ, F):
        self.Σ = list(Σ)  # Convert the alphabet into a list
        self.δ = δ  
        self.s = 0  
        self.F = set(F)  


    def getEquivalentStates(self):
        states = len(self.δ) # We stablish the number of states according to the transition table
        table = [[False] * states for _ in range(states)]  # Initialize the table with all False, create a nxn table
        
        change = False # Initialize the change variable to False
        # Mark the pairs {p, q} if p is final and q is not, or vice versa
        for i in range(states):  
            for j in range(states):
                if (i in self.F) != (j in self.F):
                    table[i][j] = True 
                    change = True # We itarate over the transition table and mark the pairs that one of them is a final state and the other is not

        while(change): # While there is a change in the table
            change = False # Set the change variable to False so we can know if there are further changes in the table
            for i in range(1 , states): # Iterate from one to the number of states, because the first row will always be false
                for j in range(states):
                    if i > j and not table[i][j]: # We only need to check for false values and for the lower triangle of the table
                        for lexema in range(len(self.Σ)): # Iterate trougth 1 and 2
                            p = self.δ[j][lexema + 1] # Get the next state for the lexema, being p the initial state we are looking to
                            q = self.δ[i][lexema + 1] # Get the next state for the lexema, being q the final state we are looking to
                            if p != q and table[q][p] == True: # If the states are different and the position we are looking to is marked as True
                               table[i][j] = True # Mark the state as a nonequivalent state
                               change = True # Put it as True to continue the loop 
                             
          
        # Identify equivalent states
        equivalentPairs = []
        for i in range(states):
            for j in range(i):
                if not table[i][j]:  # if isn't mark, is a equivalent state 
                    equivalentPairs.append((j,i))  #Add it to equivalent states array

        return equivalentPairs

# Read the file and give it the alias "file"
with open("example.txt", "r") as file:
    lines = file.readlines()

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
    i = nLines + 3 + i
    
for idx, automata in enumerate(cases): #Print the equivalent states
    equivalentes = automata.getEquivalentStates()
    print( " ".join(f"({p},{q})" for p, q in equivalentes))