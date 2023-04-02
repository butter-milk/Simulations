from random import randint

def Seats(seats:int, tries:int) -> None:
    #Prints ratio of successes.
    success = 0
    for _ in range(tries):
        taken = [randint(0,seats)]
        for person in range(1,seats-1):
            if person in taken:
                taken.append(([x for x in range(seats) if x not in taken])[randint(0,seats-person-1)])
            else:
                taken.append(person)
        if seats-1 not in taken:
            success+=1
    print(str(float(success)/float(tries)) + " success percentage."  )


    return
Seats(100,10**4)
