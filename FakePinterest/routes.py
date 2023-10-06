from flask import Flask, url_for, render_template, redirect
from FakePinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user
from FakePinterest.froms import FormLogin, FormCriarConta
from FakePinterest.models import Usuario, Foto

@app.route('/', methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario:
            bcrypt.check_password_hash(usuario.senha, formLogin.senha.data)
            login_user(usuario)
        return redirect(url_for('perfil', usuario=usuario.username))

    return render_template('homepage.html', form=formLogin)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarConta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data,
                          senha=senha,
                          email=formcriarconta.email.data)

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)

        return redirect(url_for('perfil', usuario=usuario.username))
    return render_template('criarConta.html', form=formcriarconta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)
