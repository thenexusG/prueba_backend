{% extends 'layout.html' %}

{% block body %}
{% with messages = get_flashed_messages() %}
{% if messages %}
{% for message in messages %}
<p>{{ message }}</p>
{% endfor %}
{% endif %}
{% endwith %}


<form action="/Colonia_Name" method="POST">
    <div class="mb-1 row">
        <div class="col-sm-10">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="colonia"
                placeholder="Colonia">
        </div>
        <button class="col-sm-2 btn btn-primary btn-sm" type="submit">Buscar</button>
    </div>
</form>
<br>
<table class="table table-striped">
    <thead>
        <tr>
            <td>ID Asentamiento</td>
            <td>Asentamiento</td>
            <td>ID municipio</td>
            <td>ID estado</td>
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
<hr>
<form action="/Municipio_Name" method="POST">
    <div class="mb-3 row">
        <div class="col-sm-3">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text"
                name="id_municipio" placeholder="Id municipio">
        </div>
        <div class="col-sm-3">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text"
                name="municipio" placeholder="Municipio">
        </div>
        <div class="col-sm-3">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text"
                name="id_estado" placeholder="Id estado">
        </div>
        <button class="col-sm-3 btn btn-primary btn-sm" type="submit">Buscar</button>
    </div>
</form>
<br>
<table class="table table-striped">
    <thead>
        <tr>
            <td>id municipio</td>
            <td>municipio</td>
            <td>id estado</td>
        </tr>
    </thead>
    <tbody>
        {% for municipio in municipios %}
        <tr>
            <td>{{ municipio.0}}</td>
            <td>{{ municipio.1}}</td>
            <td>{{ municipio.2}}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
<hr>
<form action="/Estado_Name" method="POST">
    <div class="mb-3 row">
        <div class="col-sm-5">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text"
                name="id_estado" placeholder="Id estado">
        </div>
        <div class="col-sm-5">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="estado"
                placeholder="Estado">
        </div>
        <button class="col-sm-2 btn btn-primary btn-sm" type="submit">Buscar</button>
    </div>
</form>

<table class="table table-striped">
    <thead>
        <tr>
            <td>id</td>
            <td>estado</td>
        </tr>
    </thead>
    <tbody>
        {% for estado in estados %}
        <tr>
            <td>{{ estado.0}}</td>
            <td>{{ estado.1}}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>


{% endblock %}