import os, sys
import codecs
import re
import pypinyin
from pypinyin import pinyin, lazy_pinyin

class Sequence(object):
    def __init__(self, Data_file_folder, File_list_txt, Output_File):
        super().__init__()
        self.Data_file_folder = Data_file_folder # 数据所在文件夹
        self.File_list_txt = File_list_txt # 数据文件列表
        self.Output_File = Output_File # 汇总结果文件

    def Get_Data(self):
        if not os.path.exists(self.Data_file_folder):
            print("输入文件夹路径不存在，请重新输入!!!")
            exit()
        else:
            Data_file_list = []
            Sequence_Combining = []
            for root, dirs, names in os.walk(self.Data_file_folder):
                for filename in names:
                    # 把文件名中的汉字转换成拼音首字母
                    # filename = re.compile(u'[^a-zA-Z]+', re.UNICODE).sub("",filename)
                    filename_pinyin = pinyin(filename, style=pypinyin.FIRST_LETTER)
                    filename_str = []
                    for ch in filename_pinyin:
                        filename_str.extend(ch)
                    new_filename = "".join(filename_str).replace(' ', '-') # 文件名不允许有空格
                    os.rename(os.path.join(root, filename), os.path.join(root, new_filename)) # 文件名包含中文的文件进行重命名
                    #os.remove(os.path.join(root, filename)) # 删除文件名包含中文的文件
                    filename = new_filename
                    # 获取文件列表
                    file_name_path = os.path.join(root, filename)
                    if ".seq" in file_name_path:
                        print("正在处理 %s\n" %file_name_path)
                        Data_file_list.append(file_name_path)
                        # 将带BOM的UTF-8转换成不带BOM的
                        BUFSIZE = 4096
                        BOMLEN = len(codecs.BOM_UTF8)
                        with open(file_name_path, "r+b") as fp:
                            chunk = fp.read(BUFSIZE)
                            if chunk.startswith(codecs.BOM_UTF8):
                                i = 0
                                chunk = chunk[BOMLEN:]
                                while chunk:
                                    fp.seek(i)
                                    fp.write(chunk)
                                    i += len(chunk)
                                    fp.seek(BOMLEN, os.SEEK_CUR)
                                    chunk = fp.read(BUFSIZE)
                                fp.seek(-BOMLEN, os.SEEK_CUR)
                                fp.truncate()
                        # 输出文件
                        Output_File = file_name_path.split('.')[0]+".fasta"
                        with open(Output_File, 'w') as f_write :
                            if '>' not in open(file_name_path, 'r').read():
                                f_write.write('>' + filename.split('.')[0] + '\n')
                            for line in open(file_name_path, 'r').readlines():
                                line = str(line)
                                print(line)
                                f_write.write(line)
                        f_write.close()

                        Sequence_Combining.append(open(file_name_path.split('.')[0] + '.fasta', 'r').read() + '\n')

            # 将读取到的文件名称写入txt文件
            with open(self.File_list_txt, 'w') as f:
                for data_file in Data_file_list:
                    f.write(data_file + '\n')
            f.close()
            print("共完成%i个数据读取汇总保存! ^_^" %len(Data_file_list))

            # 将所有序列写入fasta文件
            print(Sequence_Combining)
            if os.path.exists(self.Output_File):
                if os.path.getsize(self.Output_File) != 0:
                    os.remove(self.Output_File)
            Output = open(self.Output_File, 'a')
            for item in Sequence_Combining:
                Output.write(str(item))

if __name__=='__main__':
    # 获取文件夹及文件保存路径等参数
    Current_path = os.path.abspath(os.path.dirname(__file__)) # 当前路径
    Data_file_folder = input("请输入数据所在文件夹路径，例如：C:\Desktop\Sequence" +'\n')
    File_list_txt = Current_path + '\\文件列表.txt'
    Output_File = Current_path + '\\All_Sequence_Combined.fasta'
    Me = Sequence(Data_file_folder, File_list_txt, Output_File)
    Me.Get_Data()