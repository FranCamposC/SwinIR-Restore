import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template
import time
import shutil


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'testsets/RealSRSet+5images'
app.config['RESULT_FOLDER'] = '/results/swinir_real_sr_x4'

def limpiar_carpetas(carpetas):
    for carpeta in carpetas:
        if os.path.exists(carpeta):
            shutil.rmtree(carpeta)
        os.makedirs(carpeta) 


@app.route('/', methods=['GET', 'POST'])

def upload_file():
    carpetas = [
            'testsets/RealSRSet+5images', 
            'static/results/swinir_real_sr_x4'
            ]
    if request.method == 'POST':
        limpiar_carpetas(carpetas)
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            subprocess.run([
                'python', 'main_test_swinir.py',
                '--task', 'real_sr',
                '--scale', '4',
                '--model_path', 'model_zoo/swinir/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth',
                '--folder_lq', app.config['UPLOAD_FOLDER'],
                '--folder_gt', 'testsets/RealSRSet+5images',
                '--tile', '400'
            ], check=True)
            return redirect(url_for('uploaded_file', filename=file.filename))  
    return render_template('index.html')

@app.route('/show/<filename>')
def uploaded_file(filename):
    time.sleep(4) 
    processed_filename = filename.rsplit('.', 1)[0] + '_SwinIR.png'
    processed_filepath = os.path.join(app.config['RESULT_FOLDER'], processed_filename).replace('\\', '/')
    original_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
    return render_template('index.html', processed_image=processed_filepath, original_image=original_filepath)



if __name__ == "__main__":
    app.run(debug=True)
