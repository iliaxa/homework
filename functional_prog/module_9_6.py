# def all_variants(text):
#     length = len(text)
#     for start in range(length):
#         for end in range(start + 1, length + 1):
#             yield text[start:end]

def all_variants(text):
    length = len(text)
    for end in range(1, length + 1):  
        for start in range(length - end + 1):
            yield text[start:start + end]

a = all_variants("abc")
for i in a:
    print(i)
print("abc")
