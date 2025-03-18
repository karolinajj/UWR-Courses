import string

output = open("pan_tadeusz_lowercase.txt", "wb")

with open("pan_tadeusz.txt", "rb") as tadeusz:
    for line in tadeusz:
        line = line.decode("utf-8")
        line = line.strip()
        line = line.strip('\n')
        line = line.strip('\t')
        line = line.strip('\r')
        line = line.replace('—', '')
        line = line.replace('  ', ' ')
        line = line.replace('…', '')
        line = line.replace('«', '')
        line = line.replace('»', '')

        line = line.lower()

        for char in string.punctuation:
            line = line.replace(char, '')

        output.write(line.encode("utf-8"))
        if(line != ""): output.write("\n".encode("utf-8"))

output.close()