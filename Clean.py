import os,re,shutil,time

namebforf = {
    "exe":"应用程序",
    "zip":"压缩包",
    "7z":"压缩包",
    "rar":"压缩包",
    "gz":"压缩包",
    "jpg":"图片",
    "png":"图片",
    "gif":"图片",
    "ini":"文档",
    "bat":"脚本",
    "txt":"文档",
    "lnk":"快捷方式",
    "jar":"jar包",
    "ico":"图标",
    "e":"脚本",
    "css":"CSS",
    "mp3":"音乐",
    ".aac":"音乐",
    "doc":"docx",
    "ppt":"ppt演示",
    "pptx":"ppt演示",
    "pdf":"pdf阅读",
    "xls":"表格",
    "xlsx":"表格",
    "avi":"视频",
    "mp4":"视频",
    "flv":"视频",
    "iso":"镜像ISO",
    "msi":"安装程序",
    "html":"html",
    "torrent":"BT"
}

# find_disk = input("你将整理目录为: ")
# os.chdir(find_disk)

#re
def re_find_name(sor):
    return re.search(r'[^\.]\w*$',sor).group()

filenames = os.listdir('.')
asf = []
for root, ls, files in os.walk("."):
    if len(asf) != 1:
        asf += files;
        break
# print(asf)
for move in range(len(asf)):
    for key,filename_bofor in namebforf.items():
        if re_find_name(asf[move]) == key:
            if os.path.exists(os.getcwd()+"\\"+namebforf[key]) == False:
                os.mkdir(os.getcwd()+"\\"+namebforf[key])
                time.sleep(0.2)
            elif os.path.exists(os.getcwd()+"\\"+namebforf[key]) == True:
                shutil.move(os.getcwd()+"\\"+asf[move],os.getcwd()+"\\"+namebforf[key])
                time.sleep(0.2)
                print("旧文件目录: "+os.getcwd()+"\\"+asf[move],"新文件目录: "+os.getcwd()+"\\"+namebforf[key])