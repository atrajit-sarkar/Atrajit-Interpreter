import maths

operations={'+':maths.add,'-':maths.subtract,'*':maths.multiply,'/':maths.divide,'**':maths.pow,'//':maths.floor,'%':maths.modulo}           
# Show Fucntion is used to give console output............
def show(line):
    i=len('show >>')
    try:
        while True:
            print(line[i+1],end="")
            i+=1
            if i>(len(line)-2):
                break
        return 0
    except:
        print("")
        return 1
    
def var(line):
    try:
        dictionary={}
        line=line.split(">>")[1].strip()
        line=line.split("=")
        line1=line[0].split(" ")
        if line1[0]=='int':
            dictionary[line1[1]]=int(line[1])
        elif line1[0]=='float':
            dictionary[line1[1]]=float(line[1])

        return dictionary
    except:
        print("Check syntax....")
        return 1
    
def calculate(line,dictionary):
    listofOperators=['+','-','*','/','//','**','%']
    line=line.split(">>")[1].strip()
    for operator in listofOperators:
        if operator in line:
            line=line.split(operator)
            try:
                v=operations[operator](dictionary[line[0]],dictionary[line[1]])
                return v
            except:
                try:
                    if line[0].isdigit():
                        if line[1].isdigit():
                            v=operations[operator](int(line[0]),int(line[1]))
                        else:
                            v=operations[operator](int(line[0]),float(line[1]))
                    else:
                        if line[1].isdigit():
                            v=operations[operator](float(line[0]),int(line[1]))
                        else:
                            v=operations[operator](float(line[0]),float(line[1]))
                    return v
                except:
                    print("Check Syntax while using Calculate >>")
                    break

        
        