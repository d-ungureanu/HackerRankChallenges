n = int(input())
english_students = set(map(int, input().split()))

b= int(input())
french_students = set(map(int, input().split()))

print(len(english_students.union(french_students)))