def detect(stream, needed_length):
    group, count = '', 0
    for character in stream:
        count += 1
        if character not in group:
            group += character
            if len(group) == needed_length: 
                return count
            continue
        ind = group.rfind(character)
        group = group[ind+1::] + character
    return 'No Packet of Needed Length'