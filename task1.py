a = int(input())
mins_start = 510 + (a - 1) * 55
mins_end = 555 + (a - 1) * 55
minutes_s = str(mins_start % 60)
minutes_e = str(mins_end % 60)

if len(minutes_e) < 2:
    minutes_e = '0' + minutes_e

if len(minutes_s) < 2:
    minutes_s = '0' + minutes_s

print('Начало: ' + str(mins_start // 60) +':' + minutes_s, 'Конец: ' + str(mins_end // 60) +':' + minutes_e)