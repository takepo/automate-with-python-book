def spam():
    global eggs
    eggs = 'spam' # グローバル変数

def bacon():
    eggs = 'bacon' # ローカル変数

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
