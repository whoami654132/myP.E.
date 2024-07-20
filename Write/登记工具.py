import easygui as e 
global e2
e2={}
# def mv():
#     import os
#     import shutil

#     # 定义源目录（当前目录）和目标目录
#     src_dir = '.'  # 当前目录，可以用'.'表示
#     dst_dir = '../成绩查询'  # 替换为你的目标目录路径

#     # 确保目标目录存在
#     if not os.path.exists(dst_dir):
#         os.makedirs(dst_dir)

#     # 遍历源目录下的所有文件
#     for filename in os.listdir(src_dir):
#         # 检查文件是否是.txt文件
#         if filename.endswith('.txt'):
#             # 构建源文件和目标文件的完整路径
#             src_file = os.path.join(src_dir, filename)
#             dst_file = os.path.join(dst_dir, filename)
            
#             # 使用shutil的copy2函数复制文件，这将保留文件的元数据（如时间戳）
#             shutil.copy2(src_file, dst_file)
#             print(f"Copied {src_file} to {dst_file}")

#     print("All .txt files have been copied and overwritten in the destination directory.")



def readfile():
    f = open('../成绩查询/Names.txt', 'r')
    x = open('../成绩查询/Passwords.txt', 'r')
    xw=[]

    w = open('../成绩查询/Highs.txt', 'r')
    i=0
    for line in f:
        e2[str(line).replace("\n","")]=[]
        xw.append(str(line).replace("\n", ""))
        i+=1
    i=0
    for line in x:
        e2[xw[i]].append(str(line).replace("\n",""))
        i+=1
    i=0
    for line in w:
        e2[xw[i]].append(str(line).replace("\n", ""))
        i+=1
    

def zhuce():
    le = e.passwordbox("请输入密码")
    High = e.passwordbox("您的身高是：")

    f=open('../成绩查询/Names.txt','a')
    f.writelines("\n"+d)
    f.close
    f=open('../成绩查询/Highs.txt','a')
    f.writelines("\n"+High)
    f.close
    f=open('../成绩查询/Passwords.txt','a')
    f.writelines("\n"+le)
    f.close
    
    
    


a=["进入","退出"]

readfile()
while True:
    print(e2)
    b = e.ccbox("欢迎来到成绩登记", "欢迎来到成绩登记", a)
    if b == True:
        global d
        d=e.enterbox("请输入账号自动注册")
        
        if d in e2:
            le=e.msgbox("账号存在无需注册")

        else:
            zhuce()

            readfile()
            pass
        pass
    else:
        break


