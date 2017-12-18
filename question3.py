'''Q3. Define a function that takes in a list arbitary_list = [1, 2, 4, 4, 3, 5, 6].
 Inside the function each element of the list is extracted and is cubed.
  Finally, The squared value is then appened to another list and is returned.'''


def list_square(l):
    new_list=[]
    for each in l:
        each=each**3
        new_list.append(each)
    return new_list
print(list_square([1,2,3,4,5,6]))
