import os.path
import os #判断磁盘
filename = 'student.txt'

def main():
    while True:
        menu()
        choice = int(input('请选择\n'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？t/f\n')
                if answer == 't' or answer == 'T':
                    print('谢谢您的使用,欢迎下次使用，再见！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            print('输入有误，请重新输入')
            continue

def menu():
    print('=============================学生管理系统======================================')
    print('-------------------------------功能菜单---------------------------------------')
    print('\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t6.统计学生人数')
    print('\t\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t\t0.退出')
    print('-----------------------------------------------------------------------------')

def insert():
    student_list=[]
    while True:
        id = input('请输入学号（如096）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            chinese = int(input('请输入语文成绩：'))
            math = int(input('请输入数学成绩：'))
            english = int(input('请输入英语成绩：'))
            physics = int(input('请输入物理成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue

        #将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'chinese': chinese, 'math': math, 'english': english, 'physics': physics}
        student_list.append(student)
        answer = input('是否继续添加？t/f\n')
        if answer == 't' or answer == 'T':
            continue
        else:
            break
        #调用save()函数
    save(student_list)
    print('学生信息录入完毕！！！')
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8') #若文件存在，则追加append
    except:
        stu_txt = open(filename, 'w', encoding='utf-8') #若文件不存在，则写入write
    for item in lst:
        stu_txt.write(str(item)+'\n')   #写入文件并换行
    stu_txt.close()

def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按学号查找请输入1，按姓名查找请输入2：\n')
            if mode == '1':
                id = input('请输入学生学号：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                search()

            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))  #转换成字典
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)

            show_student(student_query)  #显示查询结果
            student_query.clear()  #清空列表
            answer = input('是否要继续查询？t/f\n')
            if answer == 't' or answer == 'T':
                continue
            else:
                break
        else:
            print('暂未保存该学生信息')
            continue

def show_student(lst):
    if len(lst) == 0:
        print('没有查找到学生信息，无数据显示')
        return
    #定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^12}\t'
    print(format_title.format('学号','姓名','语文成绩','数学成绩','英语成绩','物理成绩','总成绩'))
    #定义内容显示格式
    format_data = '{:^8}\t{:^4}\t{:^20}\t{:^6}\t{:^20}\t{:^6}\t{:^22}\t'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('chinese'),
                                 item.get('math'),
                                 item.get('english'),
                                 item.get('physics'),
                                 int(item.get('chinese')) + int(item.get('math')) + int(item.get('english')) + int(item.get('physics'))
                                 ))

def delete():
    while True:
        student_id = input('请输入要删除学生的学号：')
        if student_id != '':
            if os.path.exists(filename) :  #判断文件是否存在
                with open(filename, 'r', encoding='utf-8')as file:
                    student_old = file.readlines()
            else:
                student_old = []    #若文件不存在，则创建一个空列表
            flag = False            #标记是否删除
            if student_old:         #判断学生列表是否有数据
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d={}        #建立一个空字典
                    for item in student_old:
                        d=dict(eval(item))  #将字符串转化为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True #当查找出要删除的信息时，把标记设成已删除状态
                    if flag:
                        print(f'学号为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到学号为{student_id}的学生信息')
                        show()  # 删除之后要重新显示所有学生信息
                    answer = input('是否继续删除？t/f\n')
                    if answer == 't' or answer == 'T':
                        continue
                    else:
                        break
            else:
                print('无学生信息')
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入学生学号：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict (eval(item)) #eval()函数，将字符串还原为本来的类型
            if d['id']==student_id:
                print('找到学生信息，可以修改相关信息')

                #修改所有成绩，如何只修改错误的成绩
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['chinese'] = input('请输入语文成绩：')
                        d['math'] = input('请输入数学成绩')
                        d['english'] = input('请输入英语成绩')
                        d['physics'] = input('请输入物理成绩')
                    except:
                        print('您输入的成绩有误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
        answer = input('是否继续修改其他学生信息？t/f\n')
        if answer == 'T' or answer == 't':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_list = rfile.readlines()
        stu_new = []
        for i in stu_list:
            d = dict(eval(i))
            stu_new.append(d)
    else:
        return
    asc_or_desc = input('请选择 1.升序，2.降序 ：')
    if asc_or_desc == '1':
        asc_or_desc_bool = False  #升序标记
    elif asc_or_desc == '2':
        asc_or_desc_bool = True   #标记降序
    else:
        print('输入错误')

    m = input('请选择排序方式（1.按语文成绩排序 2.数学 3.英语 4.物理 5.总成绩）：')
    if m == '1':
        stu_new.sort(key = lambda x:int(x['chinese']), reverse = asc_or_desc_bool)
    elif m == '2':
        stu_new.sort(key=lambda x: int(x['math']), reverse=asc_or_desc_bool)
    elif m == '3':
        stu_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif m == '4':
        stu_new.sort(key=lambda x: int(x['physics']), reverse=asc_or_desc_bool)
    elif m == '5':
        stu_new.sort(key=lambda x: int(x['chinese'])+int(x['math'])+int(x['english'])+int(x['physics']), reverse=asc_or_desc_bool)
    else:
        print('输入有误！')
    show_student(stu_new)


    #lambda函数
    #对于单行函数，可省去定义函数的过程；对于不需要多次使用的函数，用lambda可以在用完后立即释放
    #表达式 lambda a , b : ab之间关系
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf=8') as rfile:
            stu = rfile.readlines()
            if stu:
                print(f'一共有{len(stu)}名学生')
            else:
                print('暂未录入学生信息')
    else:
        print('暂未保存数据信息')
def show():
    stu_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu = rfile.readlines()
            for item in stu:
                stu_lst.append(eval(item))
            if stu_lst:
                show_student(stu_lst)
    else:
        print('暂未保存学生信息')

if __name__ == '__main__':   #直接拼写main
    main()

