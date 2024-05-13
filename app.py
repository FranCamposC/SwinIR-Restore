import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template
import time
import shutil
from datetime import datetime, timedelta


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
    processing_time = None

    if request.method == 'POST':
        limpiar_carpetas(carpetas)
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Iniciar el cronómetro
            start_time = datetime.now()

            subprocess.run([
                'python', 'main_test_swinir.py',
                '--task', 'real_sr',
                '--scale', '4',
                '--model_path', 'model_zoo/swinir/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth',
                '--folder_lq', app.config['UPLOAD_FOLDER'],
                '--folder_gt', 'testsets/RealSRSet+5images',
                '--tile', '400'
            ], check=True)

            # Terminar el cronómetro
            end_time = datetime.now()
            processing_time = round((end_time - start_time).total_seconds(),2)

            return redirect(url_for('uploaded_file', filename=file.filename, time=processing_time))
    return render_template('index.html', processing_time=processing_time)

@app.route('/show/<filename>')
def uploaded_file(filename):
    time.sleep(4) 
    processed_filename = filename.rsplit('.', 1)[0] + '_SwinIR.png'
    processed_filepath = os.path.join(app.config['RESULT_FOLDER'], processed_filename).replace('\\', '/')
    original_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/')
    processing_time = request.args.get('time', None)
    return render_template('index.html', processed_image=processed_filepath, original_image=original_filepath, processing_time=processing_time)



if __name__ == "__main__":
    app.run(debug=True)
