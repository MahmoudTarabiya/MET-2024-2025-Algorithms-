


# ===============================
# محمود احمد الديسطى محمود
# سكشن 1
# ===============================

def select_sort(A):

    for i in range(len(A)):
        MIN = i

        for j in range(i+1, len(A)):
            if A[j] < A[MIN]:
                MIN = j

        A[i], A[MIN] = A[MIN], A[i]

        print(f"{A}")

    return A

A = [69, 205, 102, 22 , 44 , 79 , 91]
print(A)
sorted_A = select_sort(A)
print(sorted_A)