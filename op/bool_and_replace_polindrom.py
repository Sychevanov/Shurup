# a=18
# b=24
# print (a%b)

# s = input("Enter string: ")
# ch = input("Enter symbol: ")
# n=len(s)
# found = False
# print(n)
# for i in range(len(s)):
#     if s[i] == ch:
#         print("Yes")
#         found = True
#         break

# if not found:
#     print("No")


s = input("Enter string: ").replace(" ", "")
print("Palindrom" if s == s[::-1] else "Not palindrom")
