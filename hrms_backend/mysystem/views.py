import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee, Attendance
from django.forms.models import model_to_dict


# Add Employee
@csrf_exempt
def add_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            employee = Employee.objects.create(
                employee_id=data["employee_id"],
                full_name=data["full_name"],
                email=data["email"],
                department=data["department"]
            )

            return JsonResponse({"message": "Employee created"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# List Employees
def list_employees(request):
    employees = list(Employee.objects.values())
    return JsonResponse(employees, safe=False)


# Delete Employee
@csrf_exempt
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return JsonResponse({"message": "Employee deleted"})
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)


# Mark Attendance
@csrf_exempt
def mark_attendance(request):
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            employee = Employee.objects.get(id=data["employee_id"])

            Attendance.objects.create(
                employee=employee,
                date=data["date"],
                status=data["status"]
            )

            return JsonResponse({"message": "Attendance marked"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# Get Attendance
def get_attendance(request):
    records = Attendance.objects.select_related("employee")

    data = []

    for r in records:
        data.append({
            "employee": r.employee.full_name,
            "date": r.date,
            "status": r.status
        })

    return JsonResponse(data, safe=False)