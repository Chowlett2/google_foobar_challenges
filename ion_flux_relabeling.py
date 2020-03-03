'''Oh no! Commander Lambda's latest experiment to improve the efficiency 
of her LAMBCHOP doomsday device has backfired spectacularly. 
She had been improving the structure of the ion flux converter tree, 
but something went terribly wrong and the flux chains exploded. 
Some of the ion flux converters survived the explosion intact, 
but others had their position labels blasted off. She's having 
her henchmen rebuild the ion flux converter tree by hand, 
but you think you can do it much more quickly - quickly enough, 
perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the 
ion flux converters to form one. To label them, she performed a post-order 
traversal of the tree of converters and labeled each converter with the order 
of that converter in the traversal, starting at 1. For example, a tree of 7 
converters would look like the following:

7 3 6 1 2 4 5

Write a function answer(h, q) - where h is the height of the perfect tree of 
converters and q is a list of positive integers representing different 
flux converters - which returns a list of integers p where each element in p 
is the label of the converter that sits on top of the respective converter in 
q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) 
would return the converters above the converters at indexes 1, 4, and 7 in a 
perfect binary tree of height 3, which is [3, 6, -1].'''

def solution(h, q):
    result = []
    for i in q:
        if True:
            height = h
            num = 2**h -1
            if i == num:
                result.append(-1)
            else:
                count = 0
                place = 2**height -2
                moveL = num - (place/2) -1
                moveR = num -1
                while(i != moveR and i != moveL and count <10):
                    count += 1
                    if i > moveL:
                        num = moveR
                    else:
                        num = moveL
                    height -= 1
                    place = 2**height -2
                    moveL = num - (place/2) -1
                    moveR = num -1
                result.append(int(num))
    return result