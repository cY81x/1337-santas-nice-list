from flask import Flask, render_template, jsonify, request, make_response
import subprocess, json
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route('/')
def nicelist():
    response = subprocess.check_output('./nicelist read', shell=True)
    data = json.loads(response)

    return render_template('nicelist.html', data=data)

@app.route('/api/scrolltext', methods=['GET'])
def get_scroll_text():
    cookie = request.cookies.get('user')

    if not cookie:
        cookie = 'lamer'

    result = subprocess.check_output('./nicelist check ' + cookie, shell=True)

    if b'Name found' in result:    
        scroll_text = "Ho Ho Ho! You thought I was just about sleighs and reindeer, didn't you? Well, think again! When I'm not delivering presents, I'm a wizard with code, a virtuoso of virtual security. My workshop is a fortress of firewalls and my elves are experts in encryption! I've got more tricks up my sleeve than toys in my sack. And you, my friend, have done something remarkable. You found the breadcrumbs I cleverly left in the digital snow. Not many can outsmart Santa's cyber setup, but you've shown exceptional skill. Welcome to my Nice List, a roster reserved for the best and brightest. Keep up the good work, and who knows? Maybe one day you'll be as legendary in the world of hacking as Santa is in the world of gift-giving. Merry Hacking!"
    else:
        scroll_text = "Ho ho ho! It's Santa here! I've checked my list and noticed you've been a bit naughty with your hacking skills this year. Remember, with great power comes great responsibility. Let's use those skills for good next year, and I'm sure you'll be back on the Nice List! Keep up the coding, and have a Merry Christmas!"

    # Create a response object
    response = make_response(jsonify({'scroll_text': scroll_text}))

    # Set cookie if not present
    if not request.cookies.get('user'):
        response.set_cookie('user', 'lamer', expires=datetime.now() + timedelta(days=1))

    return response

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=1337)
