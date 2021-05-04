#choosing an item from the remaining items that has the maximum value to weight ratio
def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))  # index for looping 
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_value = 0
    fractions = [0]*len(value)  # array of 0s  == length of the value (no of values entered ie n)
    for i in index:
        if weight[i] <= capacity: # check if weight less than cap if yes, 1 fraction is added
            fractions[i] = 1
            max_value += value[i] # addd to max value which can be carried
            capacity -= weight[i] # reduce the capacity
        else:
            fractions[i] = capacity/weight[i]    # if we need to add in fractions
            max_value += value[i]*capacity/weight[i]  # add the fraction to the max_value
            break
 
    return max_value, fractions 
    #  max_value =>  maximum value of items with total weight not more than capacity
    #  fractions =>  fractions in which the items has to be carried
 
 
n = int(input('Number of items: '))

value = input('Enter the values of the ' + str(n) + ' item(s) in order: ').split()

weight = input('Enter the positive weights of the ' + str(n) + ' item(s) in order: ').split()

capacity = int(input('Enter maximum weight that can be carried: '))

value = [int(v) for v in value]
weight = [int(w) for w in weight]

 
max_value, fractions = fractional_knapsack(value, weight, capacity)


print('The maximum value of items that can be carried:', max_value)
print('The fractions in which the items should be taken:', fractions)



# 60 100 120
# weights: 10 20 30
# maxweight : 50 
# maxvalue : 240