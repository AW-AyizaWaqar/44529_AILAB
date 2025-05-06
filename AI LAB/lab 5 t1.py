def check_presence(roll_number, attendance):
    return "Present" if attendance.get(roll_number, False) else "Absent"

# Example usage:
attendance = {101: True, 102: False, 103: True}
print(check_presence(101, attendance))  # Output: Present
print(check_presence(102, attendance))  # Output: Absent
