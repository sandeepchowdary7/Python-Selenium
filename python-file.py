# import os
#
# # To create a file
# f = open("test.txt", "w")
# # f.write("\nNow the file has more content!")
# f.write("Woops. I have overwritten the content!")
# f.close()

# To Delete a file
# os.remove("test.txt")

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(2)
