# 复原图片名.py
#
# 把已编号的特定格式（默认为jpg和png）的图片名称复原。图片原名保存在同目录下的“图片原文件名.txt”。
#
######
# “图片原文件名.txt”格式如下：
# 文件名1
# 文件名2
# ...
# 文件名n
######


import os


photo_format_arr = ['jpg', 'png']
backup_file_name = "图片原文件名.txt"


def main():
    path = "./"
    file_name_arr = os.listdir(path)
    backup_file = open(backup_file_name, 'r')

    file_name_arr.sort()

    n = 1
    for file_name in file_name_arr:
        for photo_format in photo_format_arr:
            if file_name == (str(n) + '.' + photo_format):
                original_name = backup_file.readline()
                if not original_name:
                    print("Error: not enough names in backup file")
                    break

                original_name = original_name[0:-1]  # 去除'\n'
                
                if original_name:
                    try:
                        os.rename(path + file_name, original_name)
                    except:
                        print("Error: cannot rename %s as %s" % (file_name, original_name))
                else:
                    print("file \"%s\" has no original name." % file_name)
                n += 1


if __name__ == '__main__':
    main()
