from flask import Flask, request

app = Flask(__name__)

# This route must match exactly what you enter in eBay Developer Portal
@app.route("/ebay-account-deletion", methods=["POST"])
def ebay_deletion():
    # Optional: check token from eBay
    VERIFICATION_TOKEN = "SmokeyDokeyOhioSkibblerLegoStarWarsDone198356"
    token = request.headers.get("X-EBAY-VERIFY-TOKEN") or request.args.get("verificationToken")
    if token and token != VERIFICATION_TOKEN:
        return "Unauthorized", 403

    # eBay just wants 200 OK
    print("Received account deletion notification from eBay!")
    return "OK", 200

if __name__ == "__main__":
    # Port 10000 is standard on Render for Python apps
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)