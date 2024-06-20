from flask import Response
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
import os
import cv2
import numpy as np
import pickle
import dlib
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import datetime

from ..models import Funcionario, Fotos
from .. import app, db

predictor_path = "shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"

def load_images_from_folder():
    images = []
    labels = []
    label_dict = {}
    current_label = 1
    for person_name in os.listdir('dataset'):
        funcionario = Funcionario(nome=person_name, setores='1,2')
        db.session.add(funcionario)
        db.session.commit()
        person_folder = os.path.join('dataset', person_name)
        if os.path.isdir(person_folder):
            for filename in os.listdir(person_folder):
                print(f"[INFO] Carregando {filename}...")
                img_path = os.path.join(person_folder, filename)
                img = cv2.imread(img_path)
                is_success, buffer = cv2.imencode('.jpg', img)
                if is_success:
                    with app.app_context():
                        foto = Fotos(id_funcionario=current_label, data=buffer.tobytes())
                        db.session.add(foto)
                        db.session.commit()
        current_label += 1

def load_images_from_database():
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(predictor_path)
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)

    images = []
    labels = []
    label_dict = {}
    current_label = 0
    for funcionario in Funcionario.query.all():
        fotos = Fotos.query.filter(Fotos.id_funcionario == funcionario.id).all()
        label_dict[current_label] = funcionario.nome
        for foto in fotos:
            img = cv2.imdecode(np.frombuffer(foto.data, np.uint8), -1)
            # img = cv2.resize(img, (256, 256))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            rects = detector(gray, 1)
            for rect in rects:
                shape = sp(gray, rect)
                face_descriptor = facerec.compute_face_descriptor(img, shape)
                images.append(face_descriptor)
                labels.append(current_label)
        current_label += 1
    return np.array(images), np.array(labels), label_dict

def train_model(images, labels, label_dict):
    if len(set(labels)) < 2:
        print("[ERRO] O número de classes tem que ser maior que um para treinar o modelo.")
        return None, None, None

    print("[INFO] Treinando o modelo SVM...")
    
    start_time = datetime.datetime.now()
    
    le = LabelEncoder()
    le.fit([label_dict[key] for key in label_dict.keys()])
    encoded_labels = le.transform([label_dict[label] for label in labels])

    clf = SVC(C=1.0, kernel='linear', probability=True)
    clf.fit(images, encoded_labels)

    model_path = 'face_recognition_model.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump((clf, label_dict, le), f)

    end_time = datetime.datetime.now()
    print(f"[INFO] Treinamento concluído. Modelo salvo em 'face_recognition_model.pkl'. Tempo total: {end_time - start_time}")

    return clf, label_dict, le

@app.route('/carregar_dataset')
def carregar_dataset():
    load_images_from_folder()
    return Response(status=200)

@app.route('/treinar_modelo')
def treinar_modelo():
    images, labels, label_dict = load_images_from_database()
    model = train_model(images, labels, label_dict)
    return Response(status=200)

