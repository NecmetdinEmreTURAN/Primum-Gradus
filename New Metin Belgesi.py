import math
seed= 541
length_of_the_simulation= 0.5 # in terms of hours
max_people_capacity= 250
day_start =10*60
day_end= 10*60 + length_of_the_simulation*60
lambda_for_interarrival= 8     #exponential with a mean of 8 minutes
# This function will firstly put our seed into the LCG than will give us the Random Number according to this LCG
def LCG_RN_generator():
    global seed
    a=29
    c=3
    m=1289
    RN = ((a*seed +c)%m)/m
    seed= (a*seed +c)%m
    return RN

# This function creates a exponential RV with a mean  of 8 from our previously created RN
def exponential8_from_RN(RN):
    E8 = -8 * math.log(RN)
    return E8


# Now we need to create a ticket amount in order to see how the simulation behaves/We use the CDF to use our U[0,1] distributed RN's
def ticket_amount(RN):
    if RN < 0.3:
        return 1
    elif RN < 0.7:
        return 2
    elif RN <0.9:
        return 3
    else:
        return 4
    print(seed)

print(seed)
a=LCG_RN_generator()
print(a)
print(seed)
a=LCG_RN_generator()
print(seed)
print(a)




    



