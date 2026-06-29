import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Read CSV file
data = pd.read_csv("data.csv")

# Analyze Data
total_employees = len(data)
average_salary = data["Salary"].mean()
highest_salary = data["Salary"].max()
lowest_salary = data["Salary"].min()

# Create PDF
pdf = SimpleDocTemplate("Employee_Report.pdf", pagesize=letter)
styles = getSampleStyleSheet()

elements = []

# Title
elements.append(Paragraph("<b>Employee Salary Report</b>", styles["Title"]))

# Summary
elements.append(Paragraph(f"Total Employees: {total_employees}", styles["Normal"]))
elements.append(Paragraph(f"Average Salary: ₹{average_salary:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Salary: ₹{highest_salary}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Salary: ₹{lowest_salary}", styles["Normal"]))
elements.append(Paragraph("<br/><b>Employee Details</b>", styles["Heading2"]))

# Table Data
table_data = [list(data.columns)]
for row in data.values:
    table_data.append(list(row))

table = Table(table_data)

table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('BOTTOMPADDING', (0,0), (-1,0), 10),
]))

elements.append(table)

# Build PDF
pdf.build(elements)

print("PDF Report Generated Successfully: Employee_Report.pdf")
