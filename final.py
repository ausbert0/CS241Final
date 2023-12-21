def withinSet(triplet, search):
    '''
        triplet (tuple of size 3): The triplet that we're searching for
        search (set): The set we're searching in to see if a triplet is in it

        Used to check if a set contains a pythagorean triple 
    '''
    return (triplet[0] in search) and (triplet[1] in search) and (triplet[2] in search)

def moveBetweenSets(map, triplet, allTriples, x, y, z):
    '''
        map (dictionary: key = number part of triplet, value = set it is in)
        triplet (tuple of size 3): self-explanatory
        allTriples (list of size 3 tuples): list of every single triplet
        x, y, z (sets): the "colors" in the pythagorean triple problem

        Used to attempt add values from one set to the others that they
        did not start in. This only goes one set at a time. (example: if a value 
        started in x, we will try to move it to y and if that doesn't work we try moving 
        it to z. If both fail, we put it back in x where it started)
    '''
    within = False
    for i in triplet:
        if map[i] == x:
            x.remove(i)
            # case of swapping to y
            y.add(i)
            for j in allTriples:
                if withinSet(j, y):
                    within = True
                    break
            if not within:
                map[i] = y # updates the map with the new location for i
                return True
            y.remove(i) # if it doesn't work, remove it from y
            # case of swapping to z
            z.add(i)
            for j in allTriples:
                if withinSet(j, z):
                    within = True
                    break
            if not within:
                map[i] = z # updates the map with the new location for i
                return True
            z.remove(i) # if it doesn't work, remove it from z
            x.add(i) # adds back the original element to its original list if moving it to the others doesn't fix the problem

        elif map[i] == y:
            y.remove(i)
            # case of swapping to x
            x.add(i)
            for j in allTriples:
                if withinSet(j, x):
                    within = True
                    break
            if not within:
                map[i] = x # updates the map with the new location for i
                return True
            x.remove(i) # if it doesn't work, remove it from x
            # case of swapping to z
            z.add(i)
            for j in allTriples:
                if withinSet(j, z):
                    within = True
                    break
            if not within:
                map[i] = z # updates the map with the new location for i
                return True
            z.remove(i)
            y.add(i) # adds back the original element to its original list if moving it to the others doesn't fix the problem
        else:
            z.remove(i)
            # case of swapping to x
            x.add(i)
            for j in allTriples:
                if withinSet(j, x):
                    within = True
                    break
            if not within:
                map[i] = x # updates the map with the new location for i
                return True
            x.remove(i) # if it doesn't work, remove it from x
            # case of swapping to y
            y.add(i)
            for j in allTriples:
                if withinSet(j, y):
                    within = True
                    break
            if not within:
                map[i] = y # updates the map with the new location for i
                return True
            y.remove(i) # if it doesn't work, remove it from y
            z.add(i) # adds back the original element to its original list if moving it to the others doesn't fix the problem
    return False

# beginning of "main"
allTriples = [] # stores EVERY pythagorean triple encountered

x = set()
x.add(1) # we add 1 and 2 because they're not in a pythagorean triple
x.add(2)

y = set()

z = set()

whereValueIs = {}
whereValueIs[1] = x # Value 1 is stored in set x
whereValueIs[2] = x

setNumber = 1
stop = False
N = 1000 # test case, this is what should be adjusted for testing purposes, start with 100 since it's fast then move up to 1k, then the 7825
for a in range(2, N):
    for b in range(2, N):
        for c in range(2, N):
            if a**2 + b**2 == c**2:
                triplet = (a, b, c)
                allTriples.append(triplet)
                print(setNumber, ") ", triplet)
                setNumber += 1
                if a not in x:
                    if a not in y:
                        if a not in z:
                            x.add(a)
                            whereValueIs[a] = x
                if b not in x:
                    if b not in y:
                        if b not in z:
                            y.add(b)
                            whereValueIs[b] = y
                if c not in x:
                    if c not in y:
                        if c not in z:
                            z.add(c)
                            whereValueIs[c] = z
                for i in allTriples:
                    if withinSet(i, x) or withinSet(i, y) or withinSet(i, z):
                        stop = True
                        break                       
                if stop:
                    for tr in reversed(allTriples):
                        if moveBetweenSets(whereValueIs, tr, allTriples, x, y, z):
                            stop = False
                            break
        if stop:
            break
    if stop:
        print("can't fix repeated triple: ", allTriples[-1]) 
        break
print(x.intersection(y)) # these three intersection lines are also error checking, they should all print empty sets because there should be no shared values between sets
print(y.intersection(z))
print(x.intersection(z))
for i in allTriples: # this is for error checking, it ideally should only print one "oops" if it fails and no "oops" if you did it right
    if withinSet(i, x) or withinSet(i, y) or withinSet(i, z):
        print("oops")