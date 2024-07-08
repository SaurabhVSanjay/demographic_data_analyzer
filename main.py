# main.py
from mean_var_std import calculate

def main():
    try:
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        result = calculate(data)
        
        for key, value in result.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
