from flask import Flask, send_file, request, render_template
import os
import qrcode
from gtts import gTTS as GT

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/developer", methods=['GET', 'POST'])
def Developer():
    return render_template('developer.html')


@app.route("/qr_code", methods=['GET', 'POST'])
def QR_CODE():
    if request.method == 'POST':
        QRC = request.form['QR_data']
        print(QRC)
        img = qrcode.make(QRC)
        try:
            os.remove("ProtanHalder_QR_image.png")
        except:
            pass
        finally:
            img.save('ProtanHalder_QR_image.png')
    return render_template('TextToQR.html')


@app.route("/audio_maker", methods=['GET', 'POST'])
def AUDIO_MKR():
    if request.method == 'POST':
        Audio_Data = request.form['AUDIO_data']
        print(Audio_Data)
        Audio = GT(str(Audio_Data))
        try:
            os.remove("ProtanHalder_Text_To_Audo.mp3")
            print("remove audo")
        except:
            pass
        finally:
            Audio.save("ProtanHalder_Text_To_Audo.mp3")
    return render_template('TextToAudio.html')


@app.route("/qr_download", methods=['GET', 'POST'])
def download_qr_file():
    p = "ProtanHalder_QR_image.png"
    return send_file(p, as_attachment=True)


@app.route("/audio_download", methods=['GET', 'POST'])
def download_audio_file():
    p = "ProtanHalder_Text_To_Audo.mp3"
    try:
        return send_file(p, as_attachment=True)
    except:
        pass


if __name__ == "__main__":
    app.run(debug=True)