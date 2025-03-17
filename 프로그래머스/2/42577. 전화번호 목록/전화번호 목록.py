def solution(phone_book):
    book = {}
    
    for phone in phone_book:
        book[phone] = 1
    
    for phone in phone_book:
        length = len(phone)
        for i in range(0, length):
            if phone[:i] in book:
                return False
    
    return True