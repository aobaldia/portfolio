from flask import Flask, render_template, request, redirect, url_for
import csv 

app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')
    #return 'Hello, Alfredo-s World!'

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
    #return 'Hello, Alfredo-s World!'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        #message = request.form['message']  #para traer campo por campo
        data = request.form.to_dict() #to_dict() permite traer todo lo que esta en el formulario y guardarlo en un diccionario
        #print(data)
        write_to_csv(data)
        return redirect('/thankyou.html') #'Form submitted succesfully'
    else:
        return 'something went wrong.  Try again'
    

    #reurn 'form submitted succesfully' 

# @app.route('/')
# def home_page():
#     return render_template('index.html')
#     #return 'Hello, Alfredo-s World!'

# @app.route('/index.html')
# def index_page():
#     return render_template('index.html')

# @app.route('/works.html')
# def works_page():
#     return render_template('works.html')
    
# @app.route('/about.html')
# def about_page():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components_page():
#     return render_template('components.html')

# @app.route('/<username>/<string:cedula>')
# def userpage(username=None, cedula=None):
#     return render_template('index.html', name=username, cedula=cedula)
#     #return 'Hello, Alfredo-s World!'

# @app.route('/about.html')
# def aboutpage():
#     return render_template('about.html')
#     #return 'Hello, Alfredo-s World!'

# @app.route('/blog')
# def blog():
#     return 'Hello, this Alfredo-s Blog'

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'Hello, this Alfredo-s dogs Blog'