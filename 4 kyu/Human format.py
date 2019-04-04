def format_duration(seconds):
    s = formatting(seconds%60, 'second')
    m = formatting(seconds//60%60, 'minute')
    h = formatting(seconds//3600%24, 'hour')
    d = formatting(seconds//(3600*24)%365, 'day')
    y = formatting(seconds//(3600*24*365), 'year')
    res = [i for i in (y, d, h, m, s) if i]
    if len(res) >= 2:
        return rem if not res else ', '.join(res) + ', ' + rem
    elif len(res) == 1:
        return res[0]
    else:
        return 'now'


def formatting(s, period):
    if s >= 2:
        return '%d %ss' %(s, period)
    elif s == 1:
        return '1 ' + period
    else:
        return ''

print(format_duration(1234))
print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))
print(format_duration(111117262))