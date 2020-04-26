# 给图片编号.py
#
# 把同目录下的特定格式（默认为jpg和png）的图片文件按"1，2，3...n"的编号命名，将图片原名保存到同目录下的“图片原文件名.txt”中。
#
######
# “图片原文件名.txt”格式如下：
# 文件名1
# 文件名2
# ...
# 文件名n
######

import os

LEAST_FORMAT_LEN = 4
photo_format_arr = ['jpg', 'png']
backup_file_name = '图片原文件名.txt'


def isPhoto(file_name):
    if len(file_name) <= LEAST_FORMAT_LEN:
        return False

    split_arr = file_name.split('.')

    if len(split_arr) < 2:
        return False

    file_format = split_arr[-1]

    for photo_format in photo_format_arr:
        if file_format == photo_format:
            return True

    return False


def main():
    path = "./"
    file_name_arr = os.listdir(path)
    backup_file = open(backup_file_name, 'w')

    n = 1
    for file_name in file_name_arr:
        if isPhoto(file_name):
            backup_file.write(file_name + '\n')

            split_arr = file_name.split('.')
            file_format = split_arr[-1]

            new_name = str(n) + '.' + file_format
            try:
                os.rename(path + file_name, new_name)
            except:
                print("Error: cannot rename %s as %s" % (file_name, new_name))
            
            n += 1

    backup_file.close()
    os.system("pause")
        

if __name__ == "__main__":
    main()
