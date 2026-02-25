from flask import *
app=Flask(__name__)
import requests

URL="https://test.devilhai.online/"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/all")
def accounts():
    try:
        response=requests.get(URL+"all_accounts/")
        data=response.json()
        return render_template("all_accounts.html",account=data)

    except Exception as e:
        return str(e)
    

@app.route("/delete")
def delete_account():
    return "I am delete funtion and call when you clicked on delete"

@app.route("/register-now")
def register():
    return render_template("register.html")

@app.route("/create-account",methods=["POST"])
def create_account():
    try:
        if request.method=="POST":
            cus_ac_no=request.form.get("cus_ac_no")
            cus_name=request.form.get("cus_name")
            cus_mob=request.form.get("cus_mob")
            cus_add=request.form.get("cus_add")
            image=request.files.get("profile_img")

            file={}

            if image and image.filename != "":
                file["profile_image"]=(
                    image.filename,
                    image.stream,
                    image.mimetype,
                )

            payload={
                "cus_ac_no":cus_ac_no,
                "cus_ac_holder":cus_name,
                "cus_mob":cus_mob,
                "cus_address":cus_add
            }
            requests.post(URL+"create_account/",data=payload,files=file)
            return redirect(url_for("accounts"))
            # return f"{response.status_code} {response.text}"
    
    except Exception as e:
        return str(e)

    
if __name__ == "__main__":
    app.run()