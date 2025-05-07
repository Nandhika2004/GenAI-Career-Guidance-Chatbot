from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy career chatbot logic
def get_career_advice(user_input):
    if "Hi" in user_input.lower():
        return "Please tell me your interests."

    elif "engineer" in user_input.lower():
        return "Engineering Career Path: Courses: BE/BTech (Computer, Mechanical, Civil, AI), Entrance Exams: JEE, Top Colleges: IITs, Job Roles: Software Developer, Data Analyst"

    elif "doctor" in user_input.lower():
        return "Doctor Career Path: Course: MBBS, Entrance Exam: NEET-UG, Top Colleges: AIIMS, Job Roles: Surgeon, Pediatrician"

    elif "business" in user_input.lower():
        return "Business Path: Courses: BBA, MBA, Skills: Leadership, Top Institutes: IIMs, Career Roles: Manager, Analyst"

    elif "designer" in user_input.lower():
        return "Design Career Path: Courses: BDes, Animation, Entrance Exams: NID, NIFT, Job Roles: UI/UX Designer, Animator"

    else:
        return "Hello, How can i help you!, Please tell me your interests."
        

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_career_advice(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
