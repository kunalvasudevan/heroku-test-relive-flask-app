import random
from flask import Flask, render_template, request
from flask import jsonify
from data import generate_DATA

# flask app instance
app = Flask(__name__)

# storing the data in a variable
final_data = generate_DATA()

# creating a url route for home page
@app.route('/')
def home_page():
    return render_template('home.html')

# url route for contact page
@app.route('/aboutus')
def contact_page():
    return render_template('aboutus.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

#
@app.route('/show_data')
def show_data_page():
    return render_template('show_data.html', data=final_data)


# repl run
# # to run the app via terminal
# if __name__ == "__main__":
#     app.run(
#             host='0.0.0.0',
#             port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
#             debug=True
#         )

# to run the app via terminal
if __name__ == "__main__":
    app.run(debug=True)
