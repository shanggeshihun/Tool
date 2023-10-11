from fuzzywuzzy import fuzz
def sent_sim(sent_1,sent_2):
    # 位置敏感，全匹配
    ratio=fuzz.ratio(sent_1,sent_2)
    # 位置敏感，部分匹配
    partial_ratio=fuzz.partial_ratio(sent_1,sent_2)
    # _token_sort 设置参数实现 部分匹配和全匹配
    eq_ratio=fuzz._token_sort(sent_1,sent_2,partial=False)
    eq_partial_ratio=fuzz._token_sort(sent_1,sent_2,partial=True)

    # token_sort_ratio单词是否相同，不考虑词语之间顺序
    token_sort_ratio=fuzz.token_sort_ratio(sent_1,sent_2)
    # token_set_ratio不考虑词语出现次数
    token_set_ratio=fuzz.token_set_ratio(sent_1,sent_2)
    return partial_ratio