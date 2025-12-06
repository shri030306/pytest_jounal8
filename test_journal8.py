from journal8 import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Shreesai\n"
        "Employee ID: E0318\n"
        "Department: HR\n"
        "Salary: 56000"
    )

    assert employee_details("shreesai", "E0318", "HR", 56000) == expected_output