#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

struct Employee {
    char name[55];
    int salary;
};

bool cmp(const Employee& e1, const Employee& e2) {
    if (e1.salary != e2.salary) {
        return e1.salary < e2.salary;
    } else {
        return strcmp(e1.name, e2.name) < 0;
    }
}

int main() {
    int n;
    cin >> n;

    Employee employees[n];
    for (int i = 0; i < n; i++) {
        cin >> employees[i].name >> employees[i].salary;
    }

    sort(employees, employees + n, cmp);

    for (int i = 0; i < n; i++) {
        cout << employees[i].name << " " << employees[i].salary << endl;
    }

    return 0;
}