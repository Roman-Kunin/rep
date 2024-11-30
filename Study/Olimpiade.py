start_point = int(input())
end_point = int(input())
minutes = 0
while start_point < end_point:
    end_point -= 3
    minutes += 1
print(minutes)
