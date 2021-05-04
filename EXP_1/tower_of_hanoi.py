def TowerOfHanoi(n , source_rod, dest_rod, aux_rod):
    # Condition to check for disk 1
    if n == 1:
        print("Move disk 1 from rod",source_rod,"to rod",dest_rod)
        return
    # source , dest, aux
    TowerOfHanoi(n-1, source_rod, aux_rod, dest_rod) # souce to aux
    print("Move disk",n,"from rod",source_rod,"to rod",dest_rod)
    TowerOfHanoi(n-1, aux_rod, dest_rod, source_rod) # aux to dest
         
n = int(input("Enter no of disks:     ")) #4
TowerOfHanoi(n, 'A', 'C', 'B')  #3 rods




# Algorithm ---------------------------------------------------------------------------------------

# START
# Function Hanoi(disk, source, dest, aux)

#    if disk == 1, THEN
#       move disk from source to destination rod          
#    else
#       Hanoi(disk - 1, source, aux, dest)     # Step 1  #Repeat the same for the the other rod
#       move disk from source to dest          # Step 2 
#       Hanoi(disk - 1, aux, dest, source)     # Step 3
   
# END Function
# STOP