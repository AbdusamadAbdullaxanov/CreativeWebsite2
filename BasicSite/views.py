from django.shortcuts import render
from .forms import InputForms, TestForm
from googletrans import Translator

data = ""


def welcome(request):
    form = TestForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            pass
    return render(request, "MainPage.html", {})


def translator(request):
    global data
    form = InputForms(request.POST)
    if form.is_valid():
        print("valid")
        text = form.cleaned_data["textarea"]
        data += str(text)
    return render(
        request,
        "BasicSite/basic_engine.html",
        {
            "form": form
        }
    )


def translated(request):
    print(data + "\n\n\n\n")
    translated_text = Translator().translate(data, dest="uz").text
    return render(request, "BasicSite/translated.html", {"translated_text": translated_text})
