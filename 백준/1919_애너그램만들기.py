from string import ascii_lowercase

if __name__ == '__main__':
    text1 = input()
    text2 = input()
    print(sum(abs(text1.count(ascii_lowercase[i])-text2.count(ascii_lowercase[i])) for i in range(0,26)))
