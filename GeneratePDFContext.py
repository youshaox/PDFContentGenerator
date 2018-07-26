# coding:utf-8
# 添加PDF书签
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
使用教程:
1. 需要将要添加书签的pdf改为input.pdf
2. 手动将书签元数据overwrite bookmark_meta文件
3. 填入page_offset 页数偏移量.
4. python2下运行 python GeneratePDFContext.py
"""
def main():
    pdf_handler = MyPDFHandler('./input.pdf',mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('./bookmark_meta',page_offset = 16)
    pdf_handler.save2file('./output.pdf')

if __name__ == '__main__':
    main()