# 10パズル問題

import itertools

# 文字列formulaについて逆ポーランド記法の計算を解く関数
# 解いた結果の数を返す
def rpn(formula):
    f_list = formula.split(' ')
    stack = []
    for i in range(len(f_list)):
        # 数はstackに積む
        if f_list[i].isdecimal():
           stack.append(int(f_list[i]))
        # 演算子はstackに演算可能な数があるかチェックする
        elif len(stack) < 2:
            print('不正な入力です（演算子に対して数値の個数が不足しています）。処理を終了します。')
            return None
        # 演算可能ならばstack最後尾2個の要素をpopし演算した結果の数をstackに積む
        else:
            a = stack.pop()
            b = stack.pop()
            if f_list[i] == '+':
                stack.append(b + a)
            if f_list[i] == '-':
                stack.append(b - a)
            if f_list[i] == '*':
                stack.append(b * a)
            if f_list[i] == '/':
                if a == 0:
                    return None
                stack.append(b / a)
    # 処理終了後stackに2個以上要素が残っている場合は不正な入力
    if len(stack) > 1:
        print('不正な入力です（数値に対して演算子の個数が不足しています）。処理を終了します。')
        return None
    return stack[0]

# タプルnum_tupleの数の組み合わせについて逆ポーランド記法の式を生成する関数
# num_usedは式で使用されている数字の数、opr_usedは式で使用されている演算子の数
# num_tupleに出てくる数の順番に式に追加していく
def make_rpn_formula(num_tuple, num_used = 0, opr_used = 0, formula = []):
    num_tuple = tuple(str(num_tuple[i]) for i in range(len(num_tuple)))
    # 逆ポーランド記法の式が完成（＝formulaの長さが数値の個数＋演算子の個数になる）したらformulaは完成
    # なお演算子の個数は数値の個数-1
    if len(formula) == len (num_tuple) * 2 - 1:
        return [' '.join(formula)]
    else:
        rpn_list = []
        # opr_usedはnum_used以上の個数になることはできない
        if num_used <= opr_used + 1:
            rpn_list.extend(make_rpn_formula(num_tuple, num_used + 1, opr_used, formula + [num_tuple[num_used]]))
        else:
            # formulaには数値、演算子のいずれかを追加する
            if num_used < len(num_tuple):
                rpn_list.extend(make_rpn_formula(num_tuple, num_used + 1, opr_used, formula + [num_tuple[num_used]]))
            rpn_list.extend(make_rpn_formula(num_tuple, num_used, opr_used + 1, formula + ['+']))
            rpn_list.extend(make_rpn_formula(num_tuple, num_used, opr_used + 1, formula + ['-']))
            rpn_list.extend(make_rpn_formula(num_tuple, num_used, opr_used + 1, formula + ['*']))
            rpn_list.extend(make_rpn_formula(num_tuple, num_used, opr_used + 1, formula + ['/']))
    return rpn_list

num_list = list(itertools.permutations(range(1, 10), 4))
for i in range(len(num_list)):
    rpn_list = make_rpn_formula(num_list[i])
    for j in range(len(rpn_list)):
        if rpn(rpn_list[j]) == 10:
            print(rpn_list[j])
