from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def serveWebApp():
    dev_name = "Isabel"
    if request.method == "GET":
        return render_template("index.html", developer_name = dev_name)
    elif request.method == "POST":
        inputstr = request.form['number']
        num = convert(inputstr)
        if not num:
           return render_template("index.html", developer_name = dev_name, not_valid = True)
        return render_template("result.html", developer_name = dev_name, number_decimal = inputstr, number_roman = num)
    return "What happened?"


def validate_input(input):
    try:
        num = int(input)
        if not num or num < 1 or num >=  4000:
            return None
        return num

    except Exception:
        print("Something went wrong, try again!") 
        return None


# convert decimal number between 1 and 3999 to Roman number.
def convert(input):
    num = validate_input(input)
    if not num:
        return
    print(f"num is: {num}")
    decToRom = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
    result = ""
    for dec in decToRom: 
        times = num // dec
        num = num - (times * dec)
        if times > 0:                                     
            for i in range(times):
                result += decToRom[dec]        
    print(f"uncleaned result: {result}")
    # shorten result
    # Define the replacements in a dictionary
    replacements = {
        "DCCCC": "CM",
        "CCCC": "CD",
        "LXXXX": "XC",
        "XXXX": "XL",
        "VIIII": "IX",
        "IIII": "IV"
    }

    # Apply the replacements in a single loop
    for old, new in replacements.items():
        result = result.replace(old, new)
    return result


def main():

    try:
        # prompt user
        while (not num or num < 1 or num >=  4000):
            user_input = input("Please enter a decimal number between 1 and 3999 (inclusive).")
            num = int(user_input)
    except Exception:
        print("Something went wrong, try again!") 
    convert(num)
        



if __name__ == "__main__":
    main()       

   
