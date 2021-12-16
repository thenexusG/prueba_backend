{% extends 'layout.html' %}

{% block body %}
{% with messages = get_flashed_messages() %}
{% if messages %}
{% for message in messages %}
<p>{{ message }}</p>
{% endfor %}
{% endif %}
{% endwith %}

<form action="/Colonia" method="POST">
    <div class="mb-3 row">
        <div class="col-sm-2">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="id_asenta" placeholder="Id asentamiento">
        </div>
        <div class="col-sm-2">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="asentamiento" placeholder="asentamiento">
        </div>
        <div class="col-sm-2">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="id_municipio" placeholder="Id municipio">
        </div>
        <div class="col-sm-2">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="id_estado" placeholder="Id estado">
        </div>
        <div class="col-sm-2">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="cp" placeholder="CP">
        </div>

        <button class="col-sm-2 btn btn-primary btn-sm type="submit">Guardar</button>
    </div>
</form>

<table class="table table-striped">
    <thead>
        <tr>
            <td>id asentamiento</td>
            <td>asentamiento</td>
            <td>id municipio</td>
            <td>id estado</td>
            <td>CP</td>
        </tr>
    </thead>
    <tbody>
        {% for asentamiento in asentamientos %}
        <tr>
            <td>{{ asentamiento.0}}</td>
            <td>{{ asentamiento.1}}</td>
            <td>{{ asentamiento.2}}</td>
            <td>{{ asentamiento.3}}</td>
            <td>{{ asentamiento.4}}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>


{% endblock %}