from flask import Flask, render_template, request

app = Flask(__name__)

def sum_limit(number):
    while number >= 107:
        digits = [int(d) for d in str(number)]
        n = len(digits)
        new_sum = 0
        new_digits =[]

       
        for i in range((n + 1) // 2): 
            if i != (n-i-1):
                new_digits.append(digits[i] + digits[n - i - 1])
            else:
                new_digits.append(digits[i])
         
        number = int(''.join(map(str,new_digits)))

    return number

def love_percentage(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    combined_name = name1 + name2 + 'love'
    number = ''
    
    for i in combined_name:
        cnt = combined_name.count(i)
        number = number + str(cnt)
        combined_name = combined_name.replace(i,'')
    number = int(number.replace('0',''))
        
    return sum_limit(number)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':    
        name1 = request.form['name1']
        name2 = request.form['name2']
        result = love_percentage(name1, name2)
        return render_template('index.html', result=result, name1=name1, name2=name2)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)



