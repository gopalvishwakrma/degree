import matplotlib.pyplot as plt

def TakingInput():
    try:
        user_input = input("Enter a complex number (in the format a+bj or a-bj): ")
        complex_number = complex(user_input)
        print("You entered:", complex_number)
        
        print("Enter how many degrees you want to rotate or where you want to place your complex number input in a graph")
        print("1: 90\n2: 180\n3: 270")
        degree = int(input("Enter degree no.: "))
        
        z = 1j
        if degree == 1:
            print("z value based on degree: 1 and your entered complex number:", user_input)
            x_90 = complex_number *  1j
            plt.scatter(x_90.real, x_90.imag, label="90 degrees")
        elif degree == 3:
            print("z value based on degree: -1j and your entered complex number:", user_input)
            x_270 = complex_number * z** -1j
            plt.scatter(x_270.real, x_270.imag, label="270 degrees")
        else:
            print("z value based on degree: 1j and your entered complex number:", user_input)
            x_180 = complex_number * z** -1j
            plt.scatter(x_180.real, x_180.imag, label="180 degrees")

        plt.legend()
        plt.xlabel("Real Part")
        plt.ylabel("Imaginary Part")
        plt.title("Complex Plane")
        plt.grid()
        plt.show()

    except ValueError:
        print("Invalid input. Please enter a valid complex number in the format a+bj or a-bj.")

# Call the function to run your code
TakingInput()
