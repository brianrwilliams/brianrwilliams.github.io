import os

def format_date_mmdd(date_mmdd):
    """Convert 'mm/dd' string into 'Month d' string, e.g. '03/04' -> 'March 4'."""
    MONTHS = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April',
        '05': 'May', '06': 'June', '07': 'July', '08': 'August',
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    try:
        mm, dd = date_mmdd.split('/')
        month_name = MONTHS[mm]
        day = str(int(dd))  # Remove leading zero if any
        return f"{month_name} {day}"
    except (KeyError, ValueError):
        return date_mmdd  # fallback: return input if invalid

def create_quiz(date_mmdd):
    os.makedirs('quiz', exist_ok=True)
    formatted_date = format_date_mmdd(date_mmdd)
    filename = f"quiz/quiz_{date_mmdd.replace('/', '')}.tex"
    content = f"""% File: {filename}

\\documentclass[12pt]{{article}}

% Load your custom style package
\\usepackage{{/Users/bwill22/brianrwilliams/new_style}}
\\usepackage{{/Users/bwill22/brianrwilliams/macros-master}}

% Additional packages needed for this quiz template
\\usepackage{{amssymb,amsmath,amsthm}}

% Itemize and enumerate styles consistent with your style package can remain default

% Page geometry and header/footer can be customized here:
\\usepackage[a4paper,margin=1in]{{geometry}}
\\usepackage{{fancyhdr}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[L]{{\\headfam\\headweight Quiz}}
\\fancyhead[C]{{\\headfam\\itshape\\large\\thetitle}}
\\fancyhead[R]{{\\headfam\\headweight Page \\thepage}}
% Title formatting uses your package's redefinition, so normal \\title works
\\title{{MA 442 - Quiz}}
\\date{{{formatted_date}}}

\\begin{{document}}

\\maketitle
\\vspace{{-1em}}
\\noindent
\\begin{{tabular}}{{@{{}}p{{1cm}}p{{8cm}}p{{1cm}}p{{5cm}}@{{}}}}
\\textbf{{Name:}} & \\hrulefill & \\textbf{{BUID:}} & \\hrulefill \\\\
\\end{{tabular}}

\\begin{{question}}
QUESTION HERE
\\end{{question}}

\\end{{document}}
"""
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

def create_supplement(title, date_mmdd):
    os.makedirs('supplements', exist_ok=True)
    formatted_date = format_date_mmdd(date_mmdd)
    safe_title = title.replace(' ', '_')
    filename = f"supplements/{safe_title}.tex"
    content = f"""\\documentclass[12pt]{{article}}

% Load your custom style package
\\usepackage{{/Users/bwill22/brianrwilliams/new_style}}
%\\usepackage{{/Users/bwill22/brianrwilliams/macros-master}}

% Additional packages needed for this quiz template
\\usepackage{{amssymb,amsmath,amsthm}}

% Theorem-style environments for questions and solutions
\\theoremstyle{{definition}}
\\newtheorem{{question}}{{Question}}

\\theoremstyle{{remark}}
\\newtheorem*{{solution}}{{Solution}}

% Itemize and enumerate styles consistent with your style package can remain default

% Page geometry and header/footer can be customized here:
\\usepackage[a4paper,margin=1in]{{geometry}}
\\usepackage{{fancyhdr}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[L]{{\\headfam\\headweight Quiz}}
\\fancyhead[C]{{\\headfam\\itshape\\large\\thetitle}}
\\fancyhead[R]{{\\headfam\\headweight Page \\thepage}}
% Title formatting uses your package's redefinition, so normal \\title works
\\title{{{title}}}
\\date{{{formatted_date}}}

\\begin{{document}}

\\maketitle

\\end{{document}}
"""
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

def create_solution(section_input):
    os.makedirs('supplements', exist_ok=True)
    safe_title = section_input.replace(' ', '_')
    filename = f"supplements/solutions_{safe_title}.tex"
    content = f"""\\documentclass[12pt]{{article}}

% Load your custom style package
\\usepackage{{/Users/bwill22/brianrwilliams.github.io/new_style}}
\\usepackage{{/Users/bwill22/brianrwilliams.github.io/macros-master}}

% Additional packages needed for this quiz template
\\usepackage{{amssymb,amsmath,amsthm}}

% Itemize and enumerate styles consistent with your style package can remain default

% Page geometry and header/footer can be customized here:
\\usepackage[a4paper,margin=1in]{{geometry}}
\\usepackage{{fancyhdr}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[L]{{\\headfam\\headweight Quiz}}
\\fancyhead[C]{{\\headfam\\itshape\\large\\thetitle}}
\\fancyhead[R]{{\\headfam\\headweight Page \\thepage}}
% Title formatting uses your package's redefinition, so normal \\title works
\\title{{Solutions to selected exercises from \\S {{{section_input}}}}}
\\date{{}}
\\begin{{document}}

\\maketitle

\\subsection{{Question ??}}
\\end{{document}}
"""
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def main():
    print("Choose an option:")
    print("1. Quiz or quiz solution")
    print("2. Supplement")
    print("3. Solutions of book exercises")

    choice = input("Enter 1-3: ").strip()
    if choice == '1':
        date_input = input("Enter date in mm/dd format (e.g. 03/04): ").strip()
        if len(date_input) == 5 and date_input[2] == '/' and date_input[:2].isdigit() and date_input[3:].isdigit():
            create_quiz(date_input)
        else:
            print("Invalid date format, expected mm/dd")
    elif choice == '2':
        title = input("Enter title: ").strip()
        date_input = input("Enter date in mm/dd format (e.g. 03/04): ").strip()
        if len(date_input) == 5 and date_input[2] == '/' and date_input[:2].isdigit() and date_input[3:].isdigit():
            create_supplement(title, date_input)
        else:
            print("Invalid date format, expected mm/dd")
    elif choice == '3':
        section_input = input("Enter section number (eg 2.4): ").strip()
        create_solution(section_input)
    else:
        print("Invalid choice, please run script again and select 1 or 2.")
if __name__ == "__main__":
    main()
