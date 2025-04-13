def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def main():
    print("Welcome to the Unit Converter!")
    print("1. CM ⇄ INCHES\n2. °C ⇄ °F\n3. KG ⇄ LB")
    choice = input("Choose (1/2/3): ")

    if choice == '1':
        val = float(input("Enter value: "))
        direction = input("Convert to (cm/in): ")
        result = inches_to_cm(val) if direction == 'cm' else cm_to_inches(val)
        print(f"Result: {result:.2f}")
    elif choice == '2':
        val = float(input("Enter value: "))
        direction = input("Convert to (c/f): ")
        result = f_to_c(val) if direction == 'c' else c_to_f(val)
        print(f"Result: {result:.2f}")
    elif choice == '3':
        val = float(input("Enter value: "))
        direction = input("Convert to (kg/lb): ")
        result = lb_to_kg(val) if direction == 'kg' else kg_to_lb(val)
        print(f"Result: {result:.2f}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
