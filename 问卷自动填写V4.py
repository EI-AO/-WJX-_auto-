from selenium import webdriver
import random
import time
import copy

url = 'https://www.wjx.cn/m/96637563.aspx'

path = r'C:\Program Files\Mozilla Firefox\Firefox.exe'
option = webdriver.FirefoxOptions()
option.add_argument('headless')
#多选
choose = []
def choice(choose,chance):#指定概率不重复选择
    global a
    x = random.uniform(0,1)
    c = 0.0
    for a,a_ in zip(choose,chance):
        c += a_
        if x < c:
            break
    return a

#选项概率列表                
def append_chooselist():
    chooselist = []
    q_list = []
    for i in range(len(answer)):
        q_list.append(i)
    print("本题共",len(answer),"题")
    c_list = [eval(x) for x in input("请输入相应概率:").split(',')]#概率
    chooselist.append(q_list)#选项
    chooselist.append(c_list)#概率
    chance_lists.append(chooselist)

t = eval(input('数量：'))

count = 1
Finish = 0

for i in range(t):
    driver = webdriver.Firefox(options=option)
    driver.get(url)
    #定位xpath
    xpaths = driver.find_elements_by_class_name("ui-field-contain")
    #定位问题
    questens = driver.find_elements_by_class_name('ui-controlgroup')
    for index,answers in enumerate(questens):
        #定位选项
        answer = answers.find_elements_by_class_name('label')
        #定位题型
        types = xpaths[index].get_attribute('type')
        if i == 0:
            if types == '3':
                print("======",index+1,"题为单选======")
                append_chooselist()
                answer[choice(chance_lists[index][0],chance_lists[index][1])].click()
            elif types == '4':
                print("******",index+1,"题为多选******")
                append_chooselist()
                x = copy.deepcopy(chance_lists[index][0])
                y = copy.deepcopy(chance_lists[index][1])
                for m in range(1,random.randint(2,len(chance_lists[index][0]))):
                    answer[choice(x,y)].click()
                    del y[x.index(a)]
                    x.remove(a)
                    time.sleep(1)
        else:
            if types == '3':
                answer[choice(chance_lists[index][0],chance_lists[index][1])].click()
                time.sleep(1)
            elif types == '4':
                x = copy.deepcopy(chance_lists[index][0])
                y = copy.deepcopy(chance_lists[index][1])
                for l in range(1,random.randint(2,len(chance_lists[index][0]))):
                    answer[choice(x,y)].click()
                    del y[x.index(a)]
                    x.remove(a)
                    time.sleep(1)
    #提交
    finish = driver.find_element_by_class_name('voteDiv')
    finish.click()
    time.sleep(4)
    finally_url = driver.current_url
    if finally_url != 'https://www.wjx.cn/m/96637563.aspx':
        print('第{}次，Finish!'.format(count))
        count += 1
        Finish += 1
    else:
        print('第{}次，Fail!'.format(count))
        count += 1
    driver.quit()
print("本次共成功",Finish,"份问卷")
