# Problem: No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
array = list(map(int, input().split()))
liked = set(map(int, input().split()))
disliked = set(map(int, input().split()))

happiness = sum(1 for number in array if number in liked) - sum(1 for number in array if number in disliked)
print(happiness)
