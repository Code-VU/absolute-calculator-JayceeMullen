def calculateAbsolute():
    
    # This first line is provided for you
    target_num = 21
    in_num  = int(input("Enter a number: "))

    if in_num > target_num:
        print("Result:",abs(2*(in_num-target_num)))
    else:
        print("Result:",abs(in_num-target_num))
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

if __name__ == "__main__":
    calculateAbsolute()