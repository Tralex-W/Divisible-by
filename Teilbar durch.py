while True:
    nums = input("\nTrag eine Nummer ein: ")
    count, result = 0, []

    def check():
        global nums, count, result
        for i in range(2,round((nums+2)/2)):
            if nums % i == 0:
                result.append(i)
                count =+ +1
        if count == 0:
            print(nums, 'ist eine Primzahl!') 
        else:
            result = str(result)
            print(nums, "ist teilbar durch: ", result[1:-1])
     
    def isnumeric():
        global nums
        try: nums = int(nums)
        except:
            print("Nur Zahlen ohne Dezimalen!")

    if nums == "END":
        break

    isnumeric()
    if type(nums) == int:
        check()

