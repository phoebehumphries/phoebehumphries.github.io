from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

# This is creating my form.
# Imported the module Flask_wTF, wtforms.
# Created each field I wanted to be on my contact form e.g. name, email, subject.
# Flask-WTF comes with built-in validators.


class ContactForm(Form):
    name = TextField("Name",  [validators.Required("Please enter your name.")])
    # The [validators.Required()] code is used to validate its presence in each form field.
    # The email one, uses the pattern of  user@example.com, to make sure the email is actually valid.
    # In each of these I have written the specific error I want to flash up if it doesn't validate.
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")
