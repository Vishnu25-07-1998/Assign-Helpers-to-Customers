document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('db-menu').addEventListener('change', function() {
        var selectedOption = this.value;
        if (selectedOption === 'AddCustomer') {
            window.location.href = '/AddCustomer/';
        }
        else if (selectedOption === 'AddHelper') {
            window.location.href = '/AddHelper/';
        }
        else if (selectedOption === 'AssignHelper') {
            window.location.href = '/AssignHelper/';
        }
        else if (selectedOption === 'HelperDetails') {
            window.location.href = '/HelperDetails/';
        }
        else if (selectedOption === 'CustomerDetails') {
            window.location.href = '/CustomerDetails/';
        }
    });
});