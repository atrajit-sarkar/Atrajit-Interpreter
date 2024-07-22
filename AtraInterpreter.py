import sys
import stdio

dictionary={}
if len(sys.argv)!=2:
    print("Check syntax")
else:
    if sys.argv[1].endswith(".atra"):
        with open(sys.argv[1],"r",encoding='UTF-8') as f:
            lines=f.readlines()
            # print(lines)
        for line in lines:
            if 'show >>' in line:
                stdio.show(line=line)
            elif 'var >>' in line:
                temp_dictionary=stdio.var(line=line)
                dictionary.update(temp_dictionary)
            elif 'calculate >>' in line:
                v=stdio.calculate(line=line,dictionary=dictionary) 
                print(f"{v}")   
                

    else:
        print("File extension not recognised......")    