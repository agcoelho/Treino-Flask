from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from FakePinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    senha = PasswordField('senha', validators=[DataRequired()])
    botao_confirmar = SubmitField('confirma')


class FormCriarConta(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    username = StringField('username', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired(), Length(6, 20)])
    confirmar_senha = PasswordField('confirme a senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmar = SubmitField('confirma')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError('email ja cadastrado, faça login para continuar')
