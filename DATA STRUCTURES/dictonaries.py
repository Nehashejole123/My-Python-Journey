kirana = {1:"neha", 2:"Kunal", 3:"Anjali"}
print(kirana)

kirana[1] = "aditi"
print(kirana)

kirana[4] = True
print(kirana)


a = [1,2, 2, 3]
# b = a
# b[1] = 5

# print(b)
# print(a)

c = a.copy()
c[2] = "kunal"
print(a)
print(c)