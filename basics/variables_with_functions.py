globalVariable = "Im am Global"

def myFunc():
    global localVanewGlobalVariableriable # global forced state
    newGlobalVariable = "Im not Local variable, statement with global variable"

    localVariable = "Im local variable :)"

    print(localVariable)
    print(globalVariable)
    print(newGlobalVariable)

myFunc()
