import math

while True:
    print("\n ماشین حساب مهندسی ")
    print("1) جمع")
    print("2) تفریق")
    print("3) ضرب")
    print("4) تقسیم")
    print("5) توان")
    print("6) جذر")
    print("0) خروج")

    choice = input("انتخاب شما: ")
    #خروج
    if choice == "0":
        print("خارج شدید")
        break
    #جذر
    if choice == "6":
        num = float(input("عدد را وارد کنید: "))
        if num < 0:
            print("عدد منفی جذر ندارد")
        else:
            print(f"جذر {num} = {math.sqrt(num)}")
        continue   
    #عدد نامعتبر
    if choice != "1" and choice !="2" and choice !="3" and choice !="4" and choice !="5":
        print("انتخاب نامعتبر")
        continue
    
    a = float(input("عدد اول: "))
    b = float(input("عدد دوم: "))

    match choice:
        case "1":
            print(f"نتیجه: {a + b}")
        case "2":
            print(f"نتیجه: {a - b}")
        case "3":
            print(f"نتیجه: {a * b}")
        case "4":
            if b == 0:
                print("تقسیم بر صفر مجاز نیست")
            else:
                print(f"نتیجه: {a / b}")
        case "5":
            print(f"نتیجه: {a ** b}")
