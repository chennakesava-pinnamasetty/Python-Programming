n = int(input("Enter a number :"))

for i in range(1,n+1):
    print(f"the table {i}\n")  # Heading for each table
    for j in range(1,11):
     print(f"{i} * {j} = {i * j}")