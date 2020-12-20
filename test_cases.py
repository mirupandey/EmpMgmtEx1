from admin import admin_tasks
from employee import tasks
from employee.action import connection
from admin.action import admin_connection


def test_admin_view_dept():
    dept_id = 101
    dept = admin_tasks.AdminChecks()
    assert dept.view_dept(dept_id) == [(101, 'Development')]


def test_admin_view_emp():
    emp_id = 123
    emp_detail = admin_tasks.AdminChecks()
    assert emp_detail.view_emp(emp_id) == [('123', 'miru123', 'Mrinal', 'Pandey',
                                            102, 'Female', 9784314332, '1995-06-06')]


def test_emp_view_dept():
    dept_id = 102
    dept = tasks.EmpChecks()
    assert dept.view_dept(dept_id) == [(102, 'Support')]


def test_emp_view_emp():
    emp_id = 123
    emp_detail = tasks.EmpChecks()
    assert emp_detail.view_emp(emp_id) == [('123', 'miru123', 'Mrinal', 'Pandey',
                                            102, 'Female', 9784314332, '1995-06-06')]


test_admin_view_emp()
test_emp_view_emp()
test_admin_view_dept()
test_emp_view_dept()
