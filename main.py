import os

for i in range(1, 300):
    f = os.path.splitext(f"script_{i}")[0]+".py"
    new_name = os.rename(f"D:\Projects\Freelance_Projects\scrap_exist\scripts\script_{i}", f)
    print(new_name)