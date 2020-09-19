from flask import Flask, render_template, url_for, request, redirect
import csv
#render_template imports a template for us

app = Flask(__name__)
#__name__ = __main__  coz is the main file we are currently running
#@app.route('/<username>/<int:post_id>')

# if we type /<>, flask understand this as a parameter we can include in the function
# Decorator: High level of abstraction, it gives us extra functionality
# for the def function we just created. This is saying everytime we request the endpoint
# (i.e, ask for the url) and we add the '/' it should open there the def function!
#def hello_world(username=None, post_id = None):
#	return render_template('index.html',name=username, post_id = post_id)


@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')

def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]

		file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST','GET'])
#get: send info, post: browser wants to send info

def login():
	if request.method =="POST":
		data = request.form.to_dict()
		write_to_csv(data)
		#we redirect to another webpage
		return redirect('/thankyou.html')
	else:
		return 'something went wrong'


