all_guestes = {
    'アリス': {'リンゴ': 5, 'プレッツェル': 12},
    'ボブ': {'ハムサンド': 3, 'リンゴ': 2},
    'キャロル': {'コップ': 3, 'アップルパイ': 1},
}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print('持ち物の数')
print('- リンゴ' + str(total_brought(all_guestes, 'リンゴ')))
print('- コップ' + str(total_brought(all_guestes, 'コップ')))
print('- ケーキ' + str(total_brought(all_guestes, 'ケーキ')))
print('- ハムサンド' + str(total_brought(all_guestes, 'ハムサンド')))
print('- アップルパイ' + str(total_brought(all_guestes, 'アップルパイ')))
