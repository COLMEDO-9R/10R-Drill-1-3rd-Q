# conditional statements in python
from pyscript import display, document

def check_result(e):
    gwa = float(document.getElementById('gwa').value)  # get user's GWA

    if gwa >= 75:  # if statement
        display("PASSED", target="output")
    else:
        display("FAILED", target="output")
