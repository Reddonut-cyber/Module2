num_of_index = int(input())
list_of_number = list(map(int, input().split()))

for i in range(num_of_index - 1):
    if list_of_number[i] * list_of_number[i + 1 ] > 0:
        print("YES")
        break
else:
    print("NO")