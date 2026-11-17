def processing_month_input(month):
        if month < 1 or month > 12:
            return print("Mời bạn nhập lại tháng")
        elif month == 2:
            year = int (input("Mời bạn nhập năm: "))
            if year < 0:
                return print("Mời bạn nhập lại năm")
            elif year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
                return print("29 ngày")
            else:
                return print("28 ngày")   
        elif month != 2:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return print("31 ngày")
            elif month in [4, 6, 9, 11]:
                return print("30 ngày")


def salary_caculator_tool(hour_total, basic_salary):
        if basic_salary > 0 and hour_total > 0:
            if 0 < hour_total <= 40:
                return basic_salary * hour_total
            elif hour_total > 40:
                    return basic_salary * ((hour_total-40)*1.5 + 40)
            else:
                print ("Vui lòng thử lại! ")


def salary_preview(salary):
    n = len(salary)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if salary[j] < salary[min]:
                min = j
        salary[i], salary[min] = salary[min], salary[i]
    return salary


def staff_name_and_surname_processing(fullname):
    name_component_list = []
    for name_and_surname in fullname:
        fullname_capped = name_and_surname.capitalize()
        name_component_list.append(fullname_capped)
    staff_fullname_processed=" ".join(name_component_list)
    staff_name =name_component_list [-1]
    staff_surname =" ".join(name_component_list[:-1])
    print(f"Họ lót của nhan viên: {staff_surname}")
    print(f"Tên của nhân viên: {staff_name}")
    print(f"Tên đầy đủ của nhân viên: {staff_fullname_processed}")


def avgrage_result(subject_quantity):
    mark_total = 0.0
    multiple_total = 0.0
    for i in range (1, subject_quantity + 1):
        mark = float(input(f"Nhập điểm học phần {i}: "))
        multiple = float(input(f"Nhập hệ số học phần thứ {i} (1, 1.5, 2, 2.5, 3): "))
        if 0 <= mark <= 10 and multiple in (1, 1.5, 2, 2.5, 3):
            mark_total += mark * multiple
            multiple_total += multiple
        else:
            print("Vui lòng thử lại!")
            continue
    print(f"Điểm trung bình mỗi môn học phần: {mark_total/multiple_total:.2f}")