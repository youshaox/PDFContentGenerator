#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by youshaox on 2/8/18
"""
function:
1. 读取页码文件和bookmark_meta
2. 页码转换为列表
3. 追加到bookmark_meta的每一行最后
python2 append_to_final.py <pageNum_filename> <bookmark_meta_filename>
"""
import Queue


def check_and_add_space(line):
    """

    :param line:
    :return:
    """

def gen_pagenumber_queue(filename):
    """

    :param filename:
    :return:
    """
    q = Queue.Queue()
    file_obj = open(filename, 'r')
    all_lines = file_obj.readlines()
    for line in all_lines:
        q.put(line)
    return q



if __name__ == '__main__':

    bookmark_meta_filename = "bookmark_meta"
    pagenum_filname = "pagenum"
    pagenum_q = gen_pagenumber_queue(pagenum_filname)
    #
    file_obj = open(bookmark_meta_filename,'r')
    all_lines = file_obj.readlines()
    for line in all_lines:
        pagenum = pagenum_q.get()
        line = line.rstrip() + "@" + pagenum
        print line

    file_obj.close()

