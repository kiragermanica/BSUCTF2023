#!/usr/bin/python3

if __name__=="__main__":
    string = '110110111000101011101010100001111000010000011101010100100010111111010011011001101111100100111010011111110001010'
    bin2letter = {
        '000':'s',
        '00100':'g',
        '00101':'y',
        '0011':'i',
        '0100':'h',
        '0101':'t',
        '0110':'l',
        '01110':'v',
        '01111':'r',
        '10':'e',
        '1100':'n',
        '1101':'w',
        '111':'_'
        }

    flag = 'bsuctf{'
    while string:
        for key in bin2letter:
            if string.startswith(key):
                flag += bin2letter[key]
                string = string[len(key):]
                break

    flag += '}'
    print(flag)
