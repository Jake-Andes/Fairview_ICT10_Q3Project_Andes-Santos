from pyscript import document  # type: ignore

def adding_numbers(e=None):
    out = document.getElementById("output1")
    grade = document.getElementById("num1").value
    section = document.getElementById("num2").value

    clinic_el = document.querySelector('input[name="clinic"]:checked')
    online_el = document.querySelector('input[name="online"]:checked')
    clinic = clinic_el.value if clinic_el else "no"
    online = online_el.value if online_el else "no"

    if grade == "":
        out.innerText = "Please select a grade level."
        return
    if section == "":
        out.innerText = "Please select a section."
        return

    # simple team assignment (based on section)
    if section == "Topaz":
        team = "Blue Bears"
    elif section == "Ruby":
        team = "Yellow Tigers"
    elif section == "Emerald":
        team = "Green Hornets"
    elif section == "Sapphire" or section == "Jade":
        team = "Red Bulldogs"
    else:
        team = "Unassigned"

    # eligibility logic (simple if / else)
    if clinic == "yes" and online == "yes":
        status = "Eligible for intramurals."
    elif clinic == "yes" and online == "no":
        status = "Clinic slip OK — online registration missing."
    elif clinic == "no" and online == "yes":
        status = "Online registration OK — clinic slip missing."
    else:
        status = "Not eligible — clinic slip and online registration missing."

    team_images = {
        "Blue Bears": "Bears.png",
        "Yellow Tigers": "Tigers.png",
        "Green Hornets": "Hornets.png",
        "Red Bulldogs": "Bulldogs.png",
        "Unassigned": "https://via.placeholder.com/160x100.png?text=No+Team"
    }
    img = team_images.get(team, team_images["Unassigned"])

    # display image and text
    out.innerHTML = (
        f"<div style='display:flex;flex-direction:column;align-items:center;gap:8px;'>"
        f"<img src=\"{img}\" alt=\"{team}\" style='max-width:200px;border-radius:8px;border:1px solid rgba(0,0,0,0.06);'>"
        f"<div style='font-weight:700;color:var(--gold);'>Grade {grade} - {section} ({team})</div>"
        f"<div>{status}</div>"
        f"</div>"
    )
