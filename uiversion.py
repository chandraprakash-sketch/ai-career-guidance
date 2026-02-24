from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    name = request.form['name']
    current_class = int(request.form['class'])
    goal = request.form['goal']

    english = {

    "foundation_title":"Academic Foundation (Before 10th):",

    "foundation_text":[
    "From Class 6 to 8, students must build strong conceptual clarity in all subjects.",
    "Mathematics develops logical thinking required for engineering and competitive exams.",
    "Science develops curiosity and analytical thinking required for research and medical fields.",
    "Languages build communication skills, confidence and personality.",
    "Class 9 and 10 board performance plays a critical role in future academic opportunities.",
    "A strong academic base reduces stress during entrance exam preparation."
    ],

    "career_importance":{
    "1":"Doctors play a critical role in saving lives and improving public health systems.",
    "2":"Engineers contribute to national development through technology and infrastructure.",
    "3":"Police officers protect law, order and social stability.",
    "4":"Teachers build the intellectual foundation of future generations.",
    "5":"IAS officers manage administration, policy and governance.",
    "6":"Scientists lead innovation and research for national progress.",
    "7":"Entrepreneurs generate employment and economic growth.",
    "8":"Sports professionals bring pride and global recognition to the nation."
    },

    "streams":{
    "1":"PCB (Physics, Chemistry, Biology)",
    "2":"PCM (Physics, Chemistry, Mathematics)",
    "3":"Any stream + Strong Physical Fitness",
    "4":"Stream based on subject specialization",
    "5":"Any stream allowed",
    "6":"Science stream mandatory",
    "7":"Commerce preferred",
    "8":"Academics + Professional Sports Training"
    },

    "stream_reason":{
    "1":"Biology is the foundation of medical science and human anatomy.",
    "2":"Mathematics and Physics are essential for engineering problem-solving.",
    "3":"Police careers focus more on discipline and physical standards.",
    "4":"Teachers must gain deep knowledge in the subject they teach.",
    "5":"IAS requires graduation in any discipline with strong awareness.",
    "6":"Scientific research requires strong fundamentals in science.",
    "7":"Business requires financial literacy and strategic thinking.",
    "8":"Sports demand continuous training along with educational balance."
    },

    "exams":{
    "1":["NEET"],
    "2":["JEE","EAMCET"],
    "3":["Police Recruitment Exams"],
    "4":["TET"],
    "5":["UPSC Civil Services"],
    "6":["IISER","NEST"],
    "7":["CUET","CAT"],
    "8":["State/National Sports Trials"]
    },

    "exam_reason":{
    "1":"NEET ensures merit-based selection into medical colleges.",
    "2":"JEE/EAMCET evaluate analytical and problem-solving skills.",
    "3":"Police exams test physical ability and awareness.",
    "4":"TET verifies teaching competency.",
    "5":"UPSC selects capable administrative leaders.",
    "6":"Research exams evaluate scientific aptitude.",
    "7":"Management exams assess business and leadership skills.",
    "8":"Sports trials evaluate performance and consistency."
    },

    "roadmap":{
    "1":{11:"Select PCB and start structured NEET preparation.",
         12:"Revise syllabus, practice mock tests and improve time management.",
         "Degree":"Complete MBBS with clinical exposure.",
         "Future":"Specialize (MD/MS) and serve in hospitals or research institutions."},

    "2":{11:"Select PCM and begin JEE/EAMCET preparation.",
         12:"Solve previous papers and improve speed & accuracy.",
         "Degree":"Complete B.Tech / Engineering degree.",
         "Future":"Work in industry, innovation or pursue M.Tech/MS."},

    "3":{11:"Maintain physical standards and study recruitment syllabus.",
         12:"Prepare for physical and written exams.",
         "Degree":"Complete graduation.",
         "Future":"Serve in law enforcement with discipline and integrity."},

    "4":{11:"Choose subject specialization.",
         12:"Plan degree aligned with teaching career.",
         "Degree":"Complete graduation + B.Ed.",
         "Future":"Become an educator shaping future citizens."},

    "5":{11:"Build awareness, reading habits and leadership skills.",
         12:"Plan graduation with UPSC focus.",
         "Degree":"Complete graduation in any discipline.",
         "Future":"Prepare strategically for UPSC Civil Services."},

    "6":{11:"Strengthen science fundamentals.",
         12:"Prepare for research-oriented entrance exams.",
         "Degree":"Complete B.Sc / Engineering.",
         "Future":"Pursue M.Sc / PhD and research career."},

    "7":{11:"Choose Commerce and learn financial basics.",
         12:"Develop entrepreneurial thinking.",
         "Degree":"Complete BBA/B.Com.",
         "Future":"Start business or pursue MBA."},

    "8":{11:"Continue professional sports training.",
         12:"Participate in competitive trials.",
         "Degree":"Balance education with sports development.",
         "Future":"Build professional sports career."}
    },

    "parent":[
    "Encourage interest-based decision making.",
    "Focus on strong academic performance before 10th.",
    "Maintain structured routine and discipline.",
    "Avoid comparison and unnecessary pressure.",
    "Support emotional, academic and skill development."
    ],

    "final":"Career success is a structured journey. Right direction + discipline + clarity = long-term achievement."
    }

    return render_template("result.html",
                           name=name,
                           current_class=current_class,
                           goal=goal,
                           data=english)

if __name__ == "__main__":
    app.run()