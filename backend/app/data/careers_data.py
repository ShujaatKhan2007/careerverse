"""
Seed data for the `careers` collection.

This is the content backbone of CareerVerse. Each entry follows a consistent
schema so the recommendation engine, comparison tool, and detail pages can
all render any career without special-casing. Add new careers by appending
a new dict here (or inserting directly into MongoDB) - no code changes
needed elsewhere in the app.
"""

CAREERS = [
    {
        "slug": "software-engineer",
        "title": "Software Engineer",
        "category": "Technology",
        "icon": "code",
        "short_description": "Design, build, and maintain software systems, applications, and platforms.",
        "difficulty": "Medium",
        "streams": ["Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Software Engineers design, develop, test, and maintain applications, websites, and systems. "
            "It is one of the fastest-growing and highest-paying career paths globally, spanning web, mobile, "
            "cloud, AI/ML, and embedded systems specializations."
        ),
        "required_qualifications": [
            "10+2 with Physics, Chemistry, Mathematics (PCM) for engineering route",
            "B.Tech/B.E. in Computer Science or related field (4 years), or BCA/BSc CS (3 years)",
            "Optional: M.Tech/MS for specialization or research roles",
        ],
        "entrance_exams": [
            {
                "name": "JEE Main",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "Passed 10+2 with Physics, Chemistry, Mathematics",
                "age_limit": "No upper age limit (as per latest NTA guidelines)",
                "attempts": "2 attempts per year (Jan & Apr sessions), can be taken in consecutive years",
                "selection_process": "Computer-based test → Merit list → Counselling (JoSAA/CSAB)",
                "exam_pattern": "90 questions (MCQ + numerical), 300 marks, 3 hours, Physics/Chemistry/Maths",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics (NCERT-based)",
            },
            {
                "name": "JEE Advanced",
                "conducting_body": "IIT (rotational)",
                "eligibility": "Top ~2.5 lakh rankers of JEE Main",
                "age_limit": "Born on or after specified cutoff year (check current notification)",
                "attempts": "Maximum 2 attempts in consecutive years",
                "selection_process": "Two papers → Merit list → JoSAA counselling for IITs",
                "exam_pattern": "2 papers, objective + numerical, variable marking, 3 hours each",
                "syllabus": "Advanced-level Physics, Chemistry, Mathematics",
            },
        ],
        "preparation_strategy": [
            "Build strong fundamentals in Mathematics and Physics from Class 11 onward",
            "Learn a programming language (Python/C++/Java) early to build genuine interest",
            "Practice previous year JEE papers and take regular mock tests",
            "Build 2-3 personal coding projects during undergrad to strengthen your resume",
            "Prepare separately for coding interviews (DSA) in the final year for placements",
        ],
        "best_books": [
            "NCERT Physics, Chemistry, Mathematics (Class 11 & 12)",
            "Concepts of Physics - H.C. Verma",
            "Introduction to Algorithms - Cormen (CLRS)",
            "Cracking the Coding Interview - Gayle Laakmann McDowell",
        ],
        "online_resources": [
            {"name": "NPTEL", "type": "free", "url": "https://nptel.ac.in"},
            {"name": "freeCodeCamp", "type": "free", "url": "https://www.freecodecamp.org"},
            {"name": "LeetCode", "type": "freemium", "url": "https://leetcode.com"},
            {"name": "Coursera - CS Specializations", "type": "paid", "url": "https://www.coursera.org"},
        ],
        "previous_year_papers": "https://jeemain.nta.nic.in",
        "top_colleges": [
            "IIT Bombay", "IIT Delhi", "IIT Madras", "BITS Pilani", "NIT Trichy", "IIIT Hyderabad",
        ],
        "scholarships": [
            "National Merit Scholarship", "AICTE Pragati Scholarship", "Institute-specific merit scholarships",
        ],
        "salary_range": {"entry": "₹4-8 LPA", "mid": "₹12-25 LPA", "senior": "₹30 LPA - ₹1 Cr+"},
        "career_growth": "Software Engineer → Senior Engineer → Tech Lead → Engineering Manager / Staff Engineer → Director/VP of Engineering, or a specialist track into Architect/Principal Engineer.",
        "official_websites": ["https://jeemain.nta.nic.in", "https://josaa.nic.in"],
        "faqs": [
            {"q": "Do I need to be an IIT graduate to become a software engineer?",
             "a": "No. Many successful engineers come from NITs, IIITs, state colleges, or self-taught/bootcamp routes."},
            {"q": "Is coding knowledge required before joining engineering college?",
             "a": "Not mandatory, but early exposure helps build strong problem-solving skills."},
        ],
    },
    {
        "slug": "doctor",
        "title": "Doctor (MBBS)",
        "category": "Medicine",
        "icon": "stethoscope",
        "short_description": "Diagnose and treat illnesses, and provide medical care to patients.",
        "difficulty": "Hard",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Doctors diagnose, treat, and prevent illness. Becoming a licensed physician in India requires "
            "clearing NEET-UG, completing MBBS (5.5 years including internship), and optionally pursuing "
            "postgraduate specialization (MD/MS) via NEET-PG."
        ),
        "required_qualifications": [
            "10+2 with Physics, Chemistry, Biology (PCB), minimum 50% aggregate (40% for reserved categories)",
            "MBBS - 4.5 years academic + 1 year compulsory rotating internship",
            "Optional: MD/MS (3 years) or DNB for specialization",
        ],
        "entrance_exams": [
            {
                "name": "NEET-UG",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with PCB, minimum age 17 years by admission year",
                "age_limit": "No upper age limit (as per current Supreme Court ruling)",
                "attempts": "No official cap on number of attempts",
                "selection_process": "Single national exam → All India & State merit lists → Counselling (MCC/state)",
                "exam_pattern": "200 questions (180 to attempt), 720 marks, 3 hours 20 minutes",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Biology (NCERT-based)",
            }
        ],
        "preparation_strategy": [
            "Master NCERT Biology thoroughly - it forms ~50% of NEET weightage",
            "Build strong problem-solving speed in Physics and Chemistry numericals",
            "Take at least 1 full-length mock test weekly starting Class 12",
            "Revise previous 10 years' NEET papers repeatedly for pattern familiarity",
            "Balance board exam preparation with NEET prep - both use overlapping syllabus",
        ],
        "best_books": [
            "NCERT Biology, Physics, Chemistry (Class 11 & 12)",
            "Trueman's Elementary Biology",
            "NCERT + MTG Objective Books for Physics/Chemistry",
            "Dinesh Objective Biology",
        ],
        "online_resources": [
            {"name": "NEET NTA Official Portal", "type": "free", "url": "https://neet.nta.nic.in"},
            {"name": "Physics Wallah", "type": "freemium", "url": "https://www.pw.live"},
            {"name": "Unacademy NEET", "type": "paid", "url": "https://unacademy.com"},
        ],
        "previous_year_papers": "https://neet.nta.nic.in",
        "top_colleges": [
            "AIIMS New Delhi", "CMC Vellore", "JIPMER Puducherry", "Maulana Azad Medical College", "KGMU Lucknow",
        ],
        "scholarships": ["Central Sector Scholarship", "State Merit-cum-Means Scholarships", "AIIMS financial aid schemes"],
        "salary_range": {"entry": "₹6-10 LPA (post-internship)", "mid": "₹15-30 LPA (specialist)", "senior": "₹40 LPA+ (consultant/private practice)"},
        "career_growth": "Intern → Junior Resident → Senior Resident → Specialist Consultant → Department Head / Private Practice / Academic Professor.",
        "official_websites": ["https://neet.nta.nic.in", "https://www.nmc.org.in"],
        "faqs": [
            {"q": "Can I retake NEET if I don't get a good rank?", "a": "Yes, there is no cap on attempts, but plan your age and time investment carefully."},
            {"q": "Is NEET compulsory for BDS, BAMS, and BHMS too?", "a": "Yes, NEET-UG is the common entrance for all major medical, dental, and AYUSH courses in India."},
        ],
    },
    {
        "slug": "chartered-accountant",
        "title": "Chartered Accountant (CA)",
        "category": "Finance",
        "icon": "calculator",
        "short_description": "Manage financial records, audits, taxation, and business advisory for organizations.",
        "difficulty": "Hard",
        "streams": ["Commerce", "Science", "Arts"],
        "min_education": "12th",
        "overview": (
            "Chartered Accountants handle auditing, taxation, financial reporting, and business advisory. "
            "The CA qualification is administered entirely by ICAI through three levels: Foundation, "
            "Intermediate, and Final, combined with practical articleship training."
        ),
        "required_qualifications": [
            "10+2 in any stream (Commerce preferred but not mandatory)",
            "CA Foundation → CA Intermediate → 2 years Articleship → CA Final",
            "Total duration: ~4.5-5 years from 12th grade",
        ],
        "entrance_exams": [
            {
                "name": "CA Foundation",
                "conducting_body": "Institute of Chartered Accountants of India (ICAI)",
                "eligibility": "Passed 10+2 from a recognized board",
                "age_limit": "No age limit",
                "attempts": "Unlimited, exam held twice a year (May/June & Nov/Dec)",
                "selection_process": "Register with ICAI → 4-month study period → Foundation exam → Intermediate → Articleship → Final",
                "exam_pattern": "4 papers covering Accounting, Business Law, Quantitative Aptitude, Business Economics",
                "syllabus": "As prescribed by ICAI study material (updated periodically)",
            }
        ],
        "preparation_strategy": [
            "Start with ICAI's own study material - it is the single most reliable source",
            "Practice numerical papers (Accounts, Costing, Maths) daily for speed and accuracy",
            "Join a structured coaching program if self-study discipline is a challenge",
            "Use the 2-year articleship period to apply theoretical concepts practically",
            "Attempt mock test papers (MTPs) and revision test papers (RTPs) released by ICAI before every attempt",
        ],
        "best_books": [
            "ICAI Study Material & Practice Manuals (mandatory)",
            "Padhuka's Students' Guide for Accounts",
            "D.G. Sharma for Costing",
            "Munish Bhandari for Business Law",
        ],
        "online_resources": [
            {"name": "ICAI BoS Portal", "type": "free", "url": "https://boslive.icai.org"},
            {"name": "CA Wallah / Unacademy CA", "type": "paid", "url": "https://unacademy.com"},
            {"name": "ICAI Digital Learning Hub", "type": "free", "url": "https://www.icai.org"},
        ],
        "previous_year_papers": "https://www.icai.org",
        "top_colleges": ["ICAI is the sole conducting body - no college ranking applies; articleship firm reputation matters (Big 4: Deloitte, EY, KPMG, PwC)"],
        "scholarships": ["ICAI Merit Scholarship Scheme", "ICAI Need-based Scholarships for Articled Assistants"],
        "salary_range": {"entry": "₹7-12 LPA", "mid": "₹15-25 LPA", "senior": "₹30 LPA - ₹1 Cr+ (partner level)"},
        "career_growth": "Articled Assistant → CA → Senior Associate → Manager → Partner (firm) or CFO track in industry.",
        "official_websites": ["https://www.icai.org"],
        "faqs": [
            {"q": "Can a science student pursue CA?", "a": "Yes, CA is open to students from any stream after 12th grade."},
            {"q": "How long does articleship last?", "a": "2 years of mandatory practical training under a practicing CA firm."},
        ],
    },
    {
        "slug": "civil-services-ias",
        "title": "IAS Officer (Civil Services)",
        "category": "Government",
        "icon": "landmark",
        "short_description": "Administer government policy, public welfare programs, and district-level governance.",
        "difficulty": "Very Hard",
        "streams": ["Arts", "Science", "Commerce"],
        "min_education": "Graduation",
        "overview": (
            "IAS (Indian Administrative Service) officers are top-tier civil servants responsible for district "
            "and state administration, policy implementation, and public welfare. Recruitment is via the UPSC "
            "Civil Services Examination, considered one of the toughest exams in the world."
        ),
        "required_qualifications": [
            "Bachelor's degree in any discipline from a recognized university",
            "Final-year students can appear provisionally",
        ],
        "entrance_exams": [
            {
                "name": "UPSC Civil Services Examination (CSE)",
                "conducting_body": "Union Public Service Commission (UPSC)",
                "eligibility": "Graduate in any stream; Indian citizen",
                "age_limit": "21-32 years (relaxation for reserved categories)",
                "attempts": "6 attempts for General category (unlimited for some reserved categories up to age limit)",
                "selection_process": "Prelims (screening, objective) → Mains (written, descriptive) → Interview (Personality Test)",
                "exam_pattern": "Prelims: 2 papers (GS + CSAT, objective); Mains: 9 papers (descriptive); Interview: ~275 marks",
                "syllabus": "History, Polity, Geography, Economy, Environment, Science & Tech, Ethics, Optional subject",
            }
        ],
        "preparation_strategy": [
            "Build NCERT-level foundation (Class 6-12) across History, Polity, Geography, Economics first",
            "Read a national newspaper daily and maintain structured current affairs notes",
            "Choose an optional subject aligned with your academic background or interest",
            "Practice answer writing for Mains from day one, not just information gathering",
            "Take Prelims mock tests regularly to build time-management and elimination skills",
        ],
        "best_books": [
            "NCERT Class 6-12 (all social science subjects)",
            "Indian Polity - M. Laxmikanth",
            "India's Struggle for Independence - Bipan Chandra",
            "Certificate Physical & Human Geography - G.C. Leong",
        ],
        "online_resources": [
            {"name": "PIB & PRS India", "type": "free", "url": "https://pib.gov.in"},
            {"name": "Insights on India", "type": "free", "url": "https://www.insightsonindia.com"},
            {"name": "Vision IAS / ForumIAS Test Series", "type": "paid", "url": "https://visionias.in"},
        ],
        "previous_year_papers": "https://upsc.gov.in",
        "top_colleges": ["No specific college required; coaching institutes like Vajiram & Ravi, ALS, and self-study are common paths"],
        "scholarships": ["State-level pre-exam training scholarships for SC/ST/OBC/minority candidates"],
        "salary_range": {"entry": "₹56,100/month (Level 10 pay matrix) + allowances", "mid": "₹1,44,200+/month", "senior": "₹2,25,000+/month (Secretary level)"},
        "career_growth": "Sub-Divisional Magistrate → District Collector → Divisional Commissioner → Secretary (State/Central) → Cabinet Secretary.",
        "official_websites": ["https://upsc.gov.in"],
        "faqs": [
            {"q": "Is coaching mandatory for UPSC?", "a": "No, many candidates clear it through self-study using standard books and test series."},
            {"q": "Can final-year graduation students apply?", "a": "Yes, provisionally, but the degree must be completed before the Mains document verification."},
        ],
    },
    {
        "slug": "data-scientist",
        "title": "Data Scientist",
        "category": "Technology",
        "icon": "chart-bar",
        "short_description": "Analyze complex data to extract insights and build predictive models for businesses.",
        "difficulty": "Medium",
        "streams": ["Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Data Scientists use statistics, programming, and machine learning to turn raw data into actionable "
            "business insights. It is a highly interdisciplinary and fast-growing field across nearly every industry."
        ),
        "required_qualifications": [
            "10+2 with Mathematics (strongly recommended)",
            "B.Tech/B.Sc in Computer Science, Statistics, Mathematics, or Data Science",
            "Optional: M.Sc/MS/MBA (Analytics) or professional certifications for specialization",
        ],
        "entrance_exams": [
            {
                "name": "JEE Main (for B.Tech Data Science programs)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with Physics, Chemistry/Biology/Informatics, Mathematics",
                "age_limit": "No upper age limit",
                "attempts": "2 attempts per year",
                "selection_process": "CBT → Merit list → Counselling",
                "exam_pattern": "90 questions, 300 marks, 3 hours",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics",
            }
        ],
        "preparation_strategy": [
            "Build a strong base in statistics, probability, and linear algebra",
            "Learn Python (pandas, numpy, scikit-learn) and SQL early",
            "Work on real datasets via Kaggle competitions to build a public portfolio",
            "Understand ML fundamentals before jumping into deep learning frameworks",
            "Build 3-4 end-to-end projects (data collection → model → deployment) for your resume",
        ],
        "best_books": [
            "An Introduction to Statistical Learning - James, Witten, Hastie, Tibshirani",
            "Python for Data Analysis - Wes McKinney",
            "Hands-On Machine Learning - Aurélien Géron",
        ],
        "online_resources": [
            {"name": "Kaggle Learn", "type": "free", "url": "https://www.kaggle.com/learn"},
            {"name": "Andrew Ng's ML Specialization", "type": "paid", "url": "https://www.coursera.org"},
            {"name": "fast.ai", "type": "free", "url": "https://www.fast.ai"},
        ],
        "previous_year_papers": "https://jeemain.nta.nic.in",
        "top_colleges": ["IIT Madras (BS Data Science)", "ISI Kolkata", "IIIT Bangalore", "Chennai Mathematical Institute"],
        "scholarships": ["Institute merit scholarships", "Kaggle/Google Data Science fellowships"],
        "salary_range": {"entry": "₹6-10 LPA", "mid": "₹15-30 LPA", "senior": "₹35 LPA - ₹80 LPA+"},
        "career_growth": "Data Analyst → Data Scientist → Senior Data Scientist → Lead/Principal Data Scientist → Head of Data/AI.",
        "official_websites": ["https://jeemain.nta.nic.in"],
        "faqs": [
            {"q": "Do I need a PhD to become a Data Scientist?", "a": "No, a bachelor's or master's degree with strong practical skills is sufficient for most industry roles."},
            {"q": "Is coding mandatory?", "a": "Yes, proficiency in Python or R along with SQL is expected for almost all data science roles."},
        ],
    },
    {
        "slug": "lawyer",
        "title": "Lawyer",
        "category": "Law",
        "icon": "scale",
        "short_description": "Represent clients, interpret laws, and provide legal counsel in courts and corporations.",
        "difficulty": "Medium",
        "streams": ["Arts", "Commerce", "Science"],
        "min_education": "12th",
        "overview": (
            "Lawyers advise clients, draft legal documents, and represent them in courts or negotiations. "
            "In India, the integrated 5-year BA LLB (or similar) after 12th, or a 3-year LLB after graduation, "
            "are the two main routes into the profession."
        ),
        "required_qualifications": [
            "10+2 in any stream for 5-year integrated law programs",
            "Graduation in any discipline for 3-year LLB programs",
            "Enrollment with State Bar Council + clearing AIBE to practice",
        ],
        "entrance_exams": [
            {
                "name": "CLAT (Common Law Admission Test)",
                "conducting_body": "Consortium of National Law Universities",
                "eligibility": "10+2 with min 45% (40% for reserved categories) for UG; graduation for PG",
                "age_limit": "No upper age limit",
                "attempts": "No cap on attempts",
                "selection_process": "Single national test → All India merit → Centralized counselling",
                "exam_pattern": "150 objective questions (2 hours) covering English, GK, Legal Reasoning, Logical Reasoning, Maths",
                "syllabus": "Comprehension-based; no rote legal knowledge required at UG level",
            }
        ],
        "preparation_strategy": [
            "Read newspapers daily to build general knowledge and legal current affairs",
            "Practice comprehension-based reasoning and passage-based legal reasoning questions",
            "Solve previous years' CLAT papers under timed conditions",
            "Build a habit of precise, analytical writing for the Mains-stage subjective exams (if applicable)",
            "During law school, intern regularly with law firms/chambers to build practical exposure",
        ],
        "best_books": [
            "Universal's CLAT Guide",
            "Legal Awareness & Legal Reasoning - A.P. Bhardwaj",
            "Word Power Made Easy - Norman Lewis (for English section)",
        ],
        "online_resources": [
            {"name": "LawSikho", "type": "paid", "url": "https://lawsikho.com"},
            {"name": "SCC Online Blog", "type": "free", "url": "https://www.scconline.com/blog"},
            {"name": "Ipleaders", "type": "freemium", "url": "https://blog.ipleaders.in"},
        ],
        "previous_year_papers": "https://consortiumofnlus.ac.in",
        "top_colleges": ["NLSIU Bangalore", "NALSAR Hyderabad", "NLU Delhi", "NLU Jodhpur", "Symbiosis Law School"],
        "scholarships": ["NLU-specific merit-cum-means scholarships", "Bar Council of India scholarships"],
        "salary_range": {"entry": "₹6-12 LPA (top firms)", "mid": "₹15-30 LPA", "senior": "₹50 LPA+ (partner/senior counsel)"},
        "career_growth": "Associate → Senior Associate → Partner (law firm), or Junior Advocate → Senior Advocate (litigation track).",
        "official_websites": ["https://consortiumofnlus.ac.in", "https://www.barcouncilofindia.org"],
        "faqs": [
            {"q": "Can commerce or science students take up law?", "a": "Yes, law is open to students from any stream after 12th grade."},
            {"q": "What is AIBE?", "a": "The All India Bar Examination, which must be cleared to practice law in Indian courts after LLB."},
        ],
    },
    {
        "slug": "mechanical-engineer",
        "title": "Mechanical Engineer",
        "category": "Engineering",
        "icon": "cog",
        "short_description": "Design, analyze, and manufacture mechanical systems, machines, and tools.",
        "difficulty": "Medium",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Mechanical Engineers work across automotive, aerospace, manufacturing, robotics, and energy sectors, "
            "designing and optimizing physical systems and machinery."
        ),
        "required_qualifications": ["10+2 with PCM", "B.Tech/B.E. Mechanical Engineering (4 years)", "Optional: M.Tech for specialization"],
        "entrance_exams": [
            {
                "name": "JEE Main",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with Physics, Chemistry, Mathematics",
                "age_limit": "No upper age limit",
                "attempts": "2 attempts per year",
                "selection_process": "CBT → Merit list → JoSAA/state counselling",
                "exam_pattern": "90 questions, 300 marks, 3 hours",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics",
            }
        ],
        "preparation_strategy": [
            "Focus on strong fundamentals in Physics (mechanics, thermodynamics) and Mathematics",
            "Develop spatial visualization skills useful for design and CAD work",
            "Take up hands-on projects (robotics clubs, workshops) alongside academics",
            "Learn CAD tools (AutoCAD, SolidWorks) during undergraduate studies",
        ],
        "best_books": ["NCERT Physics, Chemistry, Mathematics", "Concepts of Physics - H.C. Verma", "Engineering Mechanics - R.S. Khurmi"],
        "online_resources": [
            {"name": "NPTEL Mechanical Courses", "type": "free", "url": "https://nptel.ac.in"},
            {"name": "GrabCAD Community", "type": "free", "url": "https://grabcad.com"},
        ],
        "previous_year_papers": "https://jeemain.nta.nic.in",
        "top_colleges": ["IIT Bombay", "IIT Madras", "IIT Kanpur", "NIT Trichy", "BITS Pilani"],
        "scholarships": ["National Merit Scholarship", "AICTE Pragati Scholarship"],
        "salary_range": {"entry": "₹4-7 LPA", "mid": "₹10-18 LPA", "senior": "₹25 LPA+"},
        "career_growth": "Graduate Engineer Trainee → Design Engineer → Senior Engineer → Engineering Manager → GM/Plant Head.",
        "official_websites": ["https://jeemain.nta.nic.in"],
        "faqs": [{"q": "Is GATE required after B.Tech?", "a": "Only if pursuing M.Tech or PSU jobs; not required for core industry placements."}],
    },
    {
        "slug": "architect",
        "title": "Architect",
        "category": "Design",
        "icon": "building",
        "short_description": "Design buildings and spaces balancing functionality, safety, and aesthetics.",
        "difficulty": "Medium",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Architects plan and design buildings, urban spaces, and infrastructure projects, combining "
            "creativity with technical and structural knowledge."
        ),
        "required_qualifications": ["10+2 with Mathematics", "B.Arch (5 years) recognized by Council of Architecture", "Optional: M.Arch for specialization"],
        "entrance_exams": [
            {
                "name": "NATA (National Aptitude Test in Architecture)",
                "conducting_body": "Council of Architecture (CoA)",
                "eligibility": "10+2 with Mathematics, minimum 50% aggregate",
                "age_limit": "No upper age limit",
                "attempts": "Multiple sessions per year, can reattempt",
                "selection_process": "Drawing + aptitude test → Merit list → Institute-level counselling",
                "exam_pattern": "Drawing test + MCQ-based aesthetic sensitivity/mathematics test",
                "syllabus": "Freehand drawing, geometry, observation skills, general aptitude",
            }
        ],
        "preparation_strategy": [
            "Practice freehand sketching and perspective drawing daily",
            "Build a portfolio of design sketches to strengthen college applications",
            "Study geometry and mensuration thoroughly for the aptitude section",
            "Visit and analyze real buildings to build design observation skills",
        ],
        "best_books": ["NATA/JEE Paper 2 guide by Ar. Shadan Usmani", "A Visual Dictionary of Architecture - Francis D.K. Ching"],
        "online_resources": [
            {"name": "ArchDaily", "type": "free", "url": "https://www.archdaily.com"},
            {"name": "NATA Prep by CoA", "type": "free", "url": "https://www.nata.in"},
        ],
        "previous_year_papers": "https://www.nata.in",
        "top_colleges": ["SPA Delhi", "IIT Roorkee", "CEPT Ahmedabad", "SPA Bhopal"],
        "scholarships": ["CoA merit scholarships", "State government architecture scholarships"],
        "salary_range": {"entry": "₹3-6 LPA", "mid": "₹8-15 LPA", "senior": "₹20 LPA+ (own practice/senior partner)"},
        "career_growth": "Junior Architect → Project Architect → Senior Architect → Principal Architect / Own Firm.",
        "official_websites": ["https://www.nata.in", "https://www.coa.gov.in"],
        "faqs": [{"q": "Is JEE required for architecture?", "a": "Either NATA or JEE Main Paper 2 is accepted depending on the institute."}],
    },
    {
        "slug": "commercial-pilot",
        "title": "Commercial Pilot",
        "category": "Aviation",
        "icon": "plane",
        "short_description": "Operate and navigate commercial aircraft to safely transport passengers and cargo.",
        "difficulty": "Hard",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Commercial Pilots fly passenger and cargo aircraft for airlines. The path involves obtaining a "
            "Commercial Pilot License (CPL) through DGCA-approved flying schools after 12th grade with "
            "Physics and Mathematics."
        ),
        "required_qualifications": ["10+2 with Physics and Mathematics", "CPL from a DGCA-approved flying school", "Class 1 Medical Certificate"],
        "entrance_exams": [
            {
                "name": "DGCA CPL Ground Exams",
                "conducting_body": "Directorate General of Civil Aviation (DGCA)",
                "eligibility": "10+2 with Physics & Mathematics, minimum age 17 for Student Pilot License",
                "age_limit": "Minimum 18 years for CPL issuance",
                "attempts": "Can reattempt individual subject papers",
                "selection_process": "Ground school papers + minimum flying hours (200 hrs) + skill test",
                "exam_pattern": "Subject-wise written exams: Air Navigation, Aviation Meteorology, Air Regulations, Technical",
                "syllabus": "As prescribed by DGCA CAR (Civil Aviation Requirements)",
            }
        ],
        "preparation_strategy": [
            "Build strong fundamentals in Physics, especially mechanics and fluid dynamics",
            "Maintain excellent physical fitness for Class 1 Medical certification",
            "Research and choose a reputed DGCA-approved flying school carefully - costs vary widely",
            "Clear DGCA ground subject exams before or during flight training",
        ],
        "best_books": ["Oxford ATPL series", "Trevor Thom's Private/Commercial Pilot series"],
        "online_resources": [{"name": "DGCA Official Portal", "type": "free", "url": "https://www.dgca.gov.in"}],
        "previous_year_papers": "https://www.dgca.gov.in",
        "top_colleges": ["Indira Gandhi Rashtriya Uran Akademi (IGRUA)", "CAE Simulator Training Pvt Ltd", "Rajiv Gandhi Aviation Academy"],
        "scholarships": ["State government pilot training loan schemes", "Airline-sponsored cadet programs"],
        "salary_range": {"entry": "₹8-15 LPA (First Officer)", "mid": "₹25-45 LPA (Senior First Officer)", "senior": "₹80 LPA - ₹1.5 Cr+ (Captain)"},
        "career_growth": "Trainee First Officer → First Officer → Senior First Officer → Captain → Training Captain/Check Pilot.",
        "official_websites": ["https://www.dgca.gov.in"],
        "faqs": [{"q": "Is pilot training expensive?", "a": "Yes, CPL training in India typically costs ₹35-45 lakh; some airlines offer cadet financing programs."}],
    },
    {
        "slug": "fashion-designer",
        "title": "Fashion Designer",
        "category": "Design",
        "icon": "shirt",
        "short_description": "Create original clothing and accessory designs, blending creativity with market trends.",
        "difficulty": "Medium",
        "streams": ["Arts", "Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Fashion Designers conceptualize and create clothing, accessories, and footwear, combining artistic "
            "vision with an understanding of textiles, trends, and business."
        ),
        "required_qualifications": ["10+2 in any stream", "Bachelor's in Fashion Design (B.Des, 4 years) or diploma programs", "Optional: M.Des for specialization"],
        "entrance_exams": [
            {
                "name": "NIFT Entrance Exam",
                "conducting_body": "National Institute of Fashion Technology (NIFT)",
                "eligibility": "10+2 in any stream",
                "age_limit": "No upper age limit for general category (check current notification)",
                "attempts": "No official cap",
                "selection_process": "Written exam (CAT + GAT) → Situation Test (interview/portfolio for design programs)",
                "exam_pattern": "Creative Ability Test (CAT) + General Ability Test (GAT), objective + drawing-based",
                "syllabus": "General knowledge, quantitative ability, communication, design aptitude, sketching",
            }
        ],
        "preparation_strategy": [
            "Build a strong sketching and visual portfolio well before the exam",
            "Stay updated with current fashion trends, textiles, and designers",
            "Practice situation-test style creative problem-solving exercises",
            "Take mock GAT/CAT tests to build speed for the objective sections",
        ],
        "best_books": ["NIFT/NID Entrance Guide - RPH Editorial Board", "Fashion Sketchbooks by various practicing designers"],
        "online_resources": [{"name": "NIFT Official Prep Portal", "type": "free", "url": "https://nift.ac.in"}],
        "previous_year_papers": "https://nift.ac.in",
        "top_colleges": ["NIFT Delhi", "NIFT Mumbai", "NID Ahmedabad", "Pearl Academy"],
        "scholarships": ["NIFT means-cum-merit scholarships", "State minority/SC-ST design scholarships"],
        "salary_range": {"entry": "₹3-6 LPA", "mid": "₹8-15 LPA", "senior": "₹25 LPA+ (own label/creative director)"},
        "career_growth": "Design Assistant → Designer → Senior Designer → Creative Director / Own Label.",
        "official_websites": ["https://nift.ac.in"],
        "faqs": [{"q": "Do I need drawing skills before applying?", "a": "Basic sketching ability helps, but design aptitude and creativity matter more than technical polish."}],
    },
    {
        "slug": "psychologist",
        "title": "Psychologist",
        "category": "Healthcare",
        "icon": "brain",
        "short_description": "Study human behavior and mental processes to help individuals improve wellbeing.",
        "difficulty": "Medium",
        "streams": ["Arts", "Science"],
        "min_education": "12th",
        "overview": (
            "Psychologists assess and treat mental, emotional, and behavioral issues through counseling, therapy, "
            "and research, working in clinics, schools, corporates, or private practice."
        ),
        "required_qualifications": ["10+2 in any stream", "BA/BSc Psychology (3 years)", "MA/MSc Psychology + RCI license for clinical practice"],
        "entrance_exams": [
            {
                "name": "CUET (for central university admissions)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 in any stream",
                "age_limit": "No upper age limit",
                "attempts": "Once per year",
                "selection_process": "CBT → Merit list → University-specific counselling",
                "exam_pattern": "Subject-wise MCQ tests + general test",
                "syllabus": "NCERT-based, domain-specific subjects",
            }
        ],
        "preparation_strategy": [
            "Read foundational psychology texts to confirm genuine interest before committing",
            "Build strong English communication and empathetic listening skills",
            "Seek volunteering or shadowing opportunities at counseling centers during undergrad",
            "Pursue RCI-recognized M.Phil Clinical Psychology for licensed clinical practice",
        ],
        "best_books": ["Psychology - David G. Myers", "Introduction to Psychology - Morgan & King"],
        "online_resources": [{"name": "American Psychological Association (APA)", "type": "free", "url": "https://www.apa.org"}],
        "previous_year_papers": "https://cuet.samarth.ac.in",
        "top_colleges": ["Delhi University (Lady Shri Ram, Jesus & Mary)", "TISS Mumbai", "Christ University Bangalore"],
        "scholarships": ["UGC merit scholarships", "State minority scholarships"],
        "salary_range": {"entry": "₹3-6 LPA", "mid": "₹8-15 LPA", "senior": "₹20 LPA+ (established private practice)"},
        "career_growth": "Counselor → Clinical Psychologist → Senior Therapist → Private Practice / Academic Researcher.",
        "official_websites": ["https://cuet.samarth.ac.in", "https://rehabcouncil.nic.in"],
        "faqs": [{"q": "Can I practice clinically with just a Master's degree?", "a": "Independent clinical practice generally requires RCI licensure via M.Phil Clinical Psychology."}],
    },
    {
        "slug": "teacher-professor",
        "title": "Teacher / Professor",
        "category": "Education",
        "icon": "graduation-cap",
        "short_description": "Educate and mentor students at school, college, or university level.",
        "difficulty": "Easy",
        "streams": ["Arts", "Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Teachers and professors educate students across school and higher-education levels, requiring subject "
            "expertise combined with pedagogical training (B.Ed for schools, NET/Ph.D for colleges)."
        ),
        "required_qualifications": ["10+2 in relevant stream", "Bachelor's degree + B.Ed for school teaching", "Master's + UGC-NET/Ph.D for college/university teaching"],
        "entrance_exams": [
            {
                "name": "UGC-NET",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "Master's degree with minimum 55% marks",
                "age_limit": "No upper age limit for Assistant Professor eligibility",
                "attempts": "No cap; conducted twice a year",
                "selection_process": "CBT (2 papers) → Merit-based eligibility for Assistant Professor/JRF",
                "exam_pattern": "Paper 1 (General teaching/research aptitude) + Paper 2 (subject-specific)",
                "syllabus": "As prescribed by UGC for each subject",
            }
        ],
        "preparation_strategy": [
            "Build deep subject-matter expertise through your Master's degree coursework",
            "Practice previous years' NET papers for both General and subject papers",
            "Gain teaching experience through tutoring or teaching assistantships early",
            "Pursue a Ph.D. if aiming for research-focused university positions",
        ],
        "best_books": ["UGC-NET Paper 1 by Arihant Publications", "Subject-specific NET guides per discipline"],
        "online_resources": [{"name": "UGC-NET NTA Portal", "type": "free", "url": "https://ugcnet.nta.nic.in"}],
        "previous_year_papers": "https://ugcnet.nta.nic.in",
        "top_colleges": ["Delhi University", "Jawaharlal Nehru University", "Regional College of Education"],
        "scholarships": ["UGC JRF Fellowship", "State teacher training scholarships"],
        "salary_range": {"entry": "₹3-6 LPA (school)", "mid": "₹8-14 LPA (Assistant Professor)", "senior": "₹20 LPA+ (Professor/Principal)"},
        "career_growth": "Teacher/Assistant Professor → Senior Teacher/Associate Professor → Vice Principal/Professor → Principal/HOD/Dean.",
        "official_websites": ["https://ugcnet.nta.nic.in"],
        "faqs": [{"q": "Is B.Ed compulsory for school teaching?", "a": "Yes, for most government and recognized private schools in India."}],
    },
    {
        "slug": "journalist",
        "title": "Journalist",
        "category": "Media",
        "icon": "newspaper",
        "short_description": "Research, write, and report news across print, digital, and broadcast media.",
        "difficulty": "Easy",
        "streams": ["Arts", "Commerce", "Science"],
        "min_education": "12th",
        "overview": (
            "Journalists investigate, write, and report news stories across print, television, digital, and radio "
            "platforms, playing a key role in public information and accountability."
        ),
        "required_qualifications": ["10+2 in any stream", "BA/BJMC Journalism & Mass Communication (3 years)", "Optional: MA in Journalism for specialization"],
        "entrance_exams": [
            {
                "name": "IIMC Entrance Exam",
                "conducting_body": "Indian Institute of Mass Communication",
                "eligibility": "Graduation in any discipline",
                "age_limit": "No upper age limit",
                "attempts": "No cap",
                "selection_process": "Written test (GK, English, reasoning) → Interview",
                "exam_pattern": "Objective + descriptive sections on current affairs, language skills",
                "syllabus": "Current affairs, media awareness, English comprehension, general knowledge",
            }
        ],
        "preparation_strategy": [
            "Read multiple newspapers daily and practice summarizing stories concisely",
            "Build strong writing skills through blogging or campus publications",
            "Start a portfolio - internships with local news outlets or digital media add real value",
            "Learn basic video/audio editing tools for multimedia journalism roles",
        ],
        "best_books": ["News Reporting and Editing - M.V. Kamath", "The Elements of Journalism - Kovach & Rosenstiel"],
        "online_resources": [{"name": "Poynter.org", "type": "free", "url": "https://www.poynter.org"}],
        "previous_year_papers": "https://www.iimc.gov.in",
        "top_colleges": ["IIMC Delhi", "Symbiosis Institute of Media & Communication", "Xavier Institute of Communications"],
        "scholarships": ["IIMC merit scholarships", "Media house internship stipends"],
        "salary_range": {"entry": "₹3-5 LPA", "mid": "₹7-12 LPA", "senior": "₹18 LPA+ (senior editor/anchor)"},
        "career_growth": "Trainee Reporter → Correspondent → Senior Correspondent → Editor → Editor-in-Chief.",
        "official_websites": ["https://www.iimc.gov.in"],
        "faqs": [{"q": "Do I need a mass communication degree to become a journalist?", "a": "It helps, but strong writing and reporting skills combined with internships often matter more to employers."}],
    },
    {
        "slug": "product-manager",
        "title": "Product Manager",
        "category": "Business",
        "icon": "briefcase",
        "short_description": "Own the strategy, roadmap, and execution of a product across engineering, design, and business teams.",
        "difficulty": "Medium",
        "streams": ["Science", "Commerce"],
        "min_education": "Graduation",
        "overview": (
            "Product Managers sit at the intersection of business, technology, and user experience, driving what "
            "gets built and why. Most PMs transition in from engineering, design, or business/consulting backgrounds."
        ),
        "required_qualifications": ["Bachelor's degree (Engineering/Business preferred, not mandatory)", "Optional: MBA for strategic/senior PM roles"],
        "entrance_exams": [
            {
                "name": "CAT (for MBA route into Product Management)",
                "conducting_body": "IIMs (rotational)",
                "eligibility": "Bachelor's degree with minimum 50% marks",
                "age_limit": "No age limit",
                "attempts": "No cap, once a year",
                "selection_process": "CBT → Shortlisting → WAT/GD/PI at individual B-schools",
                "exam_pattern": "VARC, DILR, QA sections, 2 hours, objective + TITA",
                "syllabus": "Verbal ability, reading comprehension, data interpretation, logical reasoning, quantitative aptitude",
            }
        ],
        "preparation_strategy": [
            "Develop strong analytical and communication skills through case-study practice",
            "Learn product fundamentals: user research, prioritization frameworks, metrics",
            "Build a portfolio of case studies analyzing real products (teardown practice)",
            "Seek APM (Associate Product Manager) programs or intern in product/business roles",
        ],
        "best_books": ["Inspired - Marty Cagan", "Cracking the PM Interview - Gayle McDowell", "The Lean Startup - Eric Ries"],
        "online_resources": [{"name": "Product School Blog", "type": "free", "url": "https://productschool.com"}, {"name": "Lenny's Newsletter", "type": "freemium", "url": "https://www.lennysnewsletter.com"}],
        "previous_year_papers": "https://iimcat.ac.in",
        "top_colleges": ["IIM Ahmedabad", "IIM Bangalore", "ISB Hyderabad", "XLRI Jamshedpur"],
        "scholarships": ["IIM need-based scholarships", "Institute merit fee waivers"],
        "salary_range": {"entry": "₹10-18 LPA", "mid": "₹25-45 LPA", "senior": "₹60 LPA - ₹1.5 Cr+ (Director/VP Product)"},
        "career_growth": "APM → Product Manager → Senior PM → Group PM → Director of Product → VP/CPO.",
        "official_websites": ["https://iimcat.ac.in"],
        "faqs": [{"q": "Is an MBA required to become a Product Manager?", "a": "No, many PMs transition from engineering or design; MBA helps most for senior/strategic roles."}],
    },
    {
        "slug": "army-officer",
        "title": "Defence Officer (Army / Navy / Air Force)",
        "category": "Defence",
        "icon": "shield",
        "short_description": "Lead and serve in the Indian Armed Forces - Army, Navy, or Air Force - across combat, technical, and administrative roles.",
        "difficulty": "Hard",
        "streams": ["Science", "Arts", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Officers in the Indian Armed Forces lead troops, manage operations, and serve the nation across "
            "combat, technical, and administrative roles in the Army, Navy, or Air Force. There are three main "
            "entry routes depending on your stage of education: NDA straight after 12th (tri-service - Army, "
            "Navy, and Air Force wings all recruit through it), CDS after graduation (Army/Navy/Air Force), and "
            "AFCAT specifically for the Air Force (flying, technical, and ground duty branches) after graduation."
        ),
        "required_qualifications": [
            "10+2 with PCM (for NDA Air Force/Navy technical entries) or any stream (NDA Army non-technical entry)",
            "Graduation in any discipline (for CDS - Army/Navy/Air Force) or with Physics & Maths (for some AFCAT technical branches)",
            "Graduation with 60% (for AFCAT flying branch, plus specific Physics/Maths criteria)",
        ],
        "entrance_exams": [
            {
                "name": "NDA (National Defence Academy) Exam",
                "conducting_body": "Union Public Service Commission (UPSC)",
                "eligibility": "10+2 pass, unmarried candidates, 16.5-19.5 years",
                "age_limit": "16.5 to 19.5 years",
                "attempts": "Twice a year exam; multiple attempts within age bracket",
                "selection_process": "Written exam → SSB Interview (5 days) → Medical Test → Merit list → Joint training at NDA, then service-specific academy",
                "exam_pattern": "Mathematics (300 marks) + General Ability Test (600 marks), objective",
                "syllabus": "Class 11-12 Mathematics, English, General Science, History, Geography, Current Affairs",
            },
            {
                "name": "CDS (Combined Defence Services) Exam",
                "conducting_body": "Union Public Service Commission (UPSC)",
                "eligibility": "Graduate in any discipline (engineering degree for technical entries); unmarried for most entries",
                "age_limit": "19-25 years (varies slightly by wing/entry - IMA, INA, AFA, OTA)",
                "attempts": "Twice a year exam; multiple attempts within age bracket",
                "selection_process": "Written exam → SSB Interview → Medical Test → Merit list → Training at IMA/INA/AFA/OTA",
                "exam_pattern": "English, General Knowledge, Elementary Mathematics (objective) - paper combination varies by entry",
                "syllabus": "Graduate-level General Knowledge and current affairs, Class 10 level Mathematics, English comprehension",
            },
            {
                "name": "AFCAT (Air Force Common Admission Test)",
                "conducting_body": "Indian Air Force",
                "eligibility": "Graduate in any discipline (Flying branch); specific engineering degree for Technical branch; 60% aggregate typically required",
                "age_limit": "20-24 years for Flying branch (up to 26 for some technical/ground duty branches)",
                "attempts": "Twice a year exam (Feb and Aug/Sep cycles); no cap on number of attempts within age limit",
                "selection_process": "Written exam → AFSB Interview (5 days, includes PABT for flying branch) → Medical Test → Merit list → Training at Air Force Academy",
                "exam_pattern": "General Awareness, Verbal Ability, Numerical Ability, Reasoning & Military Aptitude (objective, 100 questions)",
                "syllabus": "Graduate-level general awareness, reasoning, and English; basic aviation/military aptitude",
            },
        ],
        "preparation_strategy": [
            "Maintain excellent physical fitness alongside academics - both matter heavily for selection",
            "Practice Mathematics and General Ability Test papers extensively for NDA; focus on GK and reasoning speed for CDS/AFCAT",
            "Prepare specifically for the SSB/AFSB interview - group tasks, psychological tests, personal interview - this eliminates most candidates, not the written exam alone",
            "For AFCAT Flying branch, start practicing for PABT (Pilot Aptitude Battery Test) well in advance",
            "Stay updated on current national and defence-related affairs across all three exams",
        ],
        "best_books": [
            "NDA/NA Guide - Pathfinder Publications",
            "Mathematics for NDA - R.S. Aggarwal",
            "CDS Pathfinder - Arihant Publications",
            "AFCAT Guide - Pathfinder/Arihant Publications",
        ],
        "online_resources": [
            {"name": "UPSC Official Notifications (NDA/CDS)", "type": "free", "url": "https://upsc.gov.in"},
            {"name": "Indian Air Force AFCAT Portal", "type": "free", "url": "https://afcat.cdac.in"},
            {"name": "Join Indian Army/Navy/Air Force", "type": "free", "url": "https://joinindianarmy.nic.in"},
        ],
        "previous_year_papers": "https://upsc.gov.in",
        "top_colleges": [
            "National Defence Academy, Khadakwasla",
            "Indian Military Academy, Dehradun",
            "Air Force Academy, Hyderabad",
            "Indian Naval Academy, Ezhimala",
            "Officers Training Academy, Chennai",
        ],
        "scholarships": ["Fully funded training - Armed Forces cover education and stipend during training for all three services"],
        "salary_range": {"entry": "₹56,100/month (Level 10) + allowances", "mid": "₹1,21,200+/month (Lt Col / equivalent)", "senior": "₹2,25,000+/month (Brigadier & above / equivalent)"},
        "career_growth": "Lieutenant/Flying Officer/Sub-Lieutenant → Captain/Flight Lieutenant/Lieutenant → Major/Squadron Leader/Lt Commander → Lt Colonel/Wing Commander/Commander → Colonel/Group Captain/Captain → Brigadier/Air Commodore/Commodore → General/Air Marshal/Admiral ranks.",
        "official_websites": ["https://upsc.gov.in", "https://joinindianarmy.nic.in", "https://afcat.cdac.in", "https://www.joinindiannavy.gov.in"],
        "faqs": [
            {"q": "Can girls apply for NDA and AFCAT?", "a": "Yes, NDA has been open to female candidates since 2022, and AFCAT has long welcomed women across most branches."},
            {"q": "What's the difference between NDA, CDS, and AFCAT?", "a": "NDA is for candidates straight after 12th grade (joint Army/Navy/Air Force training); CDS is for graduates entering the Army, Navy, or Air Force; AFCAT is specifically for graduates entering the Air Force only."},
            {"q": "Which entry is best for the Navy specifically?", "a": "NDA (Navy wing) after 12th, or CDS (Naval Academy entry) after graduation are the two direct routes into the Indian Navy as an officer."},
        ],
    },
    {
        "slug": "state-civil-services",
        "title": "State Civil Services Officer (MPSC / State PSC)",
        "category": "Government",
        "icon": "landmark",
        "short_description": "Administer state-level governance and public welfare through State Public Service Commission exams like MPSC.",
        "difficulty": "Very Hard",
        "streams": ["Arts", "Science", "Commerce"],
        "min_education": "Graduation",
        "overview": (
            "State Civil Services Officers hold administrative, revenue, and police leadership positions within "
            "a specific state government, recruited through that state's Public Service Commission - for "
            "example, MPSC (Maharashtra), UPPSC (Uttar Pradesh), BPSC (Bihar), or similar bodies in other "
            "states. The structure and exam pattern closely mirror the UPSC Civil Services Examination but at "
            "state level, and roles include Deputy Collector, Deputy SP, Tehsildar, and other state cadre posts."
        ),
        "required_qualifications": [
            "Bachelor's degree in any discipline from a recognized university",
            "Domicile/residency requirements vary by state - check the specific state PSC's eligibility rules",
        ],
        "entrance_exams": [
            {
                "name": "MPSC (Maharashtra Public Service Commission) - State Services Exam",
                "conducting_body": "Maharashtra Public Service Commission (equivalent commissions exist in every state)",
                "eligibility": "Graduate in any stream; Maharashtra domicile requirements typically apply",
                "age_limit": "19-38 years for General category (relaxation for reserved categories)",
                "attempts": "Multiple attempts allowed within the age limit",
                "selection_process": "Prelims (objective, screening) → Mains (descriptive) → Interview → Merit list",
                "exam_pattern": "Prelims: 2 papers (GS + CSAT); Mains: multiple descriptive papers depending on the post",
                "syllabus": "State and national History, Polity, Geography, Economy, Current Affairs, plus state-specific subjects (e.g. Maharashtra-specific GK for MPSC)",
            }
        ],
        "preparation_strategy": [
            "Build the same NCERT-level foundation used for UPSC (History, Polity, Geography, Economy) - it transfers directly",
            "Add dedicated study of your specific state's geography, history, culture, and current affairs - this is weighted heavily and often decides selection",
            "Practice previous years' papers of your specific state PSC, since exam pattern/weightage varies state to state",
            "Join state-specific test series rather than only generic UPSC-focused ones",
        ],
        "best_books": [
            "State PSC-specific GK compendiums (e.g. MPSC/UPPSC/BPSC guides from local publishers)",
            "NCERT Class 6-12 (all social science subjects) - same base as UPSC prep",
            "Indian Polity - M. Laxmikanth",
            "State board textbooks for state-specific History/Geography sections",
        ],
        "online_resources": [
            {"name": "MPSC Official Portal", "type": "free", "url": "https://mpsc.gov.in"},
            {"name": "State PSC Notifications Aggregator", "type": "free", "url": "https://www.sarkariresult.com"},
            {"name": "Unacademy State PSC", "type": "paid", "url": "https://unacademy.com"},
        ],
        "previous_year_papers": "https://mpsc.gov.in",
        "top_colleges": ["No specific college required; coaching institutes offering state PSC-focused programs are common in most state capitals"],
        "scholarships": ["State government pre-exam training scholarships for SC/ST/OBC/minority candidates (varies by state)"],
        "salary_range": {"entry": "₹40,000-56,000/month + allowances", "mid": "₹80,000-1,20,000/month", "senior": "₹1,50,000+/month (senior state cadre posts)"},
        "career_growth": "Deputy Tehsildar/Assistant → Tehsildar/Deputy SP → Sub-Divisional Officer → District-level officer → Divisional/state-level senior administrative posts.",
        "official_websites": ["https://mpsc.gov.in"],
        "faqs": [
            {"q": "How is State PSC different from UPSC Civil Services?", "a": "UPSC recruits for central services (IAS, IPS, IFS) with all-India postings; State PSCs recruit for that specific state's administrative cadre, generally with domicile requirements and state-specific syllabus weightage."},
            {"q": "Can I prepare for UPSC and State PSC together?", "a": "Yes, the core subjects overlap significantly - most candidates prepare for both simultaneously and add state-specific topics as a supplement."},
        ],
    },
    {
        "slug": "ssc-government-officer",
        "title": "SSC Government Officer (CGL / CHSL)",
        "category": "Government",
        "icon": "landmark",
        "short_description": "Secure a central government job in tax, audit, inspection, or clerical roles via the Staff Selection Commission.",
        "difficulty": "Medium",
        "streams": ["Arts", "Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "The Staff Selection Commission (SSC) recruits for a wide range of Group B and Group C posts across "
            "central government ministries and departments - Income Tax Inspector, Central Excise Inspector, "
            "Assistant Section Officer, Auditor, and many more - through exams like SSC CGL (graduate-level) and "
            "SSC CHSL (10+2 level). It's one of the most popular entry points into government service due to "
            "its relatively shorter, single-year preparation cycle compared to UPSC."
        ),
        "required_qualifications": [
            "10+2 pass for SSC CHSL (Combined Higher Secondary Level) posts",
            "Bachelor's degree in any discipline for SSC CGL (Combined Graduate Level) posts",
        ],
        "entrance_exams": [
            {
                "name": "SSC CGL (Combined Graduate Level)",
                "conducting_body": "Staff Selection Commission (SSC)",
                "eligibility": "Graduate in any discipline from a recognized university",
                "age_limit": "18-32 years (varies by specific post; relaxation for reserved categories)",
                "attempts": "No cap on number of attempts within the age limit",
                "selection_process": "Tier 1 (objective, CBT) → Tier 2 (objective, CBT) → Document verification → Merit list by post",
                "exam_pattern": "Tier 1: General Intelligence, General Awareness, Quantitative Aptitude, English (200 marks); Tier 2: subject-specific papers depending on post applied for",
                "syllabus": "Class 10-12 level Mathematics and English, general awareness/current affairs, reasoning",
            },
            {
                "name": "SSC CHSL (Combined Higher Secondary Level)",
                "conducting_body": "Staff Selection Commission (SSC)",
                "eligibility": "10+2 pass from a recognized board",
                "age_limit": "18-27 years (relaxation for reserved categories)",
                "attempts": "No cap on number of attempts within the age limit",
                "selection_process": "Tier 1 (objective, CBT) → Tier 2 (descriptive + skill test where applicable) → Merit list",
                "exam_pattern": "Tier 1: General Intelligence, English, Quantitative Aptitude, General Awareness (200 marks)",
                "syllabus": "Class 10-12 level Mathematics and English, general awareness, reasoning",
            },
        ],
        "preparation_strategy": [
            "Focus heavily on speed and accuracy for Quantitative Aptitude and Reasoning - these are the biggest score differentiators",
            "Build a daily current affairs habit at least 6 months before the exam",
            "Practice previous years' papers extensively - SSC exams reuse question patterns/styles often",
            "Take regular sectional and full-length mock tests to build exam-day time management",
        ],
        "best_books": [
            "Kiran's SSC CGL Previous Year Papers",
            "Quantitative Aptitude - R.S. Aggarwal",
            "A Modern Approach to Verbal & Non-Verbal Reasoning - R.S. Aggarwal",
            "Lucent's General Knowledge",
        ],
        "online_resources": [
            {"name": "SSC Official Portal", "type": "free", "url": "https://ssc.nic.in"},
            {"name": "Adda247 SSC", "type": "freemium", "url": "https://www.adda247.com"},
            {"name": "Testbook SSC Test Series", "type": "paid", "url": "https://testbook.com"},
        ],
        "previous_year_papers": "https://ssc.nic.in",
        "top_colleges": ["No specific college required; SSC coaching institutes are widely available both online and offline"],
        "scholarships": ["Not applicable - this is a direct recruitment exam rather than an academic program"],
        "salary_range": {"entry": "₹25,000-35,000/month + allowances (Group C/B posts)", "mid": "₹47,000-1,00,000/month", "senior": "₹1,50,000+/month (senior Group B/A posts after promotion)"},
        "career_growth": "Inspector/Assistant (entry Group B/C) → Senior posts within department via departmental promotion exams → Gazetted officer ranks with sufficient seniority and further exams.",
        "official_websites": ["https://ssc.nic.in"],
        "faqs": [
            {"q": "What's the difference between SSC CGL and SSC CHSL?", "a": "CGL is for graduate-level posts (higher pay scale, e.g. Inspector-level roles); CHSL is for 10+2-level posts (e.g. Lower Divisional Clerk, Data Entry Operator)."},
            {"q": "Is SSC CGL easier than UPSC?", "a": "The preparation cycle is generally shorter (6-12 months vs 1-2+ years for UPSC), and competition, while intense, is considered somewhat less extreme than UPSC Civil Services - but it still requires serious, consistent preparation."},
        ],
    },
    {
        "slug": "pharmacist",
        "title": "Pharmacist",
        "category": "Healthcare",
        "icon": "pill",
        "short_description": "Dispense medications, advise on drug usage, and support healthcare delivery.",
        "difficulty": "Medium",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Pharmacists ensure the safe dispensing and use of medications, working in hospitals, retail pharmacies, "
            "pharmaceutical companies, or regulatory bodies."
        ),
        "required_qualifications": ["10+2 with Physics, Chemistry, Biology/Mathematics", "B.Pharm (4 years) or D.Pharm (2 years diploma)", "Optional: M.Pharm/Pharm.D for specialization"],
        "entrance_exams": [
            {
                "name": "GPAT (Graduate Pharmacy Aptitude Test)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "B.Pharm degree for GPAT (M.Pharm admission); state exams for B.Pharm entry",
                "age_limit": "No upper age limit",
                "attempts": "No cap",
                "selection_process": "CBT → Merit list → Institute counselling",
                "exam_pattern": "125 MCQs, 3 hours, covering pharmaceutical subjects",
                "syllabus": "Pharmaceutics, Pharmacology, Pharmaceutical Chemistry, Pharmacognosy",
            }
        ],
        "preparation_strategy": [
            "Build strong fundamentals in Chemistry and Biology during 11th-12th grade",
            "Focus on pharmacology and pharmaceutical chemistry concepts during B.Pharm",
            "Take up hospital or industry internships to gain practical exposure",
            "Prepare for GPAT with previous years' papers if pursuing M.Pharm",
        ],
        "best_books": ["NCERT Chemistry & Biology (Class 11-12)", "Pharmaceutical Chemistry - textbooks per curriculum"],
        "online_resources": [{"name": "PCI Official Portal", "type": "free", "url": "https://www.pci.nic.in"}],
        "previous_year_papers": "https://gpat.nta.nic.in",
        "top_colleges": ["NIPER Mohali", "Jamia Hamdard", "Manipal College of Pharmaceutical Sciences"],
        "scholarships": ["AICTE Pragati Scholarship for girls", "State pharmacy council scholarships"],
        "salary_range": {"entry": "₹2.5-5 LPA", "mid": "₹6-12 LPA", "senior": "₹18 LPA+ (regulatory/industry lead)"},
        "career_growth": "Pharmacist → Senior Pharmacist → Pharmacy Manager → Regulatory Affairs Lead / Own Pharmacy.",
        "official_websites": ["https://www.pci.nic.in", "https://gpat.nta.nic.in"],
        "faqs": [{"q": "Is D.Pharm enough to open a pharmacy?", "a": "Yes, D.Pharm with state pharmacy council registration is sufficient to practice as a registered pharmacist."}],
    },
{
        "slug": "cybersecurity-analyst",
        "title": "Cybersecurity Analyst",
        "category": "Technology",
        "icon": "shield",
        "short_description": "Protect systems, networks, and data from cyber threats through monitoring, defense, and incident response.",
        "difficulty": "Medium",
        "streams": ["Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Cybersecurity Analysts defend organizations against hacking, malware, and data breaches by "
            "monitoring networks, investigating incidents, and hardening systems. Demand has grown sharply as "
            "companies digitize, making this one of the fastest-growing specializations within tech."
        ),
        "required_qualifications": [
            "10+2 with PCM (for engineering route) or any stream (for direct certification route)",
            "B.Tech/B.Sc in Computer Science, IT, or Cybersecurity (3-4 years)",
            "Industry certifications (CompTIA Security+, CEH, CISSP) significantly boost employability",
        ],
        "entrance_exams": [
            {
                "name": "JEE Main (for B.Tech Cybersecurity/CS programs)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with Physics, Chemistry/Informatics, Mathematics",
                "age_limit": "No upper age limit",
                "attempts": "2 attempts per year",
                "selection_process": "CBT → Merit list → Counselling",
                "exam_pattern": "90 questions, 300 marks, 3 hours",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics",
            }
        ],
        "preparation_strategy": [
            "Build strong networking and operating systems fundamentals (TCP/IP, Linux) early",
            "Practice on platforms like TryHackMe or Hack The Box to build hands-on skills",
            "Earn CompTIA Security+ or CEH as an accessible first certification",
            "Participate in Capture The Flag (CTF) competitions to build a practical portfolio",
        ],
        "best_books": ["CompTIA Security+ Study Guide - Mike Chapple", "The Web Application Hacker's Handbook", "Hacking: The Art of Exploitation - Jon Erickson"],
        "online_resources": [
            {"name": "TryHackMe", "type": "freemium", "url": "https://tryhackme.com"},
            {"name": "Hack The Box", "type": "freemium", "url": "https://www.hackthebox.com"},
            {"name": "Cybrary", "type": "freemium", "url": "https://www.cybrary.it"},
        ],
        "previous_year_papers": "https://jeemain.nta.nic.in",
        "top_colleges": ["IIT Kanpur (Cybersecurity specialization)", "IIIT Hyderabad", "Amrita Vishwa Vidyapeetham"],
        "scholarships": ["National Merit Scholarship", "AICTE Pragati Scholarship"],
        "salary_range": {"entry": "₹5-9 LPA", "mid": "₹14-25 LPA", "senior": "₹35 LPA+ (CISO/security architect)"},
        "career_growth": "Security Analyst → Senior Analyst → Security Engineer → Security Architect → CISO (Chief Information Security Officer).",
        "official_websites": ["https://jeemain.nta.nic.in"],
        "faqs": [
            {"q": "Do I need a degree, or are certifications enough?", "a": "A degree helps for entry-level hiring filters, but certifications (Security+, CEH, OSCP) often matter more for actual cybersecurity roles and career progression."},
        ],
    },
    {
        "slug": "cloud-devops-engineer",
        "title": "Cloud / DevOps Engineer",
        "category": "Technology",
        "icon": "cog",
        "short_description": "Build and manage the infrastructure, automation, and deployment pipelines that keep software running reliably.",
        "difficulty": "Medium",
        "streams": ["Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Cloud/DevOps Engineers manage cloud infrastructure (AWS, Azure, GCP), build CI/CD pipelines, and "
            "ensure applications deploy and scale reliably. It's a high-demand specialization that blends "
            "software engineering with systems administration."
        ),
        "required_qualifications": [
            "10+2 with Mathematics",
            "B.Tech/B.Sc in Computer Science or IT (3-4 years)",
            "Cloud certifications (AWS Certified Solutions Architect, Azure Administrator) strongly valued",
        ],
        "entrance_exams": [
            {
                "name": "JEE Main (for B.Tech CS/IT programs)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with Physics, Chemistry/Informatics, Mathematics",
                "age_limit": "No upper age limit",
                "attempts": "2 attempts per year",
                "selection_process": "CBT → Merit list → Counselling",
                "exam_pattern": "90 questions, 300 marks, 3 hours",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics",
            }
        ],
        "preparation_strategy": [
            "Learn Linux fundamentals and shell scripting thoroughly",
            "Get hands-on with Docker, Kubernetes, and a major cloud provider's free tier",
            "Build CI/CD pipelines for personal projects using GitHub Actions or Jenkins",
            "Pursue an entry-level cloud certification (AWS Cloud Practitioner) as a first milestone",
        ],
        "best_books": ["The Phoenix Project - Gene Kim", "Kubernetes Up & Running", "AWS Certified Solutions Architect Study Guide"],
        "online_resources": [
            {"name": "AWS Free Tier + Training", "type": "freemium", "url": "https://aws.amazon.com/training"},
            {"name": "Kubernetes Official Docs", "type": "free", "url": "https://kubernetes.io/docs"},
            {"name": "KodeKloud", "type": "paid", "url": "https://kodekloud.com"},
        ],
        "previous_year_papers": "https://jeemain.nta.nic.in",
        "top_colleges": ["IIT Bombay", "IIIT Bangalore", "BITS Pilani"],
        "scholarships": ["National Merit Scholarship", "AICTE Pragati Scholarship"],
        "salary_range": {"entry": "₹5-9 LPA", "mid": "₹15-28 LPA", "senior": "₹35 LPA+ (principal/staff engineer)"},
        "career_growth": "DevOps Engineer → Senior DevOps Engineer → Cloud Architect → Principal Engineer / Head of Infrastructure.",
        "official_websites": ["https://jeemain.nta.nic.in"],
        "faqs": [
            {"q": "Which cloud provider should I learn first?", "a": "AWS has the largest market share and job demand in India, making it the most practical starting point, though Azure and GCP skills are also valuable."},
        ],
    },
    {
        "slug": "dentist",
        "title": "Dentist (BDS)",
        "category": "Medicine",
        "icon": "stethoscope",
        "short_description": "Diagnose and treat conditions of the teeth, gums, and oral cavity.",
        "difficulty": "Hard",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Dentists diagnose and treat oral health issues, from cavities to complex jaw surgeries. Entry is via "
            "the same NEET-UG exam as MBBS, followed by a 5-year BDS program including a mandatory internship."
        ),
        "required_qualifications": [
            "10+2 with Physics, Chemistry, Biology (PCB), minimum 50% aggregate (40% for reserved categories)",
            "BDS - 4 years academic + 1 year compulsory rotating internship",
            "Optional: MDS (3 years) for specialization (orthodontics, oral surgery, etc.)",
        ],
        "entrance_exams": [
            {
                "name": "NEET-UG",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with PCB, minimum age 17 years by admission year",
                "age_limit": "No upper age limit",
                "attempts": "No official cap on number of attempts",
                "selection_process": "Single national exam → Merit lists → Counselling (MCC/state) for BDS seats",
                "exam_pattern": "200 questions (180 to attempt), 720 marks, 3 hours 20 minutes",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Biology (NCERT-based)",
            }
        ],
        "preparation_strategy": [
            "Preparation is identical to MBBS aspirants - NEET is the common gateway for both",
            "Master NCERT Biology thoroughly since it carries the highest weightage",
            "Take regular full-length mock tests to build stamina for the 3+ hour exam",
            "During BDS, build strong hands-on clinical skills through consistent practical/lab attendance",
        ],
        "best_books": ["NCERT Biology, Physics, Chemistry (Class 11 & 12)", "Trueman's Elementary Biology", "MTG NEET Objective Books"],
        "online_resources": [
            {"name": "NEET NTA Official Portal", "type": "free", "url": "https://neet.nta.nic.in"},
            {"name": "Physics Wallah", "type": "freemium", "url": "https://www.pw.live"},
        ],
        "previous_year_papers": "https://neet.nta.nic.in",
        "top_colleges": ["Maulana Azad Institute of Dental Sciences", "Manipal College of Dental Sciences", "Government Dental College, Mumbai"],
        "scholarships": ["Central Sector Scholarship", "State Merit-cum-Means Scholarships"],
        "salary_range": {"entry": "₹4-7 LPA", "mid": "₹10-20 LPA", "senior": "₹25 LPA+ (specialist/own clinic)"},
        "career_growth": "Intern → Junior Dentist → Specialist (post-MDS) → Senior Consultant / Own Dental Practice.",
        "official_websites": ["https://neet.nta.nic.in", "https://dciindia.gov.in"],
        "faqs": [
            {"q": "Is BDS less competitive than MBBS?", "a": "Generally yes - BDS cutoffs on NEET are typically lower than MBBS, though top dental colleges remain highly competitive."},
        ],
    },
    {
        "slug": "nurse",
        "title": "Nurse (B.Sc Nursing)",
        "category": "Medicine",
        "icon": "stethoscope",
        "short_description": "Provide direct patient care, support treatment plans, and serve as a critical link between patients and doctors.",
        "difficulty": "Medium",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Nurses provide hands-on patient care, administer treatment, and support doctors across hospitals, "
            "clinics, and community health settings. It's a stable, in-demand profession both in India and "
            "internationally, with strong opportunities for those willing to relocate abroad."
        ),
        "required_qualifications": [
            "10+2 with Physics, Chemistry, Biology (PCB), minimum 45-50% aggregate",
            "B.Sc Nursing (4 years) or GNM Diploma (3.5 years)",
            "Registration with State Nursing Council to practice",
        ],
        "entrance_exams": [
            {
                "name": "NEET-UG (increasingly required for B.Sc Nursing admissions)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with PCB",
                "age_limit": "No upper age limit",
                "attempts": "No official cap on number of attempts",
                "selection_process": "NEET score → State/institute-specific counselling for nursing seats",
                "exam_pattern": "200 questions (180 to attempt), 720 marks, 3 hours 20 minutes",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Biology (NCERT-based)",
            }
        ],
        "preparation_strategy": [
            "Follow the same NEET Biology-focused preparation as MBBS/BDS aspirants",
            "Build genuine interest through hospital volunteering or shadowing if possible before committing",
            "During the program, focus heavily on practical clinical postings, not just theory",
            "Consider international licensing exams (NCLEX-RN for the US, OET for UK/Australia) early if aiming to work abroad",
        ],
        "best_books": ["NCERT Biology, Physics, Chemistry (Class 11 & 12)", "Trueman's Elementary Biology"],
        "online_resources": [
            {"name": "Indian Nursing Council Portal", "type": "free", "url": "https://www.indiannursingcouncil.org"},
            {"name": "NEET NTA Official Portal", "type": "free", "url": "https://neet.nta.nic.in"},
        ],
        "previous_year_papers": "https://neet.nta.nic.in",
        "top_colleges": ["AIIMS College of Nursing, New Delhi", "CMC Vellore College of Nursing", "RAK College of Nursing"],
        "scholarships": ["Central Sector Scholarship", "State nursing scholarships for economically weaker sections"],
        "salary_range": {"entry": "₹2.5-4.5 LPA", "mid": "₹6-10 LPA", "senior": "₹15 LPA+ (nursing superintendent / abroad postings)"},
        "career_growth": "Staff Nurse → Senior Nurse → Nursing Supervisor → Nursing Superintendent / Specialist Nurse (ICU, OT).",
        "official_websites": ["https://www.indiannursingcouncil.org", "https://neet.nta.nic.in"],
        "faqs": [
            {"q": "Is nursing a good option for working abroad?", "a": "Yes, Indian-trained nurses are in high demand in the Gulf, UK, and other countries, though additional licensing exams (like OET or NCLEX) are usually required."},
        ],
    },
    {
        "slug": "physiotherapist",
        "title": "Physiotherapist (BPT)",
        "category": "Healthcare",
        "icon": "stethoscope",
        "short_description": "Help patients recover movement and function through therapeutic exercise and manual treatment.",
        "difficulty": "Medium",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Physiotherapists help patients recover from injury, surgery, or chronic conditions through movement-based "
            "treatment. Growing awareness of sports medicine and an aging population are driving strong demand "
            "for this profession in India."
        ),
        "required_qualifications": [
            "10+2 with Physics, Chemistry, Biology (PCB), minimum 50% aggregate",
            "BPT - Bachelor of Physiotherapy (4.5 years including internship)",
            "Optional: MPT (2 years) for specialization (sports, neuro, ortho physiotherapy)",
        ],
        "entrance_exams": [
            {
                "name": "State/University-level Physiotherapy Entrance Exams (varies by state)",
                "conducting_body": "State authorities or individual universities",
                "eligibility": "10+2 with PCB",
                "age_limit": "No upper age limit typically",
                "attempts": "Varies by conducting body",
                "selection_process": "Entrance test or merit-based (12th percentage) → Counselling",
                "exam_pattern": "Varies - many institutes admit directly based on 12th grade Biology/PCB marks",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Biology",
            }
        ],
        "preparation_strategy": [
            "Focus on strong 12th grade Biology and Physics scores, since many programs admit on merit",
            "Build genuine interest in anatomy and human movement through early exposure if possible",
            "During BPT, prioritize hands-on clinical postings and patient interaction",
            "Consider a specialization (sports physiotherapy, neuro-rehab) early to differentiate your career",
        ],
        "best_books": ["NCERT Biology (Class 11-12)", "Textbook of Anatomy & Physiology for Physiotherapy students"],
        "online_resources": [{"name": "Indian Association of Physiotherapists", "type": "free", "url": "https://www.iaphysio.org"}],
        "previous_year_papers": "https://www.iaphysio.org",
        "top_colleges": ["Maulana Azad Medical College (Physiotherapy)", "Manipal College of Health Professions", "Christian Medical College, Vellore"],
        "scholarships": ["State merit scholarships", "AICTE Pragati Scholarship for girls"],
        "salary_range": {"entry": "₹2.5-4.5 LPA", "mid": "₹6-10 LPA", "senior": "₹15 LPA+ (own clinic / sports team physio)"},
        "career_growth": "Junior Physiotherapist → Senior Physiotherapist → Clinic Lead → Own Practice / Specialist Consultant (sports teams, hospitals).",
        "official_websites": ["https://www.iaphysio.org"],
        "faqs": [
            {"q": "Can physiotherapists work with sports teams?", "a": "Yes, sports physiotherapy is a growing specialization, with opportunities working alongside athletes and sports academies after an MPT specialization."},
        ],
    },
    {
        "slug": "civil-engineer",
        "title": "Civil Engineer",
        "category": "Engineering",
        "icon": "building",
        "short_description": "Design, construct, and maintain infrastructure like buildings, roads, bridges, and water systems.",
        "difficulty": "Medium",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Civil Engineers plan and oversee construction of infrastructure - buildings, roads, bridges, dams, "
            "and water systems. It remains one of the most stable, foundational engineering disciplines with "
            "consistent demand from both government infrastructure projects and private construction."
        ),
        "required_qualifications": ["10+2 with PCM", "B.Tech/B.E. Civil Engineering (4 years)", "Optional: M.Tech for specialization; GATE for PSU/higher studies"],
        "entrance_exams": [
            {
                "name": "JEE Main",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with Physics, Chemistry, Mathematics",
                "age_limit": "No upper age limit",
                "attempts": "2 attempts per year",
                "selection_process": "CBT → Merit list → JoSAA/state counselling",
                "exam_pattern": "90 questions, 300 marks, 3 hours",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics",
            }
        ],
        "preparation_strategy": [
            "Build strong fundamentals in Physics (mechanics, fluid dynamics) and Mathematics",
            "Develop practical site-visit exposure during internships to complement classroom learning",
            "Learn AutoCAD and structural design software (STAAD Pro) during undergraduate studies",
            "Consider GATE preparation in final year if targeting PSU jobs or M.Tech",
        ],
        "best_books": ["NCERT Physics, Chemistry, Mathematics", "Concepts of Physics - H.C. Verma", "Building Construction - Sushil Kumar"],
        "online_resources": [{"name": "NPTEL Civil Engineering Courses", "type": "free", "url": "https://nptel.ac.in"}],
        "previous_year_papers": "https://jeemain.nta.nic.in",
        "top_colleges": ["IIT Roorkee", "IIT Delhi", "NIT Surathkal", "Jadavpur University"],
        "scholarships": ["National Merit Scholarship", "AICTE Pragati Scholarship"],
        "salary_range": {"entry": "₹3.5-6 LPA", "mid": "₹9-16 LPA", "senior": "₹22 LPA+ (project manager/PSU senior roles)"},
        "career_growth": "Site Engineer → Project Engineer → Senior Engineer → Project Manager → General Manager/Director.",
        "official_websites": ["https://jeemain.nta.nic.in"],
        "faqs": [{"q": "Is GATE necessary after B.Tech Civil?", "a": "Only if pursuing M.Tech or applying to PSUs like NHAI/DMRC; private-sector core jobs don't require it."}],
    },
    {
        "slug": "electrical-electronics-engineer",
        "title": "Electrical & Electronics Engineer",
        "category": "Engineering",
        "icon": "cog",
        "short_description": "Design and develop electrical systems, power infrastructure, and electronic devices.",
        "difficulty": "Medium",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Electrical & Electronics Engineers design power systems, circuits, and electronic devices - spanning "
            "power grids, renewable energy, consumer electronics, and semiconductor design. It's a broad "
            "discipline with strong demand across manufacturing, energy, and hardware tech companies."
        ),
        "required_qualifications": ["10+2 with PCM", "B.Tech/B.E. Electrical or Electronics Engineering (4 years)", "Optional: M.Tech for VLSI/power systems specialization"],
        "entrance_exams": [
            {
                "name": "JEE Main",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 with Physics, Chemistry, Mathematics",
                "age_limit": "No upper age limit",
                "attempts": "2 attempts per year",
                "selection_process": "CBT → Merit list → JoSAA/state counselling",
                "exam_pattern": "90 questions, 300 marks, 3 hours",
                "syllabus": "Class 11 & 12 Physics, Chemistry, Mathematics",
            }
        ],
        "preparation_strategy": [
            "Build strong fundamentals in Physics, especially electromagnetism and circuits",
            "Get hands-on with basic circuit-building and Arduino/microcontroller projects early",
            "Learn simulation tools (MATLAB, Simulink) during undergraduate studies",
            "Consider GATE preparation if targeting PSU jobs (power sector) or M.Tech",
        ],
        "best_books": ["NCERT Physics, Chemistry, Mathematics", "Concepts of Physics - H.C. Verma", "Basic Electrical Engineering - V.K. Mehta"],
        "online_resources": [{"name": "NPTEL Electrical Engineering Courses", "type": "free", "url": "https://nptel.ac.in"}],
        "previous_year_papers": "https://jeemain.nta.nic.in",
        "top_colleges": ["IIT Bombay", "IIT Kanpur", "NIT Warangal", "BITS Pilani"],
        "scholarships": ["National Merit Scholarship", "AICTE Pragati Scholarship"],
        "salary_range": {"entry": "₹4-7 LPA", "mid": "₹10-18 LPA", "senior": "₹25 LPA+ (senior engineer/PSU leadership)"},
        "career_growth": "Graduate Engineer Trainee → Design Engineer → Senior Engineer → Engineering Manager → GM/Technical Director.",
        "official_websites": ["https://jeemain.nta.nic.in"],
        "faqs": [{"q": "What's the difference between Electrical and Electronics Engineering?", "a": "Electrical Engineering focuses more on power systems and machines; Electronics Engineering focuses more on circuits, semiconductors, and communication systems - many colleges offer a combined EEE program covering both."}],
    },
    {
        "slug": "company-secretary",
        "title": "Company Secretary (CS)",
        "category": "Finance",
        "icon": "briefcase",
        "short_description": "Ensure corporate governance, legal compliance, and effective board-level administration for companies.",
        "difficulty": "Hard",
        "streams": ["Commerce", "Arts", "Science"],
        "min_education": "12th",
        "overview": (
            "Company Secretaries ensure companies comply with corporate law, manage board processes, and advise "
            "on governance matters. The CS qualification is administered by ICSI through three stages - "
            "Foundation, Executive, and Professional - combined with practical training."
        ),
        "required_qualifications": [
            "10+2 in any stream (Commerce preferred but not mandatory)",
            "CS Foundation → CS Executive → CS Professional, plus practical training",
            "Total duration: ~3-4 years from 12th grade (shorter if entering after graduation)",
        ],
        "entrance_exams": [
            {
                "name": "CS Foundation",
                "conducting_body": "Institute of Company Secretaries of India (ICSI)",
                "eligibility": "Passed 10+2 from a recognized board",
                "age_limit": "No age limit",
                "attempts": "Unlimited, exam held twice a year",
                "selection_process": "Register with ICSI → Foundation exam → Executive → Practical training → Professional",
                "exam_pattern": "4 papers covering Business Environment, Business Laws, Business Management, and Economics",
                "syllabus": "As prescribed by ICSI study material",
            }
        ],
        "preparation_strategy": [
            "Use ICSI's own study material as the primary source, supplemented by reference books",
            "Build strong reading comprehension skills - CS exams are heavily law and theory-based",
            "Practice writing full-length answers for the Executive and Professional stages, not just MCQs",
            "Use the practical training period to build real corporate governance exposure",
        ],
        "best_books": ["ICSI Study Material (mandatory)", "Taxmann's CS Foundation guides", "Business Laws - N.D. Kapoor"],
        "online_resources": [{"name": "ICSI Official Portal", "type": "free", "url": "https://www.icsi.edu"}],
        "previous_year_papers": "https://www.icsi.edu",
        "top_colleges": ["ICSI is the sole conducting body - no college ranking applies"],
        "scholarships": ["ICSI Merit Scholarship Scheme"],
        "salary_range": {"entry": "₹4-7 LPA", "mid": "₹10-18 LPA", "senior": "₹25 LPA+ (Head of Compliance/Company Secretary at large firms)"},
        "career_growth": "Assistant Company Secretary → Company Secretary → Senior CS/Compliance Officer → Head of Legal & Compliance.",
        "official_websites": ["https://www.icsi.edu"],
        "faqs": [{"q": "Is CS harder than CA?", "a": "Both are considered rigorous professional courses; CS focuses more on corporate law and governance, while CA focuses more on accounting, auditing, and taxation."}],
    },
    {
        "slug": "bank-po",
        "title": "Bank PO (IBPS / SBI)",
        "category": "Finance",
        "icon": "briefcase",
        "short_description": "Manage banking operations, lending decisions, and customer relationships as a Probationary Officer.",
        "difficulty": "Medium",
        "streams": ["Commerce", "Arts", "Science"],
        "min_education": "Graduation",
        "overview": (
            "Bank Probationary Officers (POs) are management-track recruits at public sector banks, handling "
            "operations, credit decisions, and branch leadership after an initial training/probation period. "
            "It's one of the most popular stable-career choices for commerce and arts graduates in India."
        ),
        "required_qualifications": ["Bachelor's degree in any discipline from a recognized university"],
        "entrance_exams": [
            {
                "name": "IBPS PO",
                "conducting_body": "Institute of Banking Personnel Selection (IBPS)",
                "eligibility": "Graduate in any discipline",
                "age_limit": "20-30 years (relaxation for reserved categories)",
                "attempts": "No official cap within the age limit",
                "selection_process": "Prelims (objective) → Mains (objective + descriptive) → Interview → Merit list",
                "exam_pattern": "Prelims: English, Quantitative Aptitude, Reasoning; Mains: adds General Awareness, Computer Knowledge, and a descriptive paper",
                "syllabus": "Class 10-12 level Mathematics and English, banking/general awareness, reasoning",
            },
            {
                "name": "SBI PO",
                "conducting_body": "State Bank of India (SBI)",
                "eligibility": "Graduate in any discipline",
                "age_limit": "21-30 years (relaxation for reserved categories)",
                "attempts": "No official cap within the age limit",
                "selection_process": "Prelims → Mains → Group Exercise & Interview → Merit list",
                "exam_pattern": "Similar structure to IBPS PO, with an added Group Discussion/Interview weightage",
                "syllabus": "Class 10-12 level Mathematics and English, banking/economic awareness, reasoning",
            },
        ],
        "preparation_strategy": [
            "Focus heavily on speed in Quantitative Aptitude and Reasoning - the biggest differentiators in banking exams",
            "Build a daily banking and economic current affairs habit",
            "Practice previous years' papers extensively for pattern familiarity",
            "Prepare specifically for the descriptive writing and interview stages, not just objective sections",
        ],
        "best_books": ["Quantitative Aptitude - R.S. Aggarwal", "Banking Awareness - Arihant Publications", "A Modern Approach to Verbal & Non-Verbal Reasoning"],
        "online_resources": [
            {"name": "IBPS Official Portal", "type": "free", "url": "https://www.ibps.in"},
            {"name": "Adda247 Banking", "type": "freemium", "url": "https://www.adda247.com"},
        ],
        "previous_year_papers": "https://www.ibps.in",
        "top_colleges": ["No specific college required; banking exam coaching institutes are widely available"],
        "scholarships": ["Not applicable - this is a direct recruitment exam rather than an academic program"],
        "salary_range": {"entry": "₹8-10 LPA (all-inclusive, PSU banks)", "mid": "₹15-20 LPA (Manager/Senior Manager)", "senior": "₹30 LPA+ (General Manager/senior leadership)"},
        "career_growth": "Probationary Officer → Assistant Manager → Manager → Senior Manager → Chief Manager → General Manager.",
        "official_websites": ["https://www.ibps.in", "https://sbi.co.in/careers"],
        "faqs": [{"q": "What's the difference between IBPS PO and SBI PO?", "a": "IBPS PO recruits for multiple public sector banks at once; SBI PO recruits specifically for State Bank of India, generally considered slightly more prestigious with a marginally different exam pattern."}],
    },
    {
        "slug": "judge",
        "title": "Judge (Judicial Services)",
        "category": "Law",
        "icon": "scale",
        "short_description": "Preside over court proceedings, interpret law, and deliver judgments as a judicial officer.",
        "difficulty": "Very Hard",
        "streams": ["Arts", "Commerce", "Science"],
        "min_education": "Graduation",
        "overview": (
            "Judges in the lower judiciary (Civil Judge/Magistrate) are recruited directly out of law school via "
            "state Judicial Services Examinations, offering a direct path onto the bench without first needing "
            "years of litigation practice - a distinct route from becoming a Senior Advocate through practice."
        ),
        "required_qualifications": [
            "LLB degree (3-year or 5-year integrated) from a recognized university",
            "Enrollment with a State Bar Council (requirements vary slightly by state - some allow fresh LLB graduates to apply directly)",
        ],
        "entrance_exams": [
            {
                "name": "State Judicial Services Examination (e.g. Delhi Judicial Services, MP State Judicial Services)",
                "conducting_body": "Respective State Public Service Commission or High Court",
                "eligibility": "LLB degree; age and practice requirements vary by state",
                "age_limit": "21-35 years typically (varies by state)",
                "attempts": "Varies by state - generally limited attempts within age bracket",
                "selection_process": "Preliminary (objective) → Mains (descriptive law papers) → Viva Voce/Interview → Merit list",
                "exam_pattern": "Prelims: objective law paper; Mains: multiple descriptive papers on civil law, criminal law, and language",
                "syllabus": "Constitutional Law, Civil Procedure Code, Criminal Procedure Code, Indian Penal Code, Evidence Act, and state-specific local laws",
            }
        ],
        "preparation_strategy": [
            "Build a rock-solid grasp of bare acts - CPC, CrPC, IPC, Evidence Act, Constitution - through repeated reading",
            "Practice extensive answer writing for the Mains stage, since judgment-writing skills are directly tested",
            "Study your target state's local/state-specific laws in detail, as these carry significant weightage",
            "Join a judicial services-focused test series closer to the exam for realistic practice",
        ],
        "best_books": ["Universal's Bare Acts (CPC, CrPC, IPC, Evidence Act)", "Indian Polity - M. Laxmikanth (for Constitutional Law)", "State-specific judicial services guides"],
        "online_resources": [{"name": "Doctrine of Lawyering", "type": "freemium", "url": "https://blog.ipleaders.in"}],
        "previous_year_papers": "https://www.barcouncilofindia.org",
        "top_colleges": ["No specific college required; NLUs and top law schools often have strong judicial services coaching culture"],
        "scholarships": ["State-specific pre-exam training scholarships for reserved categories"],
        "salary_range": {"entry": "₹77,840-1,36,520/month (Civil Judge, per 2nd National Judicial Pay Commission)", "mid": "₹1,44,840+/month (District Judge)", "senior": "₹2,24,100+/month (High Court Judge level)"},
        "career_growth": "Civil Judge (Junior Division) → Civil Judge (Senior Division) → District Judge → (via elevation) High Court Judge.",
        "official_websites": ["https://www.barcouncilofindia.org"],
        "faqs": [
            {"q": "Can a fresh LLB graduate become a judge directly?", "a": "Yes, most states allow fresh law graduates to sit for the Judicial Services Exam directly, without requiring years of litigation practice first - though a few states do require some years of practice."},
        ],
    },
    {
        "slug": "graphic-uiux-designer",
        "title": "Graphic / UI-UX Designer",
        "category": "Design",
        "icon": "shirt",
        "short_description": "Create visual identities, digital interfaces, and user experiences for brands and products.",
        "difficulty": "Medium",
        "streams": ["Arts", "Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Graphic and UI/UX Designers shape how brands look and how digital products feel to use - spanning "
            "branding, illustration, and the design of apps and websites. Demand has grown sharply alongside the "
            "digital product economy, with UI/UX in particular commanding strong tech-industry salaries."
        ),
        "required_qualifications": [
            "10+2 in any stream",
            "B.Des in Communication/Visual/Interaction Design (4 years), or portfolio-based hiring without a formal design degree",
            "Optional: M.Des or specialized UX bootcamps for deeper specialization",
        ],
        "entrance_exams": [
            {
                "name": "NID DAT (National Institute of Design - Design Aptitude Test)",
                "conducting_body": "National Institute of Design (NID)",
                "eligibility": "10+2 in any stream",
                "age_limit": "No upper age limit for general category (check current notification)",
                "attempts": "No official cap",
                "selection_process": "Prelims (written, drawing-based) → Mains (studio test + interview)",
                "exam_pattern": "Prelims: design aptitude, sketching, general knowledge; Mains: studio-based creative exercises and personal interview",
                "syllabus": "Visual perception, sketching, design thinking, general awareness",
            }
        ],
        "preparation_strategy": [
            "Build a strong sketching and visual portfolio well before applying",
            "Study design fundamentals - color theory, typography, layout - through free online resources",
            "For UI/UX specifically, learn tools like Figma and build 2-3 case-study projects",
            "Practice NID/UCEED-style design aptitude and situation-based problem solving",
        ],
        "best_books": ["NID/UCEED Entrance Guide - RPH Editorial Board", "Don't Make Me Think - Steve Krug (for UX fundamentals)"],
        "online_resources": [
            {"name": "Figma Learning Resources", "type": "free", "url": "https://www.figma.com/resources/learn-design"},
            {"name": "Behance", "type": "free", "url": "https://www.behance.net"},
        ],
        "previous_year_papers": "https://admissions.nid.edu",
        "top_colleges": ["NID Ahmedabad", "IDC IIT Bombay", "Srishti Manipal Institute"],
        "scholarships": ["NID means-cum-merit scholarships", "State minority/SC-ST design scholarships"],
        "salary_range": {"entry": "₹4-7 LPA (UI/UX) / ₹3-5 LPA (graphic design)", "mid": "₹10-20 LPA", "senior": "₹25 LPA+ (design lead/creative director)"},
        "career_growth": "Junior Designer → Designer → Senior Designer → Design Lead → Creative Director / Head of Design.",
        "official_websites": ["https://admissions.nid.edu"],
        "faqs": [{"q": "Do I need a design degree for UI/UX specifically?", "a": "Not strictly - many UI/UX designers enter through bootcamps and strong portfolios rather than a formal design degree, especially in the tech industry."}],
    },
    {
        "slug": "digital-marketing-specialist",
        "title": "Digital Marketing Specialist",
        "category": "Media",
        "icon": "chart",
        "short_description": "Grow brands and drive business results through social media, search, content, and paid advertising.",
        "difficulty": "Easy",
        "streams": ["Arts", "Commerce", "Science"],
        "min_education": "12th",
        "overview": (
            "Digital Marketing Specialists plan and run campaigns across search, social media, email, and paid "
            "advertising to grow brands and drive measurable business results. It's one of the more accessible "
            "entry points into media/business careers, with a fast, skills-based learning curve."
        ),
        "required_qualifications": [
            "10+2 in any stream",
            "BBA/BA/BCom in Marketing or Mass Communication (not mandatory - many succeed via certifications and portfolios)",
            "Google/Meta/HubSpot certifications significantly boost employability",
        ],
        "entrance_exams": [
            {
                "name": "CUET (for BBA/BMS admissions at central universities)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "10+2 in any stream",
                "age_limit": "No upper age limit",
                "attempts": "Once per year",
                "selection_process": "CBT → Merit list → University-specific counselling",
                "exam_pattern": "Subject-wise MCQ tests + general test",
                "syllabus": "NCERT-based, domain-specific subjects plus general aptitude",
            }
        ],
        "preparation_strategy": [
            "Get hands-on early - run a small personal brand, blog, or social page to learn by doing",
            "Complete free certifications: Google Digital Garage, Google Analytics, Meta Blueprint",
            "Build a portfolio of real campaigns (even small/personal ones) with measurable results",
            "Learn basic data analysis (Excel, Google Analytics) to speak the language of ROI",
        ],
        "best_books": ["Digital Marketing for Dummies", "Contagious - Jonah Berger", "Hooked - Nir Eyal"],
        "online_resources": [
            {"name": "Google Digital Garage", "type": "free", "url": "https://learndigital.withgoogle.com"},
            {"name": "HubSpot Academy", "type": "free", "url": "https://academy.hubspot.com"},
            {"name": "Meta Blueprint", "type": "free", "url": "https://www.facebook.com/business/learn"},
        ],
        "previous_year_papers": "https://cuet.samarth.ac.in",
        "top_colleges": ["No specific college required; MICA Ahmedabad and IIMs offer strong marketing specializations for those pursuing MBA-level roles"],
        "scholarships": ["UGC merit scholarships (for BBA/BMS route)"],
        "salary_range": {"entry": "₹3-6 LPA", "mid": "₹8-15 LPA", "senior": "₹20 LPA+ (marketing head/agency founder)"},
        "career_growth": "Digital Marketing Executive → Senior Executive → Marketing Manager → Head of Marketing / Own Agency.",
        "official_websites": ["https://cuet.samarth.ac.in"],
        "faqs": [{"q": "Can I start a digital marketing career without a degree?", "a": "Yes, this is one of the most accessible fields to break into through certifications and a strong portfolio, though a business/marketing degree can help for corporate roles."}],
    },
    {
        "slug": "hr-manager",
        "title": "Human Resources Manager",
        "category": "Business",
        "icon": "briefcase",
        "short_description": "Manage talent acquisition, employee relations, and organizational culture within a company.",
        "difficulty": "Medium",
        "streams": ["Arts", "Commerce", "Science"],
        "min_education": "Graduation",
        "overview": (
            "HR Managers oversee recruitment, employee relations, performance management, and workplace culture. "
            "It's a people-centric business function present in every industry, offering a stable and "
            "relationship-driven career path."
        ),
        "required_qualifications": [
            "Bachelor's degree in any discipline",
            "MBA in Human Resources (2 years) strongly preferred for management-track roles",
            "Certifications (SHRM-CP, HRCI) valued for mid-career professionals",
        ],
        "entrance_exams": [
            {
                "name": "CAT (for MBA-HR admissions)",
                "conducting_body": "IIMs (rotational)",
                "eligibility": "Bachelor's degree with minimum 50% marks",
                "age_limit": "No age limit",
                "attempts": "No cap, once a year",
                "selection_process": "CBT → Shortlisting → WAT/GD/PI at individual B-schools",
                "exam_pattern": "VARC, DILR, QA sections, 2 hours, objective + TITA",
                "syllabus": "Verbal ability, reading comprehension, data interpretation, logical reasoning, quantitative aptitude",
            }
        ],
        "preparation_strategy": [
            "Build strong interpersonal and communication skills - core to every HR function",
            "Seek HR internships early to understand recruitment, payroll, and employee relations firsthand",
            "Learn basic labor law and compliance fundamentals, which matter more than people expect",
            "Pursue an MBA-HR or equivalent PG program for faster progression into management roles",
        ],
        "best_books": ["Human Resource Management - Gary Dessler", "The HR Scorecard - Becker, Huselid, Ulrich"],
        "online_resources": [
            {"name": "SHRM Learning Resources", "type": "freemium", "url": "https://www.shrm.org"},
            {"name": "Coursera HR Specializations", "type": "paid", "url": "https://www.coursera.org"},
        ],
        "previous_year_papers": "https://iimcat.ac.in",
        "top_colleges": ["XLRI Jamshedpur", "TISS Mumbai", "IIM Calcutta", "MDI Gurgaon"],
        "scholarships": ["Institute merit fee waivers", "Need-based MBA scholarships"],
        "salary_range": {"entry": "₹5-9 LPA", "mid": "₹15-25 LPA", "senior": "₹35 LPA+ (CHRO/VP People)"},
        "career_growth": "HR Executive → HR Business Partner → HR Manager → Head of HR → CHRO (Chief Human Resources Officer).",
        "official_websites": ["https://iimcat.ac.in"],
        "faqs": [{"q": "Is an MBA necessary for a career in HR?", "a": "Not strictly required for entry-level roles, but an MBA-HR significantly accelerates progression into management and leadership HR positions."}],
    },
    {
        "slug": "aircraft-maintenance-engineer",
        "title": "Aircraft Maintenance Engineer (AME)",
        "category": "Aviation",
        "icon": "plane",
        "short_description": "Inspect, maintain, and certify aircraft as airworthy, ensuring flight safety on the ground.",
        "difficulty": "Hard",
        "streams": ["Science"],
        "min_education": "12th",
        "overview": (
            "Aircraft Maintenance Engineers (AMEs) inspect, repair, and certify aircraft as airworthy before every "
            "flight - a highly responsible, well-regulated role distinct from piloting, requiring DGCA licensing "
            "similar in rigor to a pilot's."
        ),
        "required_qualifications": [
            "10+2 with Physics, Chemistry, Mathematics",
            "AME course (2.5-3 years) from a DGCA-approved institute, followed by DGCA licensing exams",
            "Minimum practical experience requirements before full AME license issuance",
        ],
        "entrance_exams": [
            {
                "name": "DGCA AME Licensing Exams",
                "conducting_body": "Directorate General of Civil Aviation (DGCA)",
                "eligibility": "10+2 with PCM; completion of a DGCA-approved AME course",
                "age_limit": "No strict upper age limit for starting the course",
                "attempts": "Can reattempt individual subject papers",
                "selection_process": "AME coursework → DGCA module exams → Practical experience → License (Basic Aircraft Maintenance Engineer's Licence)",
                "exam_pattern": "Modular subject-wise written exams covering aircraft systems, regulations, and maintenance practices",
                "syllabus": "As prescribed by DGCA CAR 66 (Civil Aviation Requirements for AME licensing)",
            }
        ],
        "preparation_strategy": [
            "Build strong fundamentals in Physics and basic mechanical/electrical concepts",
            "Choose a DGCA-approved AME institute carefully - approval status directly affects licensing eligibility",
            "Take the modular DGCA exams seriously and sequentially, as each has a validity window",
            "Seek hands-on hangar/practical training opportunities during the course",
        ],
        "best_books": ["Aircraft Maintenance & Repair - Kroes & Watkins", "DGCA CAR 66 Study Guides"],
        "online_resources": [{"name": "DGCA Official Portal", "type": "free", "url": "https://www.dgca.gov.in"}],
        "previous_year_papers": "https://www.dgca.gov.in",
        "top_colleges": ["Hindustan Institute of Engineering Technology (AME)", "Bombay Flying Club AME Institute", "Indira Gandhi Rashtriya Uran Akademi"],
        "scholarships": ["Institute-specific merit scholarships"],
        "salary_range": {"entry": "₹4-7 LPA", "mid": "₹10-18 LPA", "senior": "₹25 LPA+ (Chief Engineer/quality manager)"},
        "career_growth": "Trainee AME → Licensed AME → Certifying Engineer → Quality Manager → Chief Engineer (base maintenance).",
        "official_websites": ["https://www.dgca.gov.in"],
        "faqs": [{"q": "Is AME the same as a pilot?", "a": "No - AMEs maintain and certify aircraft on the ground; pilots fly them. Both require DGCA licensing but are entirely separate career tracks."}],
    },
    {
        "slug": "special-education-teacher",
        "title": "Special Education Teacher",
        "category": "Education",
        "icon": "graduation-cap",
        "short_description": "Teach and support students with learning disabilities, developmental delays, or other special needs.",
        "difficulty": "Medium",
        "streams": ["Arts", "Science", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Special Education Teachers work with students who have learning disabilities, autism spectrum "
            "conditions, or physical/developmental disabilities, adapting teaching methods to each child's needs. "
            "Growing awareness of inclusive education is driving strong, steady demand for this specialization."
        ),
        "required_qualifications": [
            "10+2 in any stream",
            "Bachelor's degree + B.Ed (Special Education) - RCI-recognized program",
            "RCI (Rehabilitation Council of India) registration required to practice",
        ],
        "entrance_exams": [
            {
                "name": "CUET (for B.Ed Special Education admissions at central universities)",
                "conducting_body": "National Testing Agency (NTA)",
                "eligibility": "Bachelor's degree in any discipline",
                "age_limit": "No upper age limit",
                "attempts": "Once per year",
                "selection_process": "CBT → Merit list → University-specific counselling",
                "exam_pattern": "Subject-wise MCQ tests + general test",
                "syllabus": "NCERT-based, domain-specific subjects plus general aptitude",
            }
        ],
        "preparation_strategy": [
            "Volunteer or intern at special schools/inclusive classrooms to confirm genuine interest early",
            "Build patience-intensive, individualized teaching skills through practical exposure",
            "Choose an RCI-recognized program specifically - non-recognized programs won't allow you to register and practice",
            "Learn about specific conditions (autism, dyslexia, ADHD) in depth, not just generic special-ed theory",
        ],
        "best_books": ["Exceptional Children - Heward & Orlansky", "Educating Children with Learning Disabilities - NCERT resources"],
        "online_resources": [{"name": "Rehabilitation Council of India Portal", "type": "free", "url": "https://rehabcouncil.nic.in"}],
        "previous_year_papers": "https://cuet.samarth.ac.in",
        "top_colleges": ["Delhi University (special education programs)", "NIEPMD Chennai", "AYJNISHD Mumbai"],
        "scholarships": ["RCI/state scholarships for special education trainees"],
        "salary_range": {"entry": "₹2.5-4.5 LPA", "mid": "₹6-10 LPA", "senior": "₹15 LPA+ (special school principal/consultant)"},
        "career_growth": "Special Educator → Senior Special Educator → Resource Room Coordinator → Special School Principal / Inclusive Education Consultant.",
        "official_websites": ["https://rehabcouncil.nic.in"],
        "faqs": [{"q": "Is RCI registration mandatory?", "a": "Yes, practicing as a special educator in India legally requires RCI registration, which in turn requires graduating from an RCI-recognized program."}],
    },
]
