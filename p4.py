name='harika chowdary'
vowel='aeiou'
r=[char for char in name if char in vowel]
print(r)
r=[char for char in name if char not in vowel]
print(r)
print(name[::3])
print(name[::-3])

