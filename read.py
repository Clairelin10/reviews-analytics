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
