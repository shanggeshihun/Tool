# _*_coding:utf-8 _*_
# @Time　　 :2021/4/28/028   12:55
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm

def get_func_info(cell):
    with open(r'E:\工作文档\antiy\NOTE\Python\Tool\get_excel_func_1\keywords.txt','r',encoding='utf-8') as f:
        keywords_list=['isnumber(search("'+ l.strip()+ '",{},1))'.format(cell) for l in f.readlines()]
    t=','.join(keywords_list)
    return t

def get_func_info2(cell):
    with open(r'E:\工作文档\antiy\NOTE\Python\Tool\get_excel_func_1\keywords_line.txt','r',encoding='utf-8') as f:
        lines=f.read().strip()
        keywords_list=['isnumber(search("'+ l.strip()+ '",{},1))'.format(cell) for l in lines.split('|')]
    t=','.join(keywords_list)
    return t
if __name__ == '__main__':
    # r=get_func_info('h2')
    r=get_func_info2('a2')
    result='=if(or({}),1,0)'.format(r)
    with open(r'E:\工作文档\antiy\NOTE\Python\Tool\get_excel_func_1\func_result.txt', 'w', encoding='utf-8') as f:
        f.write(result)