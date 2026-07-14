
#3
def calculate_tax(*salaries):
    try:
        taxes = list(map(lambda sal: sal * 0.10, salaries))
        total_tax = sum(taxes)
        return total_tax
    
    except TypeError:
        print("Error")

    except Exception as e:
        print("An error occurred:", e)

result = calculate_tax(25000, 30000, 28000, 35000)
print("Total Tax:", result)