from flask import Flask, request

app = Flask(__name__)

@app.route("/ebay-account-deletion", methods=["GET", "POST"])
def ebay_deletion():
    VERIFICATION_TOKEN = "SmokeyDokeyOhioSkibblerLegoStarWarsDone198356"
    token = request.headers.get("X-EBAY-VERIFY-TOKEN") or request.args.get("verificationToken")

    if token and token != VERIFICATION_TOKEN:
        return "Unauthorized", 403

    return "OK", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
