with open('source\so.txt','r')as file:
          content=file.read()
          t=content.count(str)
with open('destination\st.txt','w')as f:
        f.write(content)

def count_text_file(file_path):
    with open (file_path,'r') as file:
        lines=file.readline()
        line_count-len(lines)
        word_count=sum(len(line.split()) for line in lines)
        char_count -sum(len(line) for line in lines)
    return line_count, word_count, char_count

file_path = 'example.txt'
lines,words, characeter =count_text_file(file_path)
print(f'Lines: {line}, Words: {words}, characters: {characters}        