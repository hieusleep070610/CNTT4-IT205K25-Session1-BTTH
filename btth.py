# lấy 3 số ngẫu nhiên
import random

#print(random.randint(100,1000))

Patient_name = input("Nhập tên bệnh nhân:")
gender = input("Nhập giới tính:")
birth_day = int(input("Nhập năm sinh:"))
numberphone = input("Nhập số điện thoại:")
email = input("Nhập email:")
symptom = input("Nhập triệu chứng ban đầu")
cost = int(input("Nhập chi phí khám"))

random_num = random.randint(100, 999)
patient_id = "BN"+ str(birth_day) + random_num

print("--- THẺ BỆNH NHÂN ---")
print("Mã BN      :",patient_id)
print("Tên        :",Patient_name)
print("Giới tính  :",gender)
print("Năm sinh   :",birth_day)
print("Điện thoại :",numberphone)
print("Email      :",email)
print("Triệu chứng:",symptom)
print("Chi phí    :",cost)
