# Try working with 3 variables

def count_photos(road):
    
    right= 0
    left = 0
    period = 0
    count = 0

    for i in road:
        if i == '>':
            right += 1
        elif i =='<':
            left += 1
            count += period
        elif i == '.':
            count += right
            period += 1

    return count
