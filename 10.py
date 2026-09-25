## Convert seconds into hours, minutes and seconds ##


input1 = int(input("Enter seconds which you want to convert into hours and minutes: "))

hours = input1 // 3600
remaining_seconds = input1 % 3600
minutes = remaining_seconds // 60

print("Hours:", hours)
print("Minutes:", minutes)
