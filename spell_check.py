#!/usr/bin/env python
# -*- coding:utf-8 -*-

def lev_distance(text1, text2):
    arr = dict()
    for i in range(0, len(text1) + 1):
        arr[i] = dict()
        arr[i][0] = i
    for j in range(0, len(text2) + 1):
        arr[0][j] = j
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            equal = 0 if text1[i-1] == text2[j-1] else 1
            arr[i][j] = min(
                    arr[i-1][j] + 1,
                    arr[i][j-1] + 1,
                    arr[i-1][j-1] + equal)
    return arr[len(text1)][len(text2)]

NUMBER_OF_OPERATIONS = 1

def search_corrections(dictionary, words):
    for word in words:
        result_list = []
        is_correct = False
        for correction in dictionary:
            distance = lev_distance(word, correction)
            if distance == 0:
                print '%s is correct' % word
                is_correct = True
                break
            if distance == NUMBER_OF_OPERATIONS:
                result_list.append(correction)
        if not is_correct:
            print '%s: %s' % (word, ', '.join(result_list))

def get_input():
    import sys

    filename = sys.argv[1]
    file_input = open(filename, 'r')
    dictionary, words, dummy = file_input.read().strip().split('#')
    file_input.close()
    return (
        dictionary.strip('\n').split('\n'),
        words.strip('\n').split('\n')
    )

if __name__ == '__main__':
    search_corrections(*get_input())
