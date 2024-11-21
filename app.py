from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        cantidad = int(request.form.get("cantidad"))

        precio_unitario = 9000
        total_sin_descuento = precio_unitario * cantidad

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - descuento
        return render_template(
            "resultado1.html",
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_con_descuento=total_con_descuento,
        )
    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    usuarios = {"juan": "admin", "pepe": "user"}
    mensaje = None

    if request.method == "POST":
        nombre = request.form.get("nombre")
        password = request.form.get("password")

        if nombre in usuarios and usuarios[nombre] == password:
            if nombre == "juan":
                mensaje = f"Bienvenido Administrador {nombre}"
            else:
                mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)

