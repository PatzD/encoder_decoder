from rest_framework import response
from rest_framework.decorators import api_view
from . import functions


@api_view(["POST"])
def encode(request):
    """taking request containing sentence, returns encoded sentence using encode_sentance function"""
    if request.method == "POST":
        data = request.data

        return response.Response(functions.encode_sentance(data["sentence"]))


@api_view(["POST"])
def decode(request):
    """return hello world"""
    if request.method == "POST":
        encoded = request.data["encoded"]
        ori_sorted = request.data["original_sorted"]

        decoded = functions.decoder(encoded, ori_sorted)

        # decoded = " ".join(decoded)

        return response.Response(decoded)
