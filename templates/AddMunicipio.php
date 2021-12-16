{% extends 'layout.html' %}

{% block body %}
{% with messages = get_flashed_messages() %}
{% if messages %}
{% for message in messages %}
<p>{{ message }}</p>
{% endfor %}
{% endif %}
{% endwith %}


<form action="/Municipio" method="POST">
    <div class="mb-3 row">
        <div class="col-sm-3">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="id_municipio" placeholder="Id municipio">
        </div>
        <div class="col-sm-3">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="municipio" placeholder="Municipio">
        </div>
        <div class="col-sm-3">
            <input class="form-control form-control-sm" aria-label=".form-control-sm example" type="text" name="id_estado" placeholder="Id estado">
        </div>
        <button class="col-sm-3 btn btn-primary btn-sm" type="submit">Guardar</button>
    </div>
</form>

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

{% endblock %}