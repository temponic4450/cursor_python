# add_data.py
f = open("/Users/LeeChangHwan/Desktop/study/cursor/cursor_python/basic/jump2python_code/04-3/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
