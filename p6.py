values=[2,3,1,-3,-5,7]
negative_value=max(i for i in values if i<0)
positive_value=max(j for j in values if j%2 == 0)
print(negative_value)
print(positive_value)
