from queue import Queue

def first_non_repeating_character(s):
    frequency = [0] * 256
    
    queue = Queue()
    for i in range(len(s)):
        frequency[ord(s[i])] += 1
        if frequency[ord(s[i])] == 1:
            queue.put((s[i], i))    
    while not queue.empty():
        c, i = queue.get()
        if frequency[ord(c)] == 1:
            return i   
    return -1

print(first_non_repeating_character("aabbc"))