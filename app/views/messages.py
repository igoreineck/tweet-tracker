from flask import Blueprint, render_template


messages = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

@messages.route('/messages')
def index():
    fake_messages = [
        {
            'name': 'John 1'
        },
        {
            'name': 'John 2'
        },
        {
            'name': 'John 3'
        }
    ]
    return render_template('messages/index.html', data=fake_messages)