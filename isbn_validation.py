#!/usr/bin/env python
# =*- coding:utf-8 -*-

def validate_ISBN(probable_isbn):
    isbn = probable_isbn.replace('-', '')

    if len(isbn) > 10:
        print '%s is incorrect' % probable_isbn
        return

    result = [0]
    try:
        for i in range(0, len(isbn)):
            if i == 0:
                result[i] = int(isbn[i])
            else:
                number = int(isbn[i].lower().replace('x', '10'))
                result.append(result[i-1] + number)
        for i in range(1, len(result)):
                result[i] = result[i-1] + result[i]
    except ValueError:
        print '%s is incorrect' % probable_isbn
    if result[len(isbn) - 1] % 11 == 0:
        print '%s is correct' % probable_isbn
    else:
        print '%s is incorrect' % probable_isbn

def get_isbns():
    import sys

    filename = sys.argv[1]
    file_input = open(filename, 'r')
    isbns = file_input.read().strip().split('\n')
    isbns = [isbn.strip() for isbn in isbns]
    file_input.close()
    return isbns

if __name__ == '__main__':
    for isbn in get_isbns():
        validate_ISBN(isbn)
