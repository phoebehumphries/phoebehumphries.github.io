from flask import Flask
from flask import render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail


# importing flask
# Request determines whether the current HTTP method is a GET or a POST.
# importing other modules, mostly for the form to work e.g. flask_mail and making sure it can read my other py app.

mail = Mail()

app = Flask(__name__)

# An attacker could create a form on their own website,
# fill it in with malicious information, and submit it to my server.
# This sets a key so that the form submission originates from my web app.
# I created a unique token hidden inside the HTML <form> tag that cannot be guessed by anyone
# Set up Flask-WTF with a secret key, and Flask-WTF takes care of generating and managing unique tokens for your forms.

app.secret_key = 'foxisveryspooky911'

# I use the Message class to compose a new email and the Mail class to send the email.
# I used Gmail's SMTP server settings as that's the easiest to create an account for and use overall.


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
# Here is the actual set up for my email account for my website. I set up an Gmail address for it.
# For the username, I used my actual email for the site.
# For the password, I used the actual email password.
# This means it will be able to log in to the email and send me the data that's filled in on the website.
app.config["MAIL_USERNAME"] = 'phoebehumphrieswebsite@gmail.com'
app.config["MAIL_PASSWORD"] = 'websitepassword123'

mail.init_app(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    # Now when someone visits the URL /contact, the function contact() will execute.

    if request.method == 'POST':
        # If its a POST request, a function will capture the form field data and check if it's valid.
        # if a GET request is sent to the server, the web page containing the form is retrieved and loaded.
        if form.validate() == False:
            flash('All fields are required.')
            # If the form validation fails, then this code will run. This sets it so when its false,
            # it will flash an error code, telling the user that they need to fill out every field correctly.
            return render_template('contact.html', form=form)
        else:
            # This will only send an email if the form has been submitted and all validation checks pass.
            # The Message class takes a subject line, a "from" address, and a "to" address.
            # The form.subject.data is now set as the new message's subject line.
            # The email is sent from the account I created e.g. phoebehumphrieswebsite@gmail.com.
            # This email is then sent to another email address, which I have set as the same address (as its easier).
            # You can change this piece of code to check if it does receive to a personal account e.g.
            # recipients=['phoebehumphrieswebsite@gmail.com']
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['phoebehumphrieswebsite@gmail.com'])
            msg.body = """
      From: %s 
      
        
      Message: %s  
      
      
      
      Email From: %s
      """ % (form.name.data, form.message.data, form.email.data)
            mail.send(msg)

            # I use pythons % to format the email.
            # Then I use mail.send(msg) to send the email.

            return render_template('contact.html', success=True)
        # The success=True, tells the contact.html page that everything was successful and to show the if success page.

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.route('/')
def base():
    return render_template('home.html')
# Setting up the route for the homepage, having it go to the home.html page.
# Set up each episode page for the website.


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/videos')
def videos():
    return render_template('videos.html')


@app.route('/tour')
def tour():
    return render_template('tour.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/biography')
def biography():
    return render_template('biography.html')


if __name__ == '__main__':
    app.run(debug=True)



