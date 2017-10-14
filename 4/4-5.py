import random
messages = [
    '確かにそうだ',
    '間違いなくそうだ',
    'はい',
    'なんとも。もういちどやってみて',
    '集中してもう一度きいてみて',
    '私の答えはノーです',
    '見通しはそれほど良くない',
    'とても疑わしい',
]

print(messages[random.randint(0, len(messages) -1)])
