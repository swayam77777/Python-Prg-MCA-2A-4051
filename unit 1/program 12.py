x = 10

def outer_function():
    y = 20

    def inner_function():
        nonlocal y
        global x

        z = 30

        x = x + 5   # modifies global x
        y = y + 5   # modifies nonlocal y
        z = z + 5   # modifies local z

        print("Inside inner function:")
        print("global variable x:", x)
        print("nonlocal variable y:", y)
        print("local variable z:", z)

    inner_function()

    print("\nInside outer function:")
    print("Nonlocal variable y:", y)

outer_function()

print("\nOutside all function:")
print("Global variable x:", x)
