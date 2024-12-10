def quine():
    code = 'def quine():\n    code = {!r}\n    print(code.format(code))\nquine()'
    print(code.format(code))

quine()
