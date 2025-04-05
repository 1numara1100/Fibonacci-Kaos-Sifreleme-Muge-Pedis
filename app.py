from flask import Flask, render_template, request, redirect, url_for 
import numpy as np

app = Flask(__name__)


def fibonacci(n, mod=256):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % mod
    return a


def logistic_map(x, r=3.99, iterations=50):
    for _ in range(iterations):
        x = r * x * (1 - x)
    return x


def encrypt(text, seed):
    try:
        byte_data = text.encode('utf-8')
        if len(byte_data) > 256:
            raise ValueError("Maksimum 256 bayt boyutunda veri girebilirsiniz! (Türkçe karakterler daha fazla yer kaplar)")
        encrypted = []
        for i, byte in enumerate(byte_data):
            chaotic_val = logistic_map(0.1 + (i + seed) / 1000)
            key = (fibonacci(seed + i) ^ int(chaotic_val * 255)) % 256
            encrypted.append(byte ^ key)
        return bytes(encrypted).hex()
    except UnicodeEncodeError:
        raise ValueError("Geçersiz karakter girdiniz!")


def decrypt(encrypted_hex, seed):
    try:
        encrypted_bytes = bytes.fromhex(encrypted_hex)
        decrypted_bytes = []
        for i, byte in enumerate(encrypted_bytes):
            chaotic_val = logistic_map(0.1 + (i + seed) / 1000)
            key = (fibonacci(seed + i) ^ int(chaotic_val * 255)) % 256
            decrypted_bytes.append(byte ^ key)
        return bytes(decrypted_bytes).decode('utf-8')
    except:
        return "Geçersiz şifreli mesaj!"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form.get('action')
        seed = int(request.form.get('seed', 42))

        if action == 'encrypt':
            text = request.form['text']
            try:
                encrypted = encrypt(text, seed)
                return redirect(url_for('result', encrypted=encrypted, action='encrypt'))
            except ValueError as e:
                return render_template('index.html', error=str(e))

        elif action == 'decrypt':
            encrypted_hex = request.form['encrypted']
            decrypted = decrypt(encrypted_hex, seed)
            return render_template('result.html', decrypted=decrypted, action='decrypt')

    return render_template('index.html')


@app.route('/result')
def result():
    encrypted = request.args.get('encrypted', '')
    action = request.args.get('action', '')
    return render_template('result.html', encrypted=encrypted, action=action)


if __name__ == '__main__':
    app.run(debug=True)
