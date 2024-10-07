with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    new_data = data.replace("Java","Python")
    print(new_data)
f.close()