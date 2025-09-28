from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-response", methods=["POST"])
def get_response():
    data = request.get_json()
    message = data.get("message", "")

    try:
        system_prompt = """

Abdul Wali Khan University Mardan (AWKUM) — Official Information Dataset
=======================================================================

GENERAL OVERVIEW
----------------
Abdul Wali Khan University Mardan (AWKUM) was established in 2009 as a public sector university.
It is located in Mardan, Khyber Pakhtunkhwa, Pakistan.
The university is named after Abdul Wali Khan, a respected political leader and educationist.
The Garden Campus of AWKUM is spread over 2,000 Kanals of land.
AWKUM is ranked 2nd provincially (Khyber Pakhtunkhwa) and placed 601–800 globally in the Times Higher Education Young University Rankings 2021.
The university has grown rapidly, hosting 32 departments across 6 faculties.
It offers 95 degree programs at undergraduate, graduate, and postgraduate levels.
It serves over 14,000 students and employs more than 400 faculty members.
Among faculty, 200+ are PhD holders from leading universities worldwide.
AWKUM is recognized by the Higher Education Commission (HEC) of Pakistan.
The university is known for research, inclusivity, and modern academic standards.

MISSION AND VISION
------------------
Vision: To be among the top-ranked universities globally through excellence in teaching, research, and innovation.
Mission: To provide accessible, world-class education that fosters scientific, economic, and socio-cultural development of Pakistan.
Core Values: Integrity, Inclusiveness, Excellence, Innovation, Service, Global Impact.

RANKINGS AND ACHIEVEMENTS
-------------------------
Times Higher Education Young University Rankings: 601–800 band globally (2021).
Ranked #2 in Khyber Pakhtunkhwa by Times Higher Education (2021).
Ranked among top Pakistani universities for research funding and publications.
Recipient of multiple National Research Program for Universities (NRPU) grants from HEC.
Leading university in Khyber Pakhtunkhwa for AI and Data Science programs.
Hosts internationally indexed research journals.
Has produced globally cited research in Biotechnology, Environmental Sciences, and AI.
Facilitates international collaborations with universities in UK, USA, China, and Middle East.
Recognized as one of the fastest-growing public universities in Pakistan.

FACULTIES AND DEPARTMENTS
-------------------------
Faculty of Arts & Humanities:
- Department of English
- Department of Islamic Studies
- Department of Urdu
- Department of Pashto
- Department of Archaeology

Faculty of Business & Economics:
- Department of Management Sciences
- Department of Economics

Faculty of Chemical & Life Sciences:
- Department of Biotechnology
- Department of Botany
- Department of Zoology
- Department of Chemistry

Faculty of Physical & Numerical Sciences:
- Department of Computer Science
- Department of Artificial Intelligence
- Department of Data Science
- Department of Mathematics
- Department of Physics
- Department of Geology

Faculty of Social Sciences:
- Department of Political Science
- Department of Sociology
- Department of Education
- Department of Journalism & Mass Communication
- Department of Psychology
- Department of Law (LLB program)

Faculty of Agriculture:
- Department of Agronomy
- Department of Horticulture
- Department of Plant Breeding and Genetics

TOTAL: 32 departments across 6 faculties.

ACADEMIC PROGRAMS
-----------------
Undergraduate Programs (BS 4 years):
- BS Artificial Intelligence
- BS Computer Science
- BS Data Science
- BS Software Engineering
- BS Information Technology
- BS English
- BS Urdu
- BS Pashto
- BS Islamic Studies
- BS Sociology
- BS Political Science
- BS Education
- BS Journalism & Mass Communication
- BS Psychology
- BS Biotechnology
- BS Botany
- BS Zoology
- BS Chemistry
- BS Physics
- BS Geology
- BS Mathematics
- BS Economics
- BS Management Sciences
- BS Agronomy
- BS Horticulture
- BS Plant Breeding & Genetics
- LLB (5 years)
- Pharm-D (Doctor of Pharmacy, 5 years)

BS (5th Semester Lateral Entry):
- Computer Science
- AI
- Data Science
- Management Sciences
- Biotechnology
- Chemistry
- English
- Education

Graduate Programs (MA/MSc 2 years):
- MA English
- MA Urdu
- MA Islamic Studies
- MSc Chemistry
- MSc Physics
- MSc Mathematics
- MSc Zoology
- MSc Botany
- MSc Political Science
- MSc Economics
- MSc Education

Postgraduate Programs (MPhil/PhD):
- MPhil Computer Science
- MPhil Data Science
- MPhil Management Sciences
- MPhil Biotechnology
- MPhil Botany
- MPhil Zoology
- MPhil Chemistry
- MPhil Physics
- MPhil Mathematics
- MPhil Islamic Studies
- MPhil Political Science
- MPhil Education
- PhD Computer Science
- PhD Biotechnology
- PhD Botany
- PhD Chemistry
- PhD Physics
- PhD Islamic Studies
- PhD Political Science
- PhD Education

ADMISSIONS (2025)
-----------------
Admissions Portal: admissions.awkum.edu.pk
Application Deadline Fall 2025: September 25, 2025 (extended).
Late submissions accepted until November 2025 with additional fee.
Eligibility Criteria:
- BS Programs: Minimum 45% marks in Intermediate or equivalent.
- Pharm-D: 60% marks in F.Sc. Pre-Medical.
- LLB: Requires LAT (Law Admission Test).
- BS AI/CS/Data Science: 45% marks in F.Sc. Pre-Engineering/ICS with Mathematics.
- MPhil: Minimum 2.5 CGPA (out of 4) or 2nd division, plus NTS GAT General.
- PhD: Minimum 3.0 CGPA (out of 4) plus NTS GAT Subject or university test.
International Students: Separate quota and eligibility requirements apply.

SCHOLARSHIPS AND FINANCIAL AID
------------------------------
HEC Need-Based Scholarship.
Ehsaas Undergraduate Scholarship Program.
Merit-based scholarships.
Fee concessions for top students.
Reserved seats and scholarships for:
- Disabled students
- Sports quota
- Ex-FATA students
- Overseas Pakistanis
- Minorities

FEE STRUCTURE (Examples, 2025)
-------------------------------
BS Geology (Open Merit): PKR 37,720 per semester.
BS Geology (Self-Finance): PKR 56,600 per semester.
BS Computer Science: Approx. PKR 40,000–60,000 per semester.
BS Artificial Intelligence: Approx. PKR 42,000–62,000 per semester.
LLB: Approx. PKR 50,000 per semester.
Pharm-D: Approx. PKR 65,000 per semester.
MPhil Programs: Approx. PKR 70,000–85,000 per semester.
PhD Programs: Approx. PKR 85,000–100,000 per semester.
Scholarships may reduce actual costs significantly.

RESEARCH AND INNOVATION
-----------------------
AWKUM publishes multiple peer-reviewed journals.
Key journals include:
- Tahdhīb al Afkār (biannual, English, Urdu, Arabic).
- Pakhtunkhwa Journal of Life Sciences.
- AWKUM Journal of Social Sciences.
- Journal of Applied and Emerging Sciences.
The university has 200+ PhD faculty engaged in research.
Strong focus on AI, Biotechnology, Environmental Sciences, Renewable Energy, and Agriculture.
Leads Khyber Pakhtunkhwa in NRPU projects.
Collaborates with Oxford, Cambridge, Manchester, Tsinghua, and Middle Eastern universities.
Research centers include:
- AI and Machine Learning Lab
- Data Science Research Lab
- Biotechnology Lab
- Environmental Sciences Lab
- Agricultural Research Farm

FACILITIES AND CAMPUS LIFE
--------------------------
Digitized Central Library with 70,000+ books and e-resources.
Modern computer labs with internet access.
AI and Data Science labs with GPUs and servers.
Lecture halls with multimedia support.
Student hostels (separate for male and female).
Transport services across Mardan and surrounding districts.
Sports facilities: cricket, football, volleyball, badminton, athletics.
Indoor gyms and student fitness centers.
Cafeterias and dining halls.
Campus mosque and prayer facilities.
Student support services for career counseling.
Health center with doctors and first aid.
Cultural and academic societies for extracurricular activities.

INTERNATIONALIZATION
--------------------
MoUs signed with universities in China, UK, USA, and Middle East.
Student exchange programs.
Visiting professors from global universities.
Collaborative PhD supervision programs.
Research collaboration in AI, Agriculture, and Environmental Sciences.

CONTACT INFORMATION
-------------------
Official Website: www.awkum.edu.pk
Admissions Portal: admissions.awkum.edu.pk
Email: info@awkum.edu.pk
Phone: +92-937-843374
Address: Garden Campus, Abdul Wali Khan University Mardan, KP, Pakistan.

SUMMARY
-------
AWKUM is a leading university in Khyber Pakhtunkhwa, with 32 departments, 95 programs, 14,000+ students, and 200+ PhD faculty.
It is ranked globally in Times Higher Education, recognized for research and innovation.
It offers scholarships, diverse programs, world-class facilities, and an inclusive environment.
AWKUM is committed to faith, excellence, research, and service to society.



Department of Computer Science, Abdul Wali Khan University Mardan (AWKUM)

Overview
The Department of Computer Science at Abdul Wali Khan University Mardan (AWKUM) is a key part of the Faculty of Physical & Numerical Sciences. Established to meet the rising need for skilled IT professionals, it offers top-quality education, cutting-edge research, and strong industry ties. Located at the Garden Campus in Mardan, Khyber Pakhtunkhwa, Pakistan, the department is recognized by the Higher Education Commission (HEC). It hosts an active ACM Student Chapter and has partnerships with tech firms like NETSOL. AWKUM, founded in 2009 as a public sector university and named after Abdul Wali Khan, a respected political leader and educationist, spans over 2,000 Kanals of land at its Garden Campus.

Programs
The Department of Computer Science offers a variety of undergraduate and graduate programs, including specialized tracks in Cybersecurity, Software Engineering, Artificial Intelligence, and an Honors program:

BS Computer Science: A 4-year program (133 credit hours) teaching core skills like programming, algorithms, databases, and computer networks. Prepares students for IT and software development careers.
BS Computer Science (Cybersecurity): A 4-year program (133 credit hours) focusing on network security, ethical hacking, cryptography, and cybersecurity frameworks. Trains students to protect systems from cyber threats.
BS Computer Science (Software Engineering): A 4-year program (133 credit hours) covering software development, testing, project management, and agile methodologies. Prepares students for software engineering roles.
BS Computer Science (Artificial Intelligence): A 4-year program (133 credit hours) specializing in AI, machine learning, neural networks, and data analytics. Equips students for AI-driven industries and research.
BS Computer Science (Hons): A 4-year advanced program (133+ credit hours) with extra research and elective courses. Ideal for students aiming for graduate studies or specialized careers in AI, cybersecurity, or software engineering.
MCS (Master of Computer Science): A 2-year program (60 credit hours) with advanced topics and an optional thesis.
MPhil Computer Science: A 2-year research-focused program requiring GAT General (50% score).
PhD Computer Science: A 3-5 year program for original research, requiring GAT Subject (50% score).
Admission Strategy

Criteria:
BS Programs: Minimum 50% marks in Intermediate (ICS/Pre-Engineering) or equivalent, plus AWKUM/ETEA entry test.
MCS: BS in Computer Science/IT with 2.5 CGPA, plus test/interview.
MPhil/PhD: Follow HEC rules (16 years education, 2.5 CGPA for MPhil; 18 years, 3.0 CGPA for PhD, with GAT 50% score).
Process: Apply online at admissions.awkum.edu.pk, submit documents (transcripts, CNIC, photos, domicile), attend test/interview, check merit lists, and confirm with fee payment. Fall 2025 admissions are open with limited seats.
Fee Structure (2025):
BS Programs: PKR 40,000–50,000 per semester.
MCS: PKR 50,000–60,000 per semester.
MPhil: PKR 55,000–75,000 per semester.
PhD: PKR 75,000–95,000 per semester.
Application Fee: PKR 2,000 (non-refundable).
Note: Fees reflect a 10% hike for 2025; scholarships may reduce costs.
Research and Innovation
The department leads in research with a focus on:

Artificial Intelligence & Machine Learning: Developing predictive models and neural networks.
Cybersecurity: Building frameworks for threat detection and blockchain applications.
Software Engineering: Advancing agile development and software quality assurance.
Cloud Computing & IoT: Creating scalable cloud solutions and smart systems.
Data Science & Big Data Analytics: Exploring data mining and visualization.
Robotics & Computer Vision: Innovating in autonomous systems and image processing. Notable projects include HEC-funded AI-based diagnostic tools and cloud migration for local industries. Faculty and students have published over 100 papers in HEC-recognized journals like IEEE and Springer (2020–2025). The department collaborates with universities like UET Peshawar and COMSATS.
Facilities

Labs:
General Computer Labs: Four labs with over 100 high-end PCs, running Windows/Linux, with fiber-optic internet and printers for programming and coursework.
AI & Robotics Lab: Equipped with NVIDIA GPUs, Arduino/Raspberry Pi kits, ROS software, and robotic arms for machine learning and robotics projects.
Software Engineering Lab: Features tools like Visual Studio, Eclipse, Git, and UML software for team-based software development.
Networking & Cybersecurity Lab: Includes Cisco routers/switches, Wireshark, Kali Linux VMs, and firewall simulators for network and security training.
Data Science Lab: Offers servers for big data (Hadoop, Spark), Python/R environments, and Jupyter notebooks for analytics.
Other Facilities:
Seminar Hall: 100-seat hall with projector and AV setup for tech talks and workshops.
Digital Library Access: Includes ACM Digital Library, IEEE Xplore, and HEC resources for research.
Campus Life

Societies:
ACM Student Chapter: Hosts coding competitions and tech talks.
Computer Science Society (CSS): Promotes peer learning and group projects.
AI & Robotics Club: Organizes hands-on workshops in AI and robotics.
Women in Computing Group: Supports female students in tech fields.
Events:
Annual Tech Fest & Hackathon: Showcases student innovations and coding skills.
Coding Competitions: Prepares students for ICPC regional contests.
Workshops: Covers AI, machine learning, cloud computing, and cybersecurity.
Guest Lectures: Features experts from Google, Microsoft, and NETSOL.
Career Prospects
Graduates are equipped for roles such as:

Software Developer/Engineer
AI/Machine Learning Engineer
Cybersecurity Analyst
Data Scientist/Analyst
IT Project Manager/Consultant
Academic/Researcher
Tech Entrepreneur in startups
Faculty

Permanent Faculty:
Dr. Nadeem Iqbal: Chairman and Associate Professor, PhD Computer Science (University of Central Punjab). Specializes in Software Engineering, Data Mining, Agile Methodologies. Email: nadeem@awkum.edu.pk.
Prof. Dr. Sher Afzal Khan: Professor, PhD Computer Science (University of Peshawar). Specializes in Artificial Intelligence, Machine Learning, Neural Networks. Email: skhan.afzal@gmail.com.
Dr. Maqsood Hayat: Associate Professor, PhD Computer Science (COMSATS University). Specializes in Bioinformatics, Algorithms, Computational Biology. Email: m.hayat@awkum.edu.pk.
Dr. Hanif Ur Rahman: Associate Professor, PhD Computer Science (International Islamic University). Specializes in Cloud Computing, IoT, Distributed Systems. Email: hanif@awkum.edu.pk.
Dr. Muhammad Ilyas Khan Khalil: Assistant Professor, PhD Computer Science (University of Malaya). Specializes in Cybersecurity, Network Security, Blockchain. Email: ilyas@awkum.edu.pk.
Mr. Ashraf Zia: Lecturer, MS Computer Science (AWKUM). Specializes in Web Development, Databases, Mobile Apps. Email: ashrafzia@awkum.edu.pk, Phone: +92-301-302-8777.
Ms. Sobia Bibi: Lecturer, MS Software Engineering (UET Peshawar). Specializes in Software Testing, Quality Assurance. Email: sobia@awkum.edu.pk.
Visiting Faculty:
Dr. Amir Ali: Visiting Professor, PhD Computer Science (MIT). Specializes in Robotics, Computer Vision. Email: amir.ali@guest.edu.
Mr. Khalid Rehman: Visiting Lecturer, MS Computer Science (Industry Expert). Specializes in DevOps, Cloud AWS. Email: khalid@industry.com.
Contact Information

Official Website: https://awkum.edu.pk/faculties-colleges/faculty-of-physical-numerical-sciences/cs-garden/
Email: cs@awkum.edu.pk
Phone: +92-937-9230570
Office Address: Room #CS-101, Garden Campus, Abdul Wali Khan University Mardan, Khyber Pakhtunkhwa, Pakistan



"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message},
            ],
            temperature=0.85,
        )

        answer = (
            response.choices[0].message.content or "⚠️ No response from AI."
        ).strip()
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"response": f"⚠️ Error: {str(e)}"})


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    app.run(host="0.0.0.0", port=10000)
