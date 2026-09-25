def divide_nums():
    try:
        a = int(input("Birinci ədədi daxil edin: "))
        b = int(input("İkinci ədədi daxil edin: "))
        print("a / b =", a / b)
        print("a + b =", a + b)
    except ValueError:
        print("Ədədə çevrilə bilməyən simvol daxil edildı.")
    except ZeroDivisionError:
        print("Sıfıra bölmək olmaz!")
        print("a / b = sonsuzluq")
        print("a + b =", a + b)
    except:
        print("Gözlənilməyən böyük xəta baş verdi.")

print(divide_nums())