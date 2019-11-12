a = set(range(2,21,2))
b = set(range(1,21,2))
c = set(range(-10,0,1))
num_list = list(range(0,21))
d = set(filter(lambda x:x%11!=0 or x==11, filter(lambda x:x%7!=0 or x==7, filter(lambda x:x%5!=0 or x==5, filter(lambda x:x%3!=0 or x==3, filter(lambda x:x%2!=0 or x==2, filter(lambda x:x>1, num_list)))))))
num_list2 = set(range(2,21))
e = num_list2.difference(d)

#Answer
# A ∪ B ∪ C ∪ D ∪ E
point_a = set(a|b|c|d|e)
print(point_a)

# (A ∩ B) ∪ (D ∩ E)
point_b = set((a.intersection(b))|(d.intersection(e)))
print(point_b)

# (A ∪ B) ∩ (D ∪ E)
point_c = set((a|b).intersection(d|e))
print(point_c)

# (A ∪ B) - (D ∪ E)
point_d = set((a|b).difference(d|e))
print(point_d)

# (A ∪ B ∪ C) - (A ∩ E)
point_e = set((a|b|c).difference(a.intersection(e)))
print(point_e)