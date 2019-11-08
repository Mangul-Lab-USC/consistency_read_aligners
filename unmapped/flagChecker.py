flagList = open("tool_flag.txt", "r")
report = open("flagReport.csv", "w").close()
report = open("flagReport.csv", "w+")
tools = flagList.readlines()
flagList.close()
allFlags = []
singleFlag = []
print(tools)
for line in tools:
    flags = line.split(",")
    for i in range(1, len(flags)):
        allFlags.append(flags[i].replace("\n",""))
print(allFlags)
print(singleFlag)
for flag in allFlags:
    if flag in singleFlag:
        continue
    else:
        singleFlag.append(flag)
print(allFlags)
print(singleFlag)
report.write("Flag,Count\n")
for flag in singleFlag:
    num = allFlags.count(flag)
    report.write("%s,%d\n" % (flag, num))
print(allFlags)
print(singleFlag)
report.close()






