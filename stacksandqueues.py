#list - time complexity
#search through list O(n) =LINEAR [12,3,59,4,19].index(4)
#index into the list O(1) = CONSTANT [3,6,9,10][3]
#copy list O(n) - LINEAR [1,3,9][:] - need to go thru all #s
#adding to list O(1)
[1,2,3].append(4)
#removing from end O(1)
[1,2,3].pop()
#removing from specific postiion O(n)
##[1,2,3,4,5,6,7].pop(2) = LINEAR

#stack - last in first out (Ex. can of pringles, last in is top of can)
stack = []
stack.append(1) #append is one operation making ALL O(1)
stack.append(2)
stack.append(3)
#implement stack we .pop() --> popping last element
stack.pop()

#queue - is the opposite, first in first out or FIFO (Ex:line in carnival)
queues = []
queues.append(1) #O(1)
queues.append(2) #O(1)
queues.append(3) #O(1)

#remove first
queues.pop(0) #O(n)

queues2 = []
queues2.append(0,1) #O(n)
queues2.append(0,2) #O(n)
queues2.append(0,3) #O(n)

#remove first
#queues2.pop(-1 or empty) #O(1)

#waiting list for restaurant
#task scheduling queue
#message processing, queue of messages, first one shown


