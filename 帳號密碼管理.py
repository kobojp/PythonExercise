#帳號 密碼 管理 
#新增帳號, 修改密碼, 顯示所有帳號密碼, 刪除帳號, 結束程式
#請先建立一個passwod.txt  內容 ： {'chiou': '654321', '寶可夢': 'pica'}

import os
import ast

def menu():
    os.system("cls")
    print("帳號、密碼管理系統")
    print("------------------------")
    print("1. 新增帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修 改 密 碼")
    print("4. 刪除帳號、密碼")
    print("0. 結束程式")
    print("------------------------")

def ReadData(): #讀取資料
    with open('password.txt', 'r', encoding='UTF-8-sig') as f: #utf-8-sig 去除BOM
        filedata = f.read()
        if filedata !="": #如果文件資料不等於空的 則會轉換資料
            data = ast.literal_eval(filedata)
            return data
        else: return dict() #如果文件資料是空的 傳回空的字典dict()

def disp_data(): #顯示帳號密碼
    print("帳號\t 密碼") #\t = tab 
    print("================")
    for key,values in data.items(): #另一種字典印出方法
        print("{}\t{}".format(key,values))
    # for key in data: #字典印出方法
    #     print("{}\t{}".format(key,data[key])) #顯示帳號密碼,變數data 由主程式宣告的全域變數型態的字典
    input("按任意鍵返回主選單")


def input_data(): #新增帳號密碼
    while True:
        name = input("請輸入帳號(Enter==> 停止輸入)")
        if name=="": break #不在新增帳號就跳出
        if name in data: #如果 從name輸入的資料 在data資料已經有了 即成立
            print("{}帳號已存在!".format(name))
            continue #繼續 意思 跳過以下 從頭跑 name開始
        password=input("請輸入密碼") 
        data[name]=password #新增這筆資料
        with open('password.txt', 'w', encoding='UTF-8-sig') as f: #將輸入的資料，回寫入資料
            f.write(str(data))
        print("{} 已被儲存完畢".format(name))
        
def edit_data(): #修改帳號的密碼
    while True:
        name =input("請輸入要修改的帳號 (Enter==> 停止輸入)")
        if name =="":break
        if not name in data: #data中 沒有輸入的name帳號
            print("{} 帳號不存在!".format(name))
            continue
        print("原來密碼為: {}".format(data[name])) #顯示輸入帳號與密碼
        password=input("請輸入新密碼")
        data[name]=password
        with open('password.txt', 'w', encoding='UTF-8-sig') as f:
            f.write(str(data))
            input("密碼更改完畢，請按任意返回主選單")
            break

def delete_data(): #刪除帳號
    while True:
        name =input("請輸入要刪除的帳號 (Enter==> 停止輸入)")
        if name=="":break
        if not name in data: #if name輸入的資料沒有在 data裡面
            print("{} 帳號不存在".format(name))
            continue
        print("確定要刪除 {} 的資料!:".format(name))
        yn=input("(Y/N) ?")
        if yn=="Y" or yn=="y":
            del data[name]
            with open('passwod', 'w',encoding='UTF-8-sig') as f:
                f.write(str(data))
                input("已刪除完畢，請按任意鍵返回主選單")
                break




#主程式從這裡開始#
data=dict()
data = ReadData() # 讀取資料 轉dict ,全域變數

while True:
    menu()
    choice = int(input("請輸入你的選擇 :"))
    print()
    if choice==1:
        input_data()
    elif choice==2:
        disp_data()
    elif choice==3:
        edit_data()
    elif choice==4:
        delete_data()
    else:
        break
print("程式執行完畢")

