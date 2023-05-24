function insertRole(roles, name) {
    if (name in roles) {
        alert("Role already exists!");
    } else {
        alert("Role added!");
    }
}
function insertIntern(interns, name, email, roles, ) {
    alert("Intern added!");
}
function cancel() {
    if(confirm("Are you sure you want to cancel?")){
        window.history.back();
    }
}