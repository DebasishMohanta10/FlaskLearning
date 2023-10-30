from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField,TextAreaField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    description = TextAreaField("Description",validators=[DataRequired()])
    deadline = DateField("Deadline")
    submit = SubmitField("Add Task")
    