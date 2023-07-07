import os
root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

print(root_dir)
print(parent_dir)