import sys
sys.stdin = open('input.txt')
N = int(input())
words = [input() for _ in range(N)]
words = list(set(words))
words.sort()
words.sort(key = lambda x : len(x))
for word in words:
    print(word)