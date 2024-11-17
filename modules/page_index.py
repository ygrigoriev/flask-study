from flask import render_template, request


def view():
    return render_template('index.html', person='name')
