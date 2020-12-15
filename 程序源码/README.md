
***********************************************************************************************************************
                                               Documentation

-----------------------------------------------------------------------------------------------------------------------
What is it?
    This is a personal python programe, witch is used to translate DNA sequencing Pandaseq file which filename end with
'.seq' to fasta format, and combine each fasta sequcen to a single file(All_Sequence_Combined.fasta).
    In this folder you can find sample data and originally source code and is also test_data freely available.
    
-----------------------------------------------------------------------------------------------------------------------
The Latest Version
Details of the latest version can be found on the github page https://github.com/Z19900505/Transform_seq_to_fasta.

-----------------------------------------------------------------------------------------------------------------------
Installation
1. First of all this executable program based on python 3.x, and packed with pyinstaller.
2. You should trust executable program, I promise it's safe. some nti-virus software may detect it as virus and delete it,
   you can close your nti-virus software temporarily or add it to whitelists.
3. Double click the '测序Seq序列转换.exe' file to run this Programe and follow the prompts, enjoy it.

Realse & Debug
-----------------------------------------------------------------------------------------------------------------------
Realse 2020.12.15.01
1. 解决部分seq文件编码问题，将所有带BOM的UTF-8格式文件转换成不带BOM的UTF-8，避免读取过程中出现BOM标识（'\xef\xbb\xbf）；
2. 解决部分seq文件名包含中文字符或空格造成读取失败问题。中文字符自动替换成拼音首字母，例如："拼接失败" ——> "pjsb"；
3. 解决部分seq文件内容首行不包含fasta格式所需的">"和注释.