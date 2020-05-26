

#讀取檔案
def read_file(filename):
    lines = []
    with open(filename , 'r', encoding = 'utf-8-sig') as f:  #utf-8-sig去掉檔案開頭\ufeff符號
        for line in f:
            lines.append(line.strip())
    return lines

#轉換清單
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:  #person預設為none ，if person意思為若person有值
            new.append(person + ': ' + line)
    return new

def write_file(filename,lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines) 
    write_file('output.txt', lines)

main() 