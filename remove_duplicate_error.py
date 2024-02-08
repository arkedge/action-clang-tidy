import sys

file = sys.argv[1]
cc_cmd = sys.argv[2]    # it will be clang-tidy absolute path

with open(file) as f:
    s = f.read()

    # skip until the first compile log
    print(s[:s.find(cc_cmd)], end="")
    s = s[s.find(cc_cmd):]

    log = s.split(cc_cmd) # error or warning log per file
    if "" in log:
        log.remove("")
    # print(log)

    errors = []
    for l in log:  # noqa: E741
        (cmd, err) = l.split("\n", 1)
        if err in errors:
            #print("duplicate: " + cmd, file=sys.stderr)
            pass
        else:
            errors.append(err)
            print("CC" + l, end="")
