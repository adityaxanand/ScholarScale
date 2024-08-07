# import streamlit as st
# import numpy as np

# # Set the page configuration
# st.set_page_config(
#     page_title="ScholarScale",
#     page_icon="🎓",
#     layout="centered",
#     initial_sidebar_state="auto",
#     menu_items={
#         "Get Help": "https://github.com/adityaxanand/ScholarScale/discussions",
#         "Report a bug": "https://github.com/adityaxanand/ScholarScale/issues/new",
#         "About": None,
#     },
# )

# # Define the grade to point mapping
# grade_to_point = {
#     "O": 10,
#     "E": 9,
#     "A": 8,
#     "B": 7,
#     "C": 6,
#     "D": 5,
# }
# grades = list(grade_to_point.keys())

# # Function to calculate CGPA
# def calculate_cgpa(
#     grade: np.array,
#     credit: np.array,
#     previous_cgpa: float = 0,
#     previous_credit: float = 0,
# ):
#     total_credit = credit.sum() + previous_credit
#     total_grade = (grade * credit).sum() + previous_cgpa * previous_credit
#     return total_grade / total_credit

# # Title and description
# st.title("🎓 Scholar Scale")
# st.markdown("A simple and intuitive CGPA calculator.")

# # Display the CGPA formula
# st.latex(r"CGPA = \frac{\sum_{i=1}^{n} (grade_i \times credit_i)}{\sum_{i=1}^{n} credit_i}")

# # Input for previous CGPA and credit
# cols = st.columns(2)
# previous_cgpa = cols[0].number_input(
#     label="Previous CGPA",
#     help="Enter Your CGPA upto previous semester",
#     min_value=0.00,
#     value=0.00,
#     step=0.01,
# )
# previous_credit = cols[1].number_input(
#     label="Previous Credit",
#     help="Enter the total number of credits you have taken upto previous semester",
#     min_value=0.0,
#     value=0.0,
#     step=0.5,
# )

# # Input for number of subjects
# number_of_subjects = st.number_input(
#     label="Number of Subjects",
#     help="Enter the number of subjects you are taking this semester",
#     min_value=1,
#     max_value=10,
#     value=5,
# )

# # Input for grades and credits
# grade = np.array([0] * number_of_subjects)
# credit = np.array([0] * number_of_subjects)
# for i in range(number_of_subjects):
#     st.subheader(f"Subject {i+1}")
#     cols = st.columns(2)
#     grade[i] = grade_to_point[
#         cols[0].selectbox(
#             label=f"Grade",
#             options=grades,
#             key=f"selectbox_{i}",
#         )
#     ]
#     credit[i] = cols[1].number_input(
#         label=f"Credit",
#         min_value=1.0,
#         max_value=10.0,
#         value=4.0,
#         step=0.5,
#         key=f"number_input_{i}",
#     )

# # Calculate button
# if st.button("Calculate"):
#     st.info(f"Your semester GPA is {calculate_cgpa(grade, credit):.2f}")
#     st.success(
#         f"Your Cumulative GPA is {calculate_cgpa(grade, credit, previous_cgpa, previous_credit):.2f}"
#     )

# # Footer
# #st.markdown("Made with ❤️ by Aditya")
# st.write(
#     """
#     <style>
#         footer {
#             visibility: hidden;
#         }
#         /* Add some styling to the body */
#         body {
#             background-color: #fafafa;
#             font-family: Arial, sans-serif;
#         }
#         /* Style the title */
#         .title h1 {
#             color: #333;
#             text-align: center;
#             padding: 20px 0;
#         }
#         /* Style the subheader */
#         .subheader h2 {
#             color: #666;
#             text-align: center;
#             padding-bottom: 20px;
#         }
#         /* Style the calculate button */
#         .streamlit-button.primary-button {
#             background-color: #4b4bff;
#             color: white;
#         }
#         /* Style the select box options to have a hand cursor */
#         .dropdown-content {
#             cursor: pointer;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


import streamlit as st
import numpy as np

# Set the page configuration
st.set_page_config(
    page_title="ScholarScale",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://github.com/adityaxanand/ScholarScale/discussions",
        "Report a bug": "https://github.com/adityaxanand/ScholarScale/issues/new",
        "About": None,
    },
)

# Define the grade to point mapping
grade_to_point = {
    "O": 10,
    "E": 9,
    "A": 8,
    "B": 7,
    "C": 6,
    "D": 5,
}
grades = list(grade_to_point.keys())

# Function to calculate CGPA
def calculate_cgpa(
    grade: np.array,
    credit: np.array,
    previous_cgpa: float = 0,
    previous_credit: float = 0,
):
    total_credit = credit.sum() + previous_credit
    total_grade = (grade * credit).sum() + previous_cgpa * previous_credit
    return total_grade / total_credit

# Title and description
st.title("🎓 Scholar Scale")
st.markdown("A simple and intuitive CGPA calculator.")

# Display the CGPA formula
st.latex(r"CGPA = \frac{\sum_{i=1}^{n} (grade_i \times credit_i)}{\sum_{i=1}^{n} credit_i}")

# Input for previous CGPA and credit
cols = st.columns(2)
previous_cgpa = cols[0].number_input(
    label="Previous CGPA",
    help="Enter Your CGPA up to the previous semester",
    min_value=0.00,
    value=0.00,
    step=0.01,
)
previous_credit = cols[1].number_input(
    label="Previous Credit",
    help="Enter the total number of credits you have taken up to the previous semester",
    min_value=0.0,
    value=0.0,
    step=0.5,
)

# Input for number of subjects
number_of_subjects = st.number_input(
    label="Number of Subjects",
    help="Enter the number of subjects you are taking this semester",
    min_value=1,
    max_value=10,
    value=5,
)

# Input for grades and credits
grade = np.array([0] * number_of_subjects)
credit = np.array([0] * number_of_subjects)
for i in range(number_of_subjects):
    st.subheader(f"Subject {i+1}")
    cols = st.columns(2)
    grade[i] = grade_to_point[
        cols[0].selectbox(
            label=f"Grade",
            options=grades,
            key=f"selectbox_{i}",
        )
    ]
    credit[i] = cols[1].number_input(
        label=f"Credit",
        min_value=1.0,
        max_value=10.0,
        value=4.0,
        step=0.5,
        key=f"number_input_{i}",
    )

# Calculate button
if st.button("Calculate"):
    st.info(f"Your semester GPA is {calculate_cgpa(grade, credit):.2f}")
    st.success(
        f"Your Cumulative GPA is {calculate_cgpa(grade, credit, previous_cgpa, previous_credit):.2f}"
    )

# Footer
st.write(
    """
    <style>
        footer {
            visibility: hidden;
        }
        /* Add some styling to the body */
        body {
            background-color: #fafafa;
            font-family: Arial, sans-serif;
        }
        /* Style the title */
        .title h1 {
            color: #333;
            text-align: center;
            padding: 20px 0;
        }
        /* Style the subheader */
        .subheader h2 {
            color: #666;
            text-align: center;
            padding-bottom: 20px;
        }
        /* Style the calculate button */
        .streamlit-button.primary-button {
            background-color: #4b4bff;
            color: white;
        }
        /* Style the select box options to have a hand cursor */
        .dropdown-content {
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
