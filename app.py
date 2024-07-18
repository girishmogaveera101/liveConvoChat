from flask import Flask, request, render_template, jsonify,redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['get','post'])
def index():
    return render_template('chat.html',messages={'msg':'nothing'})







@app.route('/sendMessage', methods=['post','get'])
def sendMessage():
    global msgs
    global message
    if request.method=='POST':
        message = request.form['message']
        print("\n\n\nEntered message : ",message)

        # writing the message to file
        file = open('topic1.txt','a')
        file.write(message+'\n')

        # checking no of lines means messages
        no_lines = 0
        lineFile = open('topic1.txt','r')
        data = lineFile.read()
        for ch in data:
            if ch == "\n":
                no_lines+=1
        print("total msg : ",no_lines)

        # now appending the messgaes to a list
        messages=[]
        readFile = open('topic1.txt','r')
        for line in readFile:
            line1=line.strip('\n')
            messages.append(line1)
        print("All messages : ",messages,"\n\n\n")
        msgs = []
        x = 0
        for x in range(no_lines):
            msg = {'msg': messages[x]}
            msgs.append(msg)

        return redirect(url_for('sendMessage',messages=msgs,fmsg=message))
    # msgs=request.args.get('msgs')
    # message=request.args.get('message')
    return render_template('chat.html',messages=msgs,fmsg=message)

if __name__ == "__main__":
    app.run(debug=True,port=5001)