thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset.discard("apple")
print(thisset)

x = thisset.pop()
print(f"آیتم حذف شده: {x}")
print(f"مجموعه باقی‌مانده: {thisset}")