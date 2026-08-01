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
        "title": "Army Officer (Defence)",
        "category": "Defence",
        "icon": "shield",
        "short_description": "Lead and serve in the Indian Armed Forces, ensuring national security and defence operations.",
        "difficulty": "Hard",
        "streams": ["Science", "Arts", "Commerce"],
        "min_education": "12th",
        "overview": (
            "Officers in the Indian Army lead troops, manage operations, and serve the nation across combat, "
            "technical, and administrative roles. Entry is via NDA (after 12th) or CDS (after graduation)."
        ),
        "required_qualifications": ["10+2 with PCM (for NDA Army technical entries) or any stream (non-technical)", "Graduation (for CDS entry)"],
        "entrance_exams": [
            {
                "name": "NDA (National Defence Academy) Exam",
                "conducting_body": "Union Public Service Commission (UPSC)",
                "eligibility": "10+2 pass, unmarried male/female candidates, 16.5-19.5 years",
                "age_limit": "16.5 to 19.5 years",
                "attempts": "Twice a year exam; multiple attempts within age bracket",
                "selection_process": "Written exam → SSB Interview (5 days) → Medical Test → Merit list",
                "exam_pattern": "Mathematics (300 marks) + General Ability Test (600 marks), objective",
                "syllabus": "Class 11-12 Mathematics, English, General Science, History, Geography, Current Affairs",
            }
        ],
        "preparation_strategy": [
            "Maintain excellent physical fitness alongside academics - both matter for selection",
            "Practice Mathematics and General Ability Test papers extensively",
            "Prepare specifically for the SSB interview - group tasks, psychological tests, personal interview",
            "Stay updated on current national and defence-related affairs",
        ],
        "best_books": ["NDA/NA Guide - Pathfinder Publications", "Mathematics for NDA - R.S. Aggarwal"],
        "online_resources": [{"name": "UPSC NDA Official Notification", "type": "free", "url": "https://upsc.gov.in"}],
        "previous_year_papers": "https://upsc.gov.in",
        "top_colleges": ["National Defence Academy, Khadakwasla", "Indian Military Academy, Dehradun"],
        "scholarships": ["Fully funded training - Armed Forces cover education and stipend during training"],
        "salary_range": {"entry": "₹56,100/month (Level 10) + allowances", "mid": "₹1,21,200+/month (Lt Col)", "senior": "₹2,25,000+/month (Brigadier & above)"},
        "career_growth": "Lieutenant → Captain → Major → Lieutenant Colonel → Colonel → Brigadier → General.",
        "official_websites": ["https://upsc.gov.in", "https://joinindianarmy.nic.in"],
        "faqs": [{"q": "Can girls apply for NDA?", "a": "Yes, NDA has been open to female candidates since 2022."}],
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
]
