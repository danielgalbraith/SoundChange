import numpy

with open("input.txt", "r") as input, open("output.txt", 'w') as output:
    list_of_lines = input.readlines()
    newlines = []
    for line in list_of_lines:
        curline = line.strip('\n')
        charlist = []
        for i in range(0,len(curline)):
            charlist.append(line[i])
        syl = ""
        syllist = []
        for j in range(0,len(charlist)):
            if charlist[j] != '.':
                syl += charlist[j]
            else:
                syllist.append(syl)
                syl = ""
        print(syllist)
        # Specify sound change rules here:
        for k in range(0,len(syllist)):
            # p$ or t$ or k$ > V: / everywhere
            if syllist[k][len(syllist[k])-1] == 'p' or syllist[k][len(syllist[k])-1] == 't' or syllist[k][len(syllist[k])-1] == 'k':
                if len(syllist[k]) < 3:
                    syllist[k] = syllist[k][0] + ":"
                else:
                    syllist[k] = syllist[k][:len(syllist)-1] + ":"
            # f.. > v.. / everywhere
            if syllist[k][0] == 'f':
                syllist[k] = 'v' + syllist[k][1:]
            elif k == 1:
                # p,, > f.. / stressed syl
                if syllist[k][0] == 'p':
                    syllist[k] = 'f' + syllist[k][1:]
                # k,, > kh.. / stressed syl
                if syllist[k][0] == 'k':
                    syllist[k] = 'kh' + syllist[k][1:]
                # c,, > ts.. / stressed syl
                if syllist[k][0] == 'c':
                    syllist[k] = 'ts' + syllist[k][1:]
                # x,, > s.. / stressed syl
                if syllist[k][0] == 'x':
                    syllist[k] = 's' + syllist[k][1:]
            else:
                continue
        print(syllist)
        newlines.append(syllist)
    print(newlines)
    for i in range(0,len(newlines)):
        newlines[i] = "" + newlines[i][0] + "." + newlines[i][1] + "." + newlines[i][2] + "."
        word = newlines[i]
        output.write(word)
        output.write('\n')
    print(newlines)

