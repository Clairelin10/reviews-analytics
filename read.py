data =[]
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 50000 == 0:
            print(len(data))
print ('檔案讀取完畢，總共有',len(data),'筆資料。')


print(data[0])
print(len(data[0]))
sum_len = 0
for d in data:
    sum_len += len(d)
print('留言長度平均為', sum_len/len(data))
#篩選, 寫程式的難處在把要做的事情邏輯化，並用正確的程式碼撰寫出來。
new = []
for d in data:
    if len(d) > 300:
        new.append(d)
print('總共有', len(new), '筆資料留言數字大於300')
#找出留言中有good的留言

# good = []
#     for d in data:
#         if 'good' in d:
#         good.append(d)
# print('一共有', len(good), '筆留言提到good')

# list comprehensive 一行快寫法
good =[d for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')

#也可以不存入d到good清單，而是以Yes, 1 or true取而代之
bad = ['bad' in d for d in data]
print (bad[0], bad[1], bad[2])
#以下三行，等於上面的快寫
bad = []
for d in data:
    bad.append('bad' in d)
