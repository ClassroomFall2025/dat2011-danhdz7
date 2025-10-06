def run_com():
    print("Máy tính đơn giản")
    while True:
        print("\n1. Cộng (+)")
        print("2. Trừ (-)")
        print("3. Nhân (*)")
        print("4. Chia (/)")
        print("0. Thoát")

        lua_chon = input("Nhập số tương ứng phép tính: ")

        match lua_chon:
            case "0":
                print("Bye")
                break

            case "1" | "+":
                a = float(input("Số thứ nhất: "))
                b = float(input("Số thứ hai: "))
                print(f"Kết quả: {a} + {b} = {a + b}")

            case "2" | "-":
                a = float(input("Số thứ nhất: "))
                b = float(input("Số thứ hai: "))
                print(f"Kết quả: {a} - {b} = {a - b}")

            case "3" | "*":
                a = float(input("Số thứ nhất: "))
                b = float(input("Số thứ hai: "))
                print(f"Kết quả: {a} * {b} = {a * b}")

            case "4" | "/":
                a = float(input("Số thứ nhất: "))
                b = float(input("Số thứ hai: "))
                if b == 0:
                    print("Không thể chia cho 0 !!!")
                else:
                    print(f"Kết quả: {a} / {b} = {a / b}")

            case _:
                print("Lựa chọn không hợp lệ !!!")
