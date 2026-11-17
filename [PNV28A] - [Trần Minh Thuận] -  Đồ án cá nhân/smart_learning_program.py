from my_def_function import def_function
import sys
print(("+" + (50*"-")+ "+").center(100," "))
print(("|" + (50*"*") + "|").center(100," "))
print(("|" + ("Chương trình học thông minh".center(50,"*")) + "|").center(100, " ")) 
print(("|" + (50*"*") + "|").center(100," "))
print(("+" + (50*"-")+ "+").center(100," "))
print(" ")
print(("+" + (100*"-")+ "+").center(100," "))
print(("|" + "MENU".center(100, "=") + "|").center(100, " "))
print(("+" + (100*"-")+ "+").center(100," "))
print(" ")      
while True:
    try:
        print("Vui lòng chọn tính năng")
        print("1. Xem lịch")
        print("2. Tính lương")
        print("3. Xem lương")
        print("4. Xem thông tin nhân viên")
        print("5. Tính điểm học sinh")
        print("6. Thoát chương trình")
        choose_number = int(input("Mời bạn nhập số: "))
        if 1 <= choose_number <= 6:
            if choose_number == 1:
                while True:
                    try:
                        thang = int(input("Mời bạn nhập tháng(1-12): "))
                        def_function.processing_month_input(thang)
                        note = (input("Bạn có muốn tiếp tục hay không? (y/n): "))
                        if note == "y" or note== "Y":
                            continue
                        elif note == "n"or note== "N":
                            print(" ")
                            break
                    except ValueError:
                        print("Giá trị không hợp lệ. Vui lòng nhập đúng định dạng!")        
            elif choose_number == 2:
                while True:
                    try:
                        so_gio_lam = int(input("Nhập số giờ làm: "))
                        luong_co_ban = int(input("Nhập lương cơ bản (đồng): "))
                        if len(str(luong_co_ban)) >= 5 and luong_co_ban > 0:
                            luong_tong = def_function.salary_caculator_tool(so_gio_lam, luong_co_ban)
                            print(f"Tổng số tiền lương của bạn: {float(luong_tong):,.0f}")
                        else:
                            print("Giá trị quá nhỏ. Vui lòng thử lại")
                            continue
                        note = (input("Bạn có muốn tiếp tục hay không? (y/n): "))
                        if note == "y" or note== "Y":
                            continue
                        elif note == "n" or note== "N":
                            break
                    except ValueError:
                        print("Giá trị không hợp lệ. Vui lòng nhập đúng định dạng!")
            elif choose_number == 3:
               while True:
                    try:
                        danh_sach_luong = []
                        sl_nhan_vien = int(input("Nhập số lượng nhân viên: "))
                        for i in range (1, sl_nhan_vien + 1):
                            luong_nhan_vien = float(input(f"Nhập lương nhân viên thứ {i}: "))
                            if luong_nhan_vien > 0:
                                danh_sach_luong.append(luong_nhan_vien)
                        print (f"Danh sách lương theo thứ tự tăng dần: ")
                        print(def_function.salary_preview(danh_sach_luong))
                        note = (input("Bạn có muốn tiếp tục hay không? (y/n): "))
                        if note == "y" or note== "Y":
                            continue
                        elif note == "n" or note== "N":
                            break
                    except ValueError:
                        print("Giá trị không hợp lệ. Vui lòng nhập đúng định dạng!")  
            elif choose_number == 4:
                while True:
                    ho_ten = input("Nhập họ và tên nhân viên: ").split()
                    def_function.staff_name_and_surname_processing(ho_ten)
                    note = (input("Bạn có muốn tiếp tục hay không? (y/n): "))
                    if note == "y" or note== "Y":
                        continue
                    elif note == "n" or note== "N":
                        break
            elif choose_number == 5:
                while True:
                    try:
                        so_luong_hoc_phan = int (input("Nhập số lượng học phần: "))
                        def_function.avgrage_result(so_luong_hoc_phan)
                        note = (input("Bạn có muốn tiếp tục hay không? (y/n): "))
                        if note == "y" or note== "Y":
                            continue
                        elif note == "n" or note== "N":
                            break
                    except ValueError:
                        print("Giá trị không hợp lệ. Vui lòng nhập đúng định dạng!")
            elif choose_number == 6:
                print("Tạm biệt!")
                sys.exit()
        else:
            print("Tính năng đang phát triển. Vui lòng thử lại sau!")
            print(" ")
            continue
    except ValueError:
        print("Giá trị không hợp lệ. Vui lòng nhập đúng định dạng!")
        print(" ")