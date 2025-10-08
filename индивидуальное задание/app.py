from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        print("POST получен")  # для отладки в консоли
        file = request.files.get("file")
        word = request.form.get("word")
        if file and word:
            text = file.read().decode("utf-8", errors="ignore")
            count = text.lower().count(word.lower())
            positions = []
            start = 0
            while True:
                pos = text.lower().find(word.lower(), start)
                if pos == -1:
                    break
                positions.append(pos)
                start = pos + len(word)
            result = {"count": count, "positions": positions}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)