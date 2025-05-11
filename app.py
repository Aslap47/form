from flask import Flask, request, render_template

app = Flask(__name__)

# Formu gösterecek route
@app.route('/')
def form():
    return render_template('form.html')  # templates/form.html dosyasını yükler

# Formdan gelen veriyi alacak route
@app.route('/submit', methods=['POST'])
def submit_data():
    username = request.form.get('username')  # Kullanıcı adını al
    password = request.form.get('password')  # Şifreyi al

    # Gelen verileri terminalde yazdır
    print(f"Kullanıcı Adı: {username}")
    print(f"Şifre: {password}")

    # Kullanıcıya bir yanıt gönder
    return f"Kullanıcı Adı: {username}, Şifre: {password}"

if __name__ == '__main__':
    app.run(debug=True)