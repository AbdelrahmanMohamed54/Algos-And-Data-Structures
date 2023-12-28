#import shortest_path_algorithm
from shortest_path import shortest_path_search

# EXERCISE 7.2

start = (0, 0, 0)

def is_goal(state):
    return state == (3, 3, 1)


def successors(M, C, B):
    def sc(state):
        m,c,b = state

        if m < c and m > 0:
            return {}
        if M - m < C - c and M - m > 0:
            return {}

        if b == 1:
            return {(m, c-1, 0): 'c<-',
                    (m, c-2, 0): 'cc<-',
                    (m-1, c-1, 0): 'mc<-',
                    (m-1, c, 0): 'm<-',
                    (m-2, c, 0): 'mm<-'}
        
        else:
            return {(m, c+1, 1): '->c',
                    (m, c+2, 1): '->cc',
                    (m+1, c+1, 1): '->mc',
                    (m+1, c, 1): '->m',
                    (m+2, c, 1): '->mm'}

    return sc

res = shortest_path_search(start, successors(3, 3, 1), is_goal)
print(res)

print(len(res) // 2)
