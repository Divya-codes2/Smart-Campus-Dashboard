
def get_notices():
    return [
        {
            "title": "Holiday Notice",
            "body": "Campus closed on 25th Dec",
            "date": "2025-12-25"
        },
        {
            "title": "Exam Notice",
            "body": "Mid-sem exams from 5th Jan",
            "date": "2026-01-05"
        }
    ]


def get_attendance(section):
    return [
        {"date": "2025-12-01", "percent": 75},
        {"date": "2025-12-05", "percent": 78},
        {"date": "2025-12-10", "percent": 80},
        {"date": "2025-12-15", "percent": 82},
        {"date": "2025-12-20", "percent": 85},
    ]


def get_usage():
    return [
        {"date": "2025-12-01", "electricity_kwh": 120, "water_liters": 300},
        {"date": "2025-12-05", "electricity_kwh": 110, "water_liters": 280},
        {"date": "2025-12-10", "electricity_kwh": 100, "water_liters": 260},
        {"date": "2025-12-15", "electricity_kwh": 95, "water_liters": 250},
    ]


def get_chat_history():
    return [
        {
            "question": "When is exam?",
            "answer": "Exam is on 5th January"
        },
        {
            "question": "Is campus open today?",
            "answer": "Campus is closed today due to holiday"
        }
    ]
