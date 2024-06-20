from flask import Flask, Response, request, redirect
from imutils import face_utils
import cv2
import dlib
import numpy as np
import tensorflow as tf
import pickle

from ..models import Funcionario, Fotos
from .. import app, db

count = 0

predictor_path = "shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"

def load_trained_model():
    with open('face_recognition_model.pkl', 'rb') as f:
        clf, label_dict, le = pickle.load(f)
    return clf, label_dict, le

def gen_buffer_camera(model, facerec, le, detector, sp, ret, frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for rect in rects:
        shape = sp(gray, rect)
        face_descriptor = facerec.compute_face_descriptor(frame, shape)
        face_descriptor = np.array(face_descriptor).reshape(1, -1)
        prediction = model.predict(face_descriptor)
        proba = model.predict_proba(face_descriptor)
        confidence = np.max(proba)
        name = le.inverse_transform(prediction)[0] if confidence > 0.5 else 'Unknown'
        name = str(name)  # Certifique-se de que o nome é uma string
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        # Definir a cor da borda com base no conteúdo do nome
        if 'Funcionario' in name:
            color = (0, 255, 0)  # Verde para Funcionario
        elif 'Fora da Lei' in name:
            color = (0, 0, 255)  # Vermelho para Fora da Lei
        else:
            color = (255, 0, 0)  # Azul para Tudo
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    ret, buffer = cv2.imencode('.jpg', frame)
    return buffer

def gen_buffer_camera_unavaible():
    placeholder_frame = np.ones((480, 640, 3), dtype=np.uint8) * 255
    cv2.putText(placeholder_frame, 'Camera nao disponivel', (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    ret, buffer = cv2.imencode('.jpg', placeholder_frame)
    return buffer

def gen_frames_reconhecimento(model, label_dict, le, camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(predictor_path)
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)

    while True:
        if cap is None or not cap.isOpened():
            buffer = gen_buffer_camera_unavaible()
        else:
            ret, frame = cap.read()
            if not ret:
                break
            buffer = gen_buffer_camera(model, facerec, le, detector, sp, ret, frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def capturar_frame(frame, id_funcionario):
    global count
    is_success, buffer = cv2.imencode('.jpg', frame)
    if is_success:
        with app.app_context():
            foto = Fotos(id_funcionario=id_funcionario, data=buffer.tobytes())
            db.session.add(foto)
            db.session.commit()
        count += 1

def gen_frames(camera_index, capturar, id_funcionario):
    cap = cv2.VideoCapture(camera_index)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if capturar == 1 and count < 20: 
            capturar_frame(frame, id_funcionario)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

@app.route('/video_feed/funcionario/<id_funcionario>')
def vide_feed(id_funcionario):
    global count 
    camera_id = int(request.args.get('camera_id', 0))
    capturar = int(request.args.get('capturar', 0))
    if count == 19:
        count+=1
        return redirect(f'/video_feed/funcionario/{id_funcionario}?camera_id={camera_id}&capturar=0')
    if count == 20:
        count = 0
    return Response(gen_frames(int(camera_id), capturar, id_funcionario), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed/reconhecimento')
def video_feed_reconhecimento():
    camera_id = request.args.get('camera_id')

    model, label_dict, le = load_trained_model()
    return Response(gen_frames_reconhecimento(model, label_dict, le, int(camera_id)), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

