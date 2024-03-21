from flask import Flask, render_template, request
from hymnal import hymn
from functions import InputSong

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/songs', methods=['GET', 'POST'])
def song_sheet():
    try:
        if request.method == 'POST':
            req = request.form['song'].lower()

            sheet = hymn['song'][req]
            main_image = hymn['song'][req]['chord_image']
            
            return render_template('song_sheet.html', ts=sheet, img=main_image)
    except:
        return render_template('error_found.html', er=req)


@app.route('/change_tone', methods=['POST'])
def change_tones():
    try:
        if request.method == 'POST':
            song_name = request.form['song_name_id']
            song_tone = request.form['song_tone_id']
            tone_selected = request.form['tones']

            sheet = hymn['song'][song_name.lower()]
            change_process = InputSong.inputs(song_name, tone_selected)

            message = [song_name, song_tone, tone_selected]
            

       
            return render_template('change_tone.html', msg=list(message), chp=change_process, ts=sheet)

    except:
        message = "Change not detected"

        return render_template('change_tone.html', msg=message)

if __name__ == '__main__':
    app.run(debug=True)