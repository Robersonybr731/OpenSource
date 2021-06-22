from flask import Flask, render_template, Response,request
import cv2
import cognitive_face as CF
app = Flask(__name__)

# record attributes
informations={}


def detectEmotion():
    # set default picture
    oldface = CF.face.detect('./babyface.jpg', False, False, 'emotion')
    # set up the url of th e group picture
    attributes = {'emotion,age,Gender,Glasses,Hair'}

    print("Face emotion detecting")
    faces = CF.face.detect('./bbface.jpg', False, False, attributes)
    # check detected
    if (not bool(faces)):
        return oldface[0]
    return faces[0]

def gen_frames():
    global informations
    # Set Camera and Windows Azure API
    camera=cv2.VideoCapture(0)
    KEY = '314cbf094b584c6a8590e3e78df6cbc2'
    CF.Key.set(KEY)
    BASE_URL = 'https://opensource1071526.cognitiveservices.azure.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    i = 0
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            # draw image rectangle
            # 轉成灰階
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 偵測臉部
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            # 繪製人臉部份的方框
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            face = 0
            # write picture
            cv2.imwrite('./bbface.jpg', frame)
            if i % 100 == 0:
                face = detectEmotion()
                if face != 0:
                    # update informations value
                    informations = face['faceAttributes']
                    face = face['faceAttributes']
                    print(informations)
                i=0
            i += 1
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)

            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
    camera.release()
    cv2.destroyAllWindows()

@app.route('/',methods=['POST','GET'])
def index():
    global informations

    # form request
    if request.method == 'POST':
        if request.values['send'] == '人物偵測':
            genders=''
            ages=''
            emotions=''
            hairs=''
            if 'gender' in informations:
                genders=informations['gender']
            else:
                genders='none'
            if 'age' in informations:
                ages=str(informations['age'])
            else:
                ages=0
            if 'hair' in informations:
                if len(informations['hair']['hairColor'])!=0:
                    hairs=str(informations['hair']['hairColor'][0]['color'])
                else:
                    hairs='black'
            else:
                hairs='none'
            emotions='none'
            emo=0
            # check which emotion confidence is higher
            if 'emotion' in informations:
                for i in informations['emotion']:
                    print(i,float(informations['emotion'][i]))
                    if emo<float(informations['emotion'][i]):
                        emo=float(informations['emotion'][i])
                        emotions=i
            return render_template('stream.html', gender=genders,ages=ages,hairs=hairs,emotions=emotions)
    # initial no value
    return render_template('stream.html',gender="None",ages="None",hairs="None",emotions="None")


@app.route('/video_feed')
def video_feed():
    # generate frame
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    app.run(port=8000, debug=True)
