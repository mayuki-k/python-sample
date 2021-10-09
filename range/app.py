datas = ['弁当', 'トースト', '牛乳', '解凍', '惣菜']

def main():
    setting_num = 0
    time_num = 0

    print('数字を入力してください')
    show_str = ''
    for i in range(len(datas)):
        show_str += f'{i} {datas[i]}'
    print(show_str)

    while(True):
        setting_num_str = input()
        if validate_number(setting_num_str, 0, 4):
            continue
        setting_num = int(setting_num_str)
        break
    
    while(True)
        print('時間を入力してください。')
        time_str = input()
        if validate_number(time_str, 0, 10):
            continue
        time_num = int(time_str)
        break

        print(f'{datas[setting_num]}を{time_num}分レンジでチンします。')

def validate_number(num_str, start, end):
    if not setting_num_str.isdigit():
        print('これは数字ではありません。')
        return False
    
    setting_num = int(setting_num_str)
    if setting_num < start or setting_num > end:
        print('数字の範囲外です。')
        return False
    return True





    



    

    



main()
